from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = 'id', 'name', 'description', 'address'

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    salary = serializers.FloatField()
    company = CompanySerializer()