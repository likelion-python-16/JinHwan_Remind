from rest_framework.serializers import ModelSerializer
from .models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        
        # fields = ["name", "description", "complete", "exp", "completed_at", "created_at", "updated_at"]
        # exclude = ["completed_at", "exp",]

        	
	
	
	
	
	
	