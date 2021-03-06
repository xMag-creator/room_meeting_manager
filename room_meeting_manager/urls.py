"""room_meeting_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from manager.views import AddMeetingRoom, MeetingRoomsList, DeleteMeetingRoom, ModifyMeetingRoom, MakeReservation, \
    MeetingRoomDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new/', AddMeetingRoom.as_view()),
    path('room/', MeetingRoomsList.as_view()),
    path('room/delete/<room_id>', DeleteMeetingRoom.as_view()),
    path('room/modify/<room_id>', ModifyMeetingRoom.as_view()),
    path('room/reserve/<room_id>', MakeReservation.as_view()),
    path('room/<room_id>', MeetingRoomDetails.as_view())
]
