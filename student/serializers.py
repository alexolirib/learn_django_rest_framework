from rest_framework import  serializers

from student.models import Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    #students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.ReadOnlyField(source='owner.username')



    class Meta:
        model = User
        # fields = ('id', 'username' , 'students', 'owner')
        fields = ('id' , 'students', 'owner')


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('id', 'name', 'age', 'discount')