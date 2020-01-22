"""bugtracker URL Configuration

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
from django.urls import path

from app.views import IndexView, TicketDetailView, TicketListView, UserListView, UserDetailView, CompanyListView, \
    CompanyDetailView, ProjectListView, ProjectDetailView, Login, TicketSearchByProjectListView, logout_user, \
    ProjectCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('tickets/<int:pk>', TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets', TicketListView.as_view(), name='ticket_list'),
    path('projects/<int:pk>/ticket-list', TicketSearchByProjectListView.as_view(), name='ticket_list_by_project'),
    path('users', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetailView.as_view, name='user_detail'),
    path('companies', CompanyListView.as_view(), name='company_list'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('projects', ProjectListView.as_view(), name='project_list'),
    path('projects/create', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail')
]
