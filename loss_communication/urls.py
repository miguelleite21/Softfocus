
from django.urls import path
from loss_communication.views import Loss_communicationViw,Loss_communicationIdViw

urlpatterns = [path("",Loss_communicationViw.as_view()),path("<int:id>/",Loss_communicationIdViw.as_view())]