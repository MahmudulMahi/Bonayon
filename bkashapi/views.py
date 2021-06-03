from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from bkash_webhook import BkashWebhookListener,ValidationError
from .models import  BkashPayload
# Create your views here.

class BkashExample(APIView):
    authentication_classes = ()
    permission_classes = ()
    def post(selfself,request):
        try:
            bkash = BkashWebhookListener(json.loads(request.body))
            response = bkash.bkash_response_process()
            if response is not None:
                BkashPayload.objects.create(payload=response)

            return Response(data={"status" : "success"},status = 200)
        except ValidationError as err:
            return Response(data=err.message,status=err.status_code)