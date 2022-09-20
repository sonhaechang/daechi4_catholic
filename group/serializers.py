from core.serializers import BaseCommentSerializer
from group.models import Comment

class CommentSerializer(BaseCommentSerializer):
	class Meta(BaseCommentSerializer.Meta):
		model = Comment