from django.shortcuts import render
from proj.models import Account, DataLog, StatusLog, Maintenance
from proj.serializers import AccountSerializer, DataLogSerializer, StatusLogSerializer, MaintenanceSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 

# Create your views here.

#class to create user accounts
class AllAccount(APIView):
    '''
        A class to get all accounts
    '''
    def get(self,requests):
        accounts = Account.objects.all().order_by("id")
        serializer = AccountSerializer(accounts,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)


#class to login the user
class AccountLogin(APIView):
    '''
        A class to login the user
    '''
    def post(self,request):
        data = request.data
        try:
            account = Account.objects.filter(email=data['email']).filter(password=data['password']).first()
            if not account:
                raise Account.DoesNotExist
        except Account.DoesNotExist:
            return Response({'error':'Credentials provided did\'nt matched'})
        serializer = AccountSerializer(account)
        return Response(serializer.data)

#class to get all data logs
class AllDataLog(APIView):

    def get(self,requests):
        log = DataLog.objects.all().order_by("id")
        serializer = DataLogSerializer(log,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = DataLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to get all status logs
class AllStatusLog(APIView):

    def get(self,requests):
        slog = StatusLog.objects.all().order_by("id")
        serializer = StatusLogSerializer(slog,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = StatusLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)


#class to get all the maintenance 
class AllMaintenance(APIView):
    '''
        A class to get all accounts
    '''
    def get(self,requests):
        maintenance = Maintenance.objects.all().order_by("id")
        serializer = MaintenanceSerializer(maintenance,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = MaintenanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to get the last data log
class LastDataLog(APIView):
    '''
        A class to get the current/last data read from the sensor 
    '''
    def get(self,request,chamber_id,format=None):
        try:
            last = DataLog.objects.filter(chamber_id=chamber_id).last()
        except DataLog.DoesNotExist:
            return Response({},status=200)
        serializer = DataLogSerializer(last)
        return Response(serializer.data)


#class to get latest data logs
class LatestReadings(APIView):
    '''
        A class to get the latest readings of  sensors
    '''
    def get(self,request,chamber_id,format=None):
        try:
            latest = DataLog.objects.filter(chamber_id=chamber_id).order_by('-timestamp_log')[:15]
            if not latest:
                raise DataLog.DoesNotExist
        except DataLog.DoesNotExist:
            return Response({'error':'something went wrong'})
        serializer = DataLogSerializer(latest,many=True)
        return Response(serializer.data)


class LatestStatus(APIView):
    '''
        A class to get the latest status readings 
    '''
    def get(self,request,format=None):
        try:
            slatest = StatusLog.objects.order_by('-timestamp')[:15]
            if not slatest:
                raise StatusLog.DoesNotExist
        except StatusLog.DoesNotExist:
            return Response({'error':'something went wrong'})
        serializer = StatusLogSerializer(slatest,many=True)
        return Response(serializer.data)


#class to get the last data log
class LastStatusLog(APIView):
    '''
        A class to get the current/last data read from the sensor 
    '''
    def get(self,request,format=None):
        try:
            last = StatusLog.objects.last()
        except StatusLog.DoesNotExist:
            return Response({},status=200)
        serializer = StatusLogSerializer(last)
        return Response(serializer.data)




    