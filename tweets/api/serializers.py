from django.utils.timesince import timesince
from rest_framework import serializers


from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet # from ..models import Tweet


class ParentTweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) #write_only
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    dp = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'dp',
            'timestamp',
            'date_display',
            'timesince',
            'likes',
            'did_like',
           

        ]

    def get_did_like(self, obj):
        try:
            user = request.user
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
        except:
            pass
        return False


    def get_dp(self,obj):
        username = obj.user.username
        if "H3M3N" in username :
                dp_file = username + '.png'
                return dp_file
        if "shubham" in username :
                dp_file = username + '.png'
                return dp_file
        if "indra" in username :
                dp_file = username + '.png'
                return dp_file        
        username = username[0]
        username = username.lower()
        dp_file = username + '.png'
        return dp_file    

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"


class TweetModelSerializer(serializers.ModelSerializer):
    parent_id = serializers.CharField(write_only=True, required=False)
    user = UserDisplaySerializer(read_only=True) #write_only
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    parent = ParentTweetModelSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    dp = serializers.SerializerMethodField()
    # image = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'parent_id',
            'id',
            'user',
            'content',
            # 'image',
            'dp',
            'timestamp',
            'date_display',
            'timesince',
            'parent',
            'likes',
            'did_like',
            'reply',
        ]
        #read_only_fields = ['reply']
    # def get_image(self, obj):
      
    def get_dp(self,obj):
        username = obj.user.username
        if "H3M3N" in username :
                dp_file = username + '.png'
                return dp_file
        if "shubham" in username :
                dp_file = username + '.png'
                return dp_file
        if "indra" in username :
                dp_file = username + '.png'
                return dp_file     
        username = username[0]
        username = username.lower()
        dp_file = username + '.png'
        return dp_file

    def get_did_like(self, obj):
        request = self.context.get("request")
        try:
            user = request.user
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
        except:
            pass
        return False

    def get_likes(self, obj):
        return obj.liked.all().count()

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"