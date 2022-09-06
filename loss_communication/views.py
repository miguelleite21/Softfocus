from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from loss_communication.models import Loss_communication
from loss_communication.serializers import Loss_communicationSerializer

class Loss_communicationViw(APIView):

    def get(self, request:Request):
        communications = Loss_communication.objects.all()
        serialized = Loss_communicationSerializer(instance=communications,many=True)
        return Response({"communications":serialized.data},status.HTTP_200_OK)

    def post(self, request:Request):
        serialized = Loss_communicationSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        try:
            serialized.save()
            return Response(serialized.data, status.HTTP_201_CREATED)
        except ValueError as error:
            return Response(*error.args)

class Loss_communicationIdViw(APIView):
    def patch(self,request:Request, id:int):
        try:
            communication = get_object_or_404(Loss_communication,pk=id)
            serialized = Loss_communicationSerializer(communication,request.data, partial=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data,status.HTTP_200_OK)
        except Http404:
            return Response({"detail": "Loss communication not found."}, status.HTTP_404_NOT_FOUND)

        except KeyError as err:
            return Response(*err.args)
  

    def delete(self,_:Request, id:int):
        communication = get_object_or_404(Loss_communication,pk=id)
        communication.delete()
        return Response("",status.HTTP_204_NO_CONTENT)
    

