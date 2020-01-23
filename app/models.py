from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True,
                                  related_name='employees')

    def description(self):
        return ' / '.join([self.user.username, str(self.company)]).strip()

    def __str__(self):
        return f'{self.user}'


class Company(models.Model):
    name = models.CharField(max_length=255, )

    address = models.CharField(max_length=255, )

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):

        return f'{self.name}'


class Level(models.Model):
    label = models.CharField(max_length=55,
                             default='No level')

    def __str__(self):
        return f'{self.label}'


class Status(models.Model):
    label = models.CharField(max_length=55,
                             default='No Status')

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name_plural = 'Status'


class Project(models.Model):
    name = models.CharField(max_length=55, )

    created_at = models.DateTimeField(auto_now_add=True)

    company = models.ManyToManyField(Company, through='CompanyProject', related_name='projects')

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    label = models.TextField(max_length=255,
                             default='No description')

    user = models.ManyToManyField('Employee')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE)

    level = models.ForeignKey(Level,
                              on_delete=models.CASCADE)

    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f' ID {self.id} -  {self.project} - status : {self.status}'


class CompanyProject(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    is_client = models.BooleanField(blank=False)

    def __str__(self):
        if self.is_client:
            return f'{self.company} a effectué une demande'
        return f'{self.company} répond à une demande '

