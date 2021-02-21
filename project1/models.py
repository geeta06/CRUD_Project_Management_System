from django.db import models


# create models from here

class Project(models.Model):
    """A project the user is working on."""
    name = models.CharField(max_length=70, null=True, editable=True)
    description = models.CharField(max_length=200)
    duration = models.DateTimeField(auto_now_add=True)
    avtar = models.ImageField(upload_to='pics')

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Task(models.Model):
    """A task of a project to complete."""
    name = models.CharField(max_length=70, null=True, editable=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        """Return a string representation of the model."""
        return self.name
