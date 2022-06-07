from rest_framework import serializers
from fscohort.models import Student, Course



class CourseSerializer(serializers.ModelSerializer):
    
    students = serializers.StringRelatedField(many=True)
    student_counts = serializers.SerializerMethodField()

    class Meta:
        model = Course
        # fields = "__all__"
        fields = ["id", "title", "student_counts", "students"]   
        
    def get_student_counts(self, obj):        
        return obj.students.count()


class StudentSerializer(serializers.ModelSerializer):

 
    course = serializers.StringRelatedField()    # read_only
    course_id = serializers.IntegerField()       # course_id yi ezdik yoksa strrelatedfield ile create edemiyorduk

    class Meta:
        model = Student
        fields = '__all__'
