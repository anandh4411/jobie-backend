from django.contrib import admin
from .models import Application, Company, Job, Notification, User, UserFiles

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','name','profession','about','phone','email','location','password']
    list_editable = ['name','profession','about','phone','email','location','password']


@admin.register(UserFiles)
class UserFilesAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','profile_image','cover_image','resume']
    list_editable = ['profile_image','cover_image','resume']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','company_id','name','location','phone','email','website','about','profile_image','cover_image']
    list_editable = ['company_id','name','location','phone','email','website','about','profile_image','cover_image']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id','company_id','title','mode','salary','recruitment_type','description']
    list_editable = ['company_id','title','mode','salary','recruitment_type','description']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','location','job','company','salary','mode','user_id','job_id','resume']
    list_editable = ['name','phone','email','location','job','company','salary','mode','user_id','job_id','resume']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','user','company','title','notification','time','job','salary','mode']
    list_editable = ['user','company','title','notification','time','job','salary','mode']