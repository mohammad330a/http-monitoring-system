from rest_framework import serializers

from core.models import Server


class ServerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['id', 'address', 'success', 'failure', 'last_failure', 'created_at']
        read_only_fields = ['id', 'success', 'failure', 'last_failure', 'created_at']
