from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models.Movie import Movie
from .models.Actor import Actor
from .serializer import ActorSerializers, MovieSerializers
from .models.Comment import Comment
from .serializer import Comment_serializers
from rest_framework import generics


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class MovieAPIView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializers = MovieSerializers(movie, many=True)
        return Response(data=serializers.data)

    def post(self, request):
        pass


class ActorAPIView(APIView):
    def get(self, request):
        actor = Actor.objects.all()
        serializers = ActorSerializers(actor, many=True)
        return Response(data=serializers.data)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    @action(detail=True, methods=['POST'])
    def add_actor(self, requerst, *args, **kwargs):
        data = requerst.data
        name = data['name']
        year = data['year']
        imdb = data['imdb']
        genree = data['genree']
        actors = data['actors']
        actor = Actor.objects.create(
            name=name,
            year=year,
            imdb=imdb,
            genree=genree,
            actors=actors
        )
        movie = self.get_object()
        movie.actors.add(actor)
        movie.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentApiView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializers = Comment_serializers(comment, many=True)

        return Response(data=serializers.data)


class CommentDeleteApiViews(generics.UpdateAPIView):
    queryset = Comment
    serializer_class = Comment_serializers
