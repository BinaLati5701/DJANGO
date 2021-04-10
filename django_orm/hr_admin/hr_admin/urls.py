"""hr_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# ==========================================================
from hr_app.models import Employee, Department, Job, JobHistory, Location, User
class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job, JobAdmin)

class JobHistoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(JobHistory, JobHistoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)



# ==================================================================

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hr_app.urls')),
]
