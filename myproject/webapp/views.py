from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees, JWTPayloadTrack
from . serializers import employeesSerializer, JWTPayloadTrackSerializer
import jwt
from django.views.decorators.csrf import csrf_exempt


class employeeList(APIView):
    @csrf_exempt
    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many=True)
        return HttpResponse(serializer.data)

    def post(self):
        pass


class TakeJWTPayload(APIView):
    @csrf_exempt
    def get(self, request):
        print('Header: ', request.headers)
        encoded_jwt = request.headers['Authorization']
        print('After Encode: ', encoded_jwt)

        if encoded_jwt:
            decoded_payloads = jwt.decode(encoded_jwt, 'MahfuzSecretKey', algorithms=['HS256'])
            print('After Decode: ', decoded_payloads)

            if decoded_payloads:
                saved_jwt_payloads = JWTPayloadTrack.objects.create(
                    username=decoded_payloads['username'],
                    password=decoded_payloads['password'],
                    # iat=decoded_payloads['iat']
                )

                serialized_payload = JWTPayloadTrackSerializer(saved_jwt_payloads)

                return Response(serialized_payload.data, status=status.HTTP_201_CREATED)

            else:
                return Response({'message': 'decode not working!'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message': 'jwt payload not found!'}, status=status.HTTP_404_NOT_FOUND)