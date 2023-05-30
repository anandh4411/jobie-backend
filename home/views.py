from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Application, Company, Job, Notification, User, UserFiles
from .serializers import  ApplicationSerializer, CompanySerializer, JobSerializer, UserFilesSerializer, UserSerializer
from django.core.mail import send_mail, EmailMessage
import random
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view()
def home(request):
    return Response({'message': "APIs for Jobie Application"})


@api_view(['GET','POST','PUT','DELETE'])
def user(request, id):

    try:
        user = get_object_or_404(User, user_id=id) 
    except:
        pass

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET','POST','PUT','DELETE'])
def user_files(request, id):

    try:
        user_file = get_object_or_404(UserFiles, user_id=id) 
    except:
        pass

    if request.method == 'GET':
        serializer = UserFilesSerializer(user_file)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        serializer = UserFilesSerializer(user_file, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        user_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def user_id_check(request, id):

    if request.method == 'GET':
        try:
            user = User.objects.get(user_id=id)
        except:
            return Response({"message":"false"})
        return Response({"message":"true"})
    

@api_view(['GET'])
def user_verify_email(request, email):
    if request.method == 'GET':
        otp = random.randint(1000, 9999)
        subject = 'Jobie'
        message = f'Your Jobie OTP is {otp}. Please enter this otp to verify your email address.'
        recipient = email
        send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        return Response({"otp":otp})
        


@api_view(['GET'])
def jobs(request):

    try:
        jobs = list(Job.objects.all().values() )
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(jobs, safe=False)


@api_view(['GET'])
def companies(request):

    try:
        companies = list(Company.objects.all().values())
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(companies, safe=False)


@api_view(['GET'])
def job(request, id):

    try:
        job = get_object_or_404(Job, id=id) 
    except:
        pass

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)
    
@api_view(['GET'])
def company(request, id):

    try:
        company = get_object_or_404(Company, company_id=id) 
    except:
        pass

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)


@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        email = serializer.data['email']
        password = serializer.data['password']
        queryset = User.objects.all()
        for user in queryset:
            if user.password == password:
                if user.email == email:
                    return Response({"message":"true", "user_id":user.user_id})
        return Response({"message":"false"})


@api_view(['GET'])
def search(request, query):
    try:
        jobs = list(Job.objects.filter(title__contains=query).values() )
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(jobs, safe=False)
    

@api_view(['POST'])
def job_apply(request):

    if request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        job = serializer.data['job']
        subject = 'Jobie'
        message = f'Your application for {job} has successfully submited. The company will contact you back soon.'
        recipient = serializer.data['email']
        mail = EmailMessage(subject, message, to=[recipient])
        mail.send(fail_silently=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def job_check(request):
    if request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        userid = serializer.data['user_id']
        jobid = serializer.data['job_id']
        queryset = Application.objects.all()
        for application in queryset:
            if application.user_id == userid:
                if application.job_id == jobid:
                    return Response({"message":"true"})
        return Response({"message":"false"})
    

@api_view(['GET'])
def notifications(request, id):
    try:
        jobs = list(Notification.objects.filter(user__contains=id).values().order_by('-id'))
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(jobs, safe=False)
    

@api_view(['GET'])
def job_count(request, id):
    try:
        applications = list(Application.objects.filter(user_id__contains=id).values().count())
    except:
        pass

    if request.method == 'GET':
        return JsonResponse(applications, safe=False)