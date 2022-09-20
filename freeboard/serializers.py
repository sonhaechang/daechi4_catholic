from core.serializers import BaseCommentSerializer
from freeboard.models import Comment

class CommentSerializer(BaseCommentSerializer):
	class Meta(BaseCommentSerializer.Meta):
		model = Comment