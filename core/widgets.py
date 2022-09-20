from django import forms


class PreviewClearbleFileInput(forms.ClearableFileInput):
    template_name = 'widgets/preview_clearable_file_input.html'