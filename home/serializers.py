from rest_framework import serializers
from .models import Application, Company, Job, Notification, User, UserFiles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','user_id','name','profession','about','phone','email','location','password']

class UserFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFiles
        fields = ['id','user_id','profile_image','cover_image','resume']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','company_id','title','mode','salary','recruitment_type','description']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','company_id','name','location','phone','email','website','about','profile_image','cover_image']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id','name','phone','email','location','job','company','salary','mode','user_id','job_id']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id','user','company','title','notification','time','job','salary','mode']