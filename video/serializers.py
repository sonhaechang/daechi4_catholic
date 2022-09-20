from core.serializers import BaseCommentSerializer
from video.models import Comment

class CommentSerializer(BaseCommentSerializer):
	class Meta(BaseCommentSerializer.Meta):
		model = Comment