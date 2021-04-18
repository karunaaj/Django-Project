from rest_framework import serializers
from proj.models import Account, DataLog, StatusLog, Maintenance

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"

class DataLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataLog
        fields = "__all__"

class StatusLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusLog
        fields = ("id","status","timestamp","log_fid")

        #for foreign key datalog
    def to_representation(self,instance):
        self.fields["log_fid"] = DataLogSerializer(read_only=True)
        return super().to_representation(instance)

class MaintenanceSerializer(serializers.ModelSerializer):
    '''
        serializer class for the maintenance model
    '''
    class Meta:
        model = Maintenance
        fields = ("id","date","description","resolved","account")
    #for foreign key account
    def to_representation(self,instance):
        self.fields["account"] = AccountSerializer(read_only=True)
        return super().to_representation(instance)
