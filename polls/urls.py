from django.urls import path 
from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView 
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    #path('polls/', PollList.as_view(), name='polls_list'),
    #path('polls/<int:pk>', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='Choice_List'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='Create_Vote '),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
]
urlpatterns += router.urls  