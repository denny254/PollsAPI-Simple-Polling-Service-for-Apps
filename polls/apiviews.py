from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView 
from .models import poll, choice
from .serializers import PollSerializers, ChoiceSerializers, VoteSerializers, UserSerializers 
from django.contrib .auth import authenticate 
from rest_framework.exceptions import PermissionDenied


class PollViewSet(viewsets.ModelViewSet):
    queryset = poll.objects.all()
    serializer_class = PollSerializers

    def destroy(self, request, *args, **kwargs):
        Poll = poll.objects.get(pk=self.kwargs['pk'])
        if not request.user == Poll.created_by:
            raise PermissionDenied('You can not delete this poll.')
        return super().destroy(request, *args, **kwargs)
     
# class PollList(generics.ListCreateAPIView):
#     queryset = poll.objects.all()
#     serializer_class = PollSerializers

# class PollDetail(generics.RetrieveDestroyAPIView):
#     queryset = poll.objects.all()
#     serializer_class = PollSerializers 


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializers

    authentication_classes = ()
    permission_classes = ()

class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializers

    def post(self, request, *args, **kwargs):
        try:
            Poll = poll.objects.get(pk=self.kwargs['pk'])
        except poll.DoesNotExist:
            raise PermissionDenied('Poll does not exist')

        if not request.user == Poll.created_by:
            raise PermissionDenied('You cannot create a choice for this poll')

        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        queryset = choice.objects.filter(Poll_id=self.kwargs['pk'])
        return queryset
        
    
class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializers 
   

    def post(self, request, pk, choice_pk): 
        voted_by = request.data.get('voted_by')
        data = {'choice':choice_pk, 'poll':pk, 'voted_by': voted_by}
        serializer = VoteSerializers(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = password.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token':user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)