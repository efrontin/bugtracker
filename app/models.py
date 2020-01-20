from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    password = models.CharField(max_length=55,
                                blank=True,
                                null=True)

    companies = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'


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

    created_at = models.DateTimeField(auto_now=True)

    company = models.ManyToManyField(Company, through='CompanyProject', related_name='projects')

    def __str__(self):
        return f'{self.name}'


class Role(models.Model):
    name = models.CharField(max_length=55,
                            default='No role')

    class Meta:
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    label = models.TextField(max_length=255,
                             default='No description')

    user = models.ManyToManyField('User')

    created_at = models.DateTimeField

    updated_at = models.DateTimeField

    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE)

    level = models.ForeignKey(Level,
                              on_delete=models.CASCADE)

    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.label}'


class CompanyProject(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    is_client = models.BooleanField(blank=False)

    def __str__(self):
        if self.is_client:
            return f'{self.company} a effectué une demande'
        return f'{self.company} répond à une demande '

