from django.contrib import admin, messages
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django_summernote.admin import SummernoteModelAdmin

from information.models import (
	Carousel,
	Introduce, Condition,
	FatherSister,
	History,
	JumbotronImage,
	PastoralOrientation,
	Popup
)

from core.widgets import PreviewClearbleFileInput


# Register your models here.
class CheckCountMixins(object):
	def save_model(self, request, obj, form, change):
		if not change:
			meta = obj._meta
			message = _(f'해당 데이터는 최대 {self.check_num}개까지 생성 가능합니다. \
				기존 데이터를 수정하거나 삭제후 다시 생성해주세요.')

			if self.model.objects.count() >= int(self.check_num):
				messages.set_level(request, messages.ERROR)
				messages.error(request, message)
				return reverse(f'admin:{meta.app_label}_{meta.model_name}_changelist')
			
		super().save_model(request, obj, form, change)


@admin.register(Carousel)
class CarouselAdmin(CheckCountMixins, admin.ModelAdmin):
	model = Carousel
	check_num = 5

	formfield_overrides = {
		models.ImageField: {'widget': PreviewClearbleFileInput}
	}


class ConditionInline(admin.StackedInline):
    model = Condition
    raw_id_fields = ['introduce']
    extra = 0


@admin.register(Introduce)
class IntroduceAdmin(CheckCountMixins, SummernoteModelAdmin):
	inlines = [ConditionInline,]
	model = Introduce
	check_num = 1

	formfield_overrides = {
		models.ImageField: {'widget': PreviewClearbleFileInput}
	}

@admin.register(FatherSister)
class FatherSisterAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ImageField: {'widget': PreviewClearbleFileInput}
	}


@admin.register(JumbotronImage)
class JumbotronImageAdmin(CheckCountMixins, admin.ModelAdmin):
	model = JumbotronImage
	check_num = 8

	formfield_overrides = {
		models.ImageField: {'widget': PreviewClearbleFileInput}
	}


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
	pass


@admin.register(PastoralOrientation)
class PastoralOrientationAdmin(CheckCountMixins, SummernoteModelAdmin):
	model = PastoralOrientation
	check_num = 1


@admin.register(Popup)
class PopupAdmin(CheckCountMixins, SummernoteModelAdmin):
	model = Popup
	check_num = 1