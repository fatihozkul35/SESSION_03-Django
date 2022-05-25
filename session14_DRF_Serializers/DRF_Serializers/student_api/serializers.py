from dataclasses import fields
from rest_framework import serializers
from .models import Student, Path


# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

#     def create(self, validated_data):
#         # { first_name: '', last_name:'Veli', number:123486}
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get(
#             'first_name', instance.first_name)
#         instance.last_name = validated_data.get(
#             'last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(
        method_name='fullname')  # method name not defined :  get_full_name
    path = serializers.StringRelatedField()
    path_id = serializers.IntegerField()  # write_only=True

    class Meta:
        model = Student
        fields = ["id", "path", "path_id", "first_name",
                  "last_name", "number", "full_name"]
        # fields = '__all__'

        # exclude = ['number']

    def get_full_name():
        pass

    def fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class PathSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Path
        fields = ('id', 'path_name', 'students')
