from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status,
                               default=1,
                               on_delete=models.CASCADE,
                               related_name='statuses')
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='creators')
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='doers')
    tags = models.ManyToManyField(Tag,
                                  default=1,
                                  related_name='tags')

    def get_absolute_url(self):
        return reverse('mainpage:view_task', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    def random_taskname():
        import random
        ROUTINE_TASKS = [
            'Hello'
        ]
        return random.choice(ROUTINE_TASKS)
