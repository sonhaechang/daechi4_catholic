from core.serializers import BaseCommentSerializer
from flower.models import Comment

class CommentSerializer(BaseCommentSerializer):
	class Meta(BaseCommentSerializer.Meta):
		model = Comment