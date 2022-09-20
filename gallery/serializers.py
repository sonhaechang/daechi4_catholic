from core.serializers import BaseCommentSerializer
from gallery.models import Comment

class CommentSerializer(BaseCommentSerializer):
	class Meta(BaseCommentSerializer.Meta):
		model = Comment