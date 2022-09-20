from rest_framework import serializers

class BaseCommentSerializer(serializers.ModelSerializer):
	parent_id = serializers.SerializerMethodField()
	last_name = serializers.SerializerMethodField()
	first_name = serializers.SerializerMethodField()
	created_at = serializers.SerializerMethodField()
	is_mine = serializers.SerializerMethodField()
	is_authenticated = serializers.SerializerMethodField()
	replies = serializers.SerializerMethodField()

	class Meta:
		fields = ['id', 'parent_id', 'comment', 'last_name', 'first_name', 'created_at', 'is_mine', 'is_authenticated', 'replies']
		read_only_fields = ['last_name', 'first_name']

	def get_parent_id(self, obj):
		return obj.parent.pk if obj.parent else obj.parent

	def get_last_name(self, obj):
		return obj.user.last_name

	def get_first_name(self, obj):
		return obj.user.first_name

	def get_created_at(self, obj):
		return obj.updated_at.strftime('%Y-%m-%d')

	def get_is_mine(self, obj):
		return obj.user == self.user

	def get_is_authenticated(self, obj):
		return self.user.is_authenticated

	def get_replies(self, instance):
		serializer = self.__class__(instance.replies, many=True)
		serializer.bind('', self)
		return serializer.data