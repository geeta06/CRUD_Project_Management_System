from django.conf.urls import url, include
from .views import ListCreateProject, RetrieveUpdateDeleteProject,\
    ListCreateTask, RetrieveUpdateDeleteTask

urlpatterns = [
    url(r'project$', ListCreateProject.as_view(), name='Projects'),  # To get list of existing projects and creating new project
    url(r'project/(?P<pk>[0-9]+)$', RetrieveUpdateDeleteProject.as_view(), name='Project'), # To get, update, and delete existing given project with pk
    url(r'project/(?P<pk>[0-9]+)/task$', ListCreateTask.as_view(), name='Tasks'), #To get existing list of tasks for given project pk and creating new tasks
    url(r'task/(?P<pk>[0-9]+)$', RetrieveUpdateDeleteTask.as_view(), name='Task ') #To get, update, and delete given task with pk
]
