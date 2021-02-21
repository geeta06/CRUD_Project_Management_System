from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.
from .models import Project, Task
from rest_framework.views import APIView
from .serializers import ProjectListSerializer, TaskListSerializer
#create your view here

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class RetrieveUpdateDeleteProject(APIView):
    """
    this api is used to get , update and delete existing Project with pk of project
    """

    def get_queryset(self, pk):
        try:
            project_object = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return None
        return project_object


    def get(self, request, pk):
        """
        to get the particular project details
        """
        try:
            project_object = self.get_queryset(pk)
            if not project_object:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Project Not Found'
                })
            serializer = ProjectListSerializer(
                project_object)
            return JSONResponse({
                'code': 1,
                'response': serializer.data,
                'message': 'Projects Retrieved Successfully'
            })
        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Retrieve Projects',

            })

    def put(self, request, pk):
        """
        to update particular projects
        """
        try:
            data = request.data
            project_object = self.get_queryset(pk)
            if not project_object:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Project Not Found'
                })
            project_serializer = ProjectListSerializer(
                instance=project_object,
                data=data
            )
            if not project_serializer.is_valid():
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Project updated Successfully',
                })
            project_serializer.save()
            return JSONResponse({
                'code': 1,
                'response': {},
                'message': 'Project updated Successfully',
            })

        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Update Project',
            })
    def delete(self, request, pk):
        """
        to delete particular project
        """
        try:
            data = request.data
            project_object = self.get_queryset(pk)
            if not project_object:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Project Not Found'
                })
            project_object.delete()
            return JSONResponse({
                'code': 1,
                'response': {},
                'message': 'Deleted Project Successfully',
            })
        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Delete Project',
            })

class ListCreateProject(APIView):
    """
    to get list of existing projects and creating new project
    """

    def get_queryset(self):
        projects = Project.objects.all()
        return projects

    def get(self, request):
        """
        to get list of exiting projects
        """
        project_queryset = self.get_queryset()
        serializer = ProjectListSerializer(project_queryset, many=True)
        return JSONResponse({
            'code':1,
            'response':serializer.data,
            'message':'Retrieved successfully'
        })

    def post(self, request):
        """
        to create new project
        """
        try:
            post_data = request.data
            name = post_data.get('name')
            project_name_exists = Project.objects.filter(name=name).exists()
            if project_name_exists:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Project with given name already exists, please provide unique name',
                })
            serializer = ProjectListSerializer(data=post_data)
            if not serializer.is_valid():
                return JSONResponse({
                    'code': 0,
                    'response': serializer.data,
                    'message': 'Project Not Created',
                })
            serializer.save()
            return JSONResponse({
                'code': 1,
                'response': serializer.data,
                'message': 'Project Created Successfully',
            })
        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Create Project',
            })


class RetrieveUpdateDeleteTask(APIView):
    """
        this api is used to get , update and delete existing Task with pk of Task
    """

    def get_queryset(self, pk):
        try:
            task_object = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return None
        return task_object

    def get(self, request, pk):
        """
        to get the particular Task details
        """
        try:
            task_object = self.get_queryset(pk)
            if not task_object:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Task Not Found'
                })
            serializer = TaskListSerializer(
                task_object)
            return JSONResponse({
                'code': 1,
                'response': serializer.data,
                'message': 'Task Retrieved Successfully'
            })
        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Retrieve Task',
            })

    def put(self, request, pk):
        """
        to update the particular Task details
        """
        try:
            data = request.data
            task_object = self.get_queryset(pk)
            if not task_object:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Task Not Found'
                })
            task_serializer = TaskListSerializer(
                instance=task_object,
                data=data
            )
            if not task_serializer.is_valid():
                return JSONResponse({
                    'code': 0,
                    'response': task_serializer.errors,
                    'message': 'Task not updated',
                })
            task_serializer.save()
            return JSONResponse({
                'code': 1,
                'response': {},
                'message': 'Task updated Successfully',
            })

        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Update Task',
            })

    def delete(self, request, pk):
        """
         to delete the particular task
        """
        try:
            data = request.data
            task_object = self.get_queryset(pk)
            if not task_object:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Task Not Found'
                })
            task_object.delete()
            return JSONResponse({
                'code': 1,
                'response': {},
                'message': 'Deleted Task Successfully',
            })
        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Delete Task',
            })


class ListCreateTask(APIView):
    """
    to get list of existing Tasks with given project and creating new Task referenced to project
    """

    def get_queryset(self, pk):
        tasks = Task.objects.filter(project=pk)
        return tasks

    def get(self, request, pk):
        """
         to get list of existing tasks with given project
        """
        tasks = self.get_queryset(pk)
        if not tasks:
            return JSONResponse({
                'code': 1,
                'response': {},
                'message': 'No tasks found with project id {} '.format(pk)
            })
        serializer = TaskListSerializer(tasks, many=True)
        return JSONResponse({
            'code': 1,
            'response': serializer.data,
            'message': 'Retrieved successfully'
        })

    def post(self, request, pk):
        """
        to create new task with given project
        """
        try:
            post_data = request.data
            name = post_data.get('name')
            start_date = post_data.get('start_date')
            end_date = post_data.get('end_date')
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            project_object = Project.objects.filter(id=pk).last()
            if not project_object:
                return JSONResponse({
                    'code':0,
                    'response':{},
                    'message':'Project does not exists, can not create tasks'
                })
            task_name_exists = Task.objects.filter(name=name).exists()
            if task_name_exists:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Task with given name already exists, please provide unique name',
                })
            serializer = TaskListSerializer(data=post_data)
            if not serializer.is_valid():
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': 'Task Not Created',
                })
            serializer.save()
            return JSONResponse({
                'code': 1,
                'response': serializer.data,
                'message': 'Task Created Successfully',
            })

        except Exception as e:
            return JSONResponse({
                'code': 0,
                'response': e,
                'message': 'Failed to Create Task',
            })
