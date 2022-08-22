from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all_workers(request):
    return Response({"name":"okumu justine"})
