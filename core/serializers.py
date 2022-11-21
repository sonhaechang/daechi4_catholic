from rest_framework import serializers

class BaseCommentSerializer(serializers.ModelSerializer):
	''' Comment를 사용하는 모든 Commentview에서 상속 받아서 사용할 Base CommentSerializer '''

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
		''' obj의 성 반환 '''

		return obj.user.last_name

	def get_first_name(self, obj):
		''' obj의 이름 반환 '''

		return obj.user.first_name

	def get_created_at(self, obj):
		''' obj의 (Y-m-d)형식의 생성일 반환 '''

		return obj.updated_at.strftime('%Y-%m-%d')

	def get_is_mine(self, obj):
		''' comment의 작성자가 self.user인지 반환 '''

		return obj.user == self.user

	def get_is_authenticated(self, obj):
		''' 로그인 여부 반환 '''

		return self.user.is_authenticated

	def get_replies(self, instance):
		''' 대댓글 데이터 반환 '''

		serializer = self.__class__(instance.replies, many=True)
		serializer.bind('', self)
		return serializer.data