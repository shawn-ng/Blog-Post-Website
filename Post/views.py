from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Post.models import Post
from Post.serializer import PostSerializer
from Friend.models import Friend
from UserProfile.models import UserProfile
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # creating a get request where all the post that friend post will be seen
    # get friends' blog post and portray it.
    # coditions
    # if they are friends && the profile is public then the post can be seen
    def get_queryset(self):
        # getting friend data
        friend_status = Friend.objects.filter(
            user_friend_id_one=self.request.user.id)

        friends_array = []

        # this is to go through each object and getting the friend list
        for friend in friend_status:
            # users must be friends
            if friend.request_status == True:
                friends_array.append(friend.user_friend_id_two.id)

        # checking the friend profile is public or private
        profiles = {}

        for _id in friends_array:
            profile_status = UserProfile.objects.filter(user_id_profile=_id)

            profiles[_id] = profile_status

        # profile that is public and friends with the user
        public_profile = []
        for key in profiles:
            for profile in profiles[key]:
                if profile.private == False:
                    public_profile.append(profile.profile_id)

        # blog post of the public and friend profile
        posts_pk = []

        for _id in public_profile:
            post = Post.objects.filter(profile_id=_id)
            for obj in post:
                posts_pk.append(obj.post_id)

        # user profile posts
        user_profile_posts_pk = []

        user_profiles = UserProfile.objects.filter(
            user_id_profile=self.request.user.id)

        for profile in user_profiles:
            post = Post.objects.filter(profile_id=profile.profile_id)
            for obj in post:
                user_profile_posts_pk.append(obj.post_id)

        result_post_array = posts_pk + user_profile_posts_pk

        return Post.objects.filter(pk__in=result_post_array)

    def destroy(self, request, pk):

        post = Post.objects.filter(post_id=pk)

        for profile in post:

            if self.request.user == profile.profile_id.user_id_profile:
                post.delete()
                return Response(f'Post deleted: {pk}', status=status.HTTP_200_OK)

        return Response('Failed to delete', status=status.HTTP_403_FORBIDDEN)
