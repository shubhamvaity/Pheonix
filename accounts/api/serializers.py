
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers


User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    # website = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'date_joined',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_superuser',
            'follower_count',
            # 'website',
            'url',
            # 'email',
        ]
    # def get_website(self, obj):
    #     return 0    

    def get_follower_count(self, obj):
        return 0

    def get_url(self, obj):
        return reverse_lazy("profiles:detail", kwargs={"username": obj.username })

