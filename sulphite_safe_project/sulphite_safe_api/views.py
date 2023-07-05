# from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Beverage, SulphiteStatus, BeverageSulphiteStatus, UserBeverageSulphiteStatus
from .serializers import UserSerializer, BeverageSerializer, SulphiteStatusSerializer, BeverageSulphiteStatusSerializer, UserBeverageSulphiteStatusSerializer

# def index(request):
#     return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib import messages

class UserViewSet(viewsets.ModelViewSet):
    '''
    to see this viewset in action, go to http://127.0.01:8000/api/users/
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    related_name='users'

class BeverageViewSet(viewsets.ModelViewSet):
    '''
    to see this viewset in action, go to http://127.0.01:8000/api/beverages/
    '''
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer

class SulphiteStatusViewSet(viewsets.ModelViewSet):
    '''
    to see this viewset in action, go to http://127.0.01:8000/api/sulphite_statuses/
    '''
    queryset = SulphiteStatus.objects.all()
    serializer_class = SulphiteStatusSerializer

    def destroy(request, sulphite_status_id):
        sulphite_status = SulphiteStatus.objects.get(id=sulphite_status_id)
        if sulphite_status.beverage_sulphite_statuses.all():
            messages.error(request, 'You cannot delete a sulphite status that has a beverage')
            return redirect('/sulphite_statuses')
        else:
            sulphite_status.delete()
            return redirect('/sulphite_statuses')

class BeverageSulphiteStatusViewSet(viewsets.ModelViewSet):
    '''
    to see this viewset in action, go to http://127.0.01:8000/api/beverage_sulphite_statuses/
    '''
    queryset = BeverageSulphiteStatus.objects.all()
    serializer_class = BeverageSulphiteStatusSerializer

class UserBeverageSulphiteStatusViewSet(viewsets.ModelViewSet):
    '''
    to see this viewset in action, go to http://127.0.01:8000/api/user_beverage_sulphite_statuses/
    '''
    queryset = UserBeverageSulphiteStatus.objects.all()
    serializer_class = UserBeverageSulphiteStatusSerializer
