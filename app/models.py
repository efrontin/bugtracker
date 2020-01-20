from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    role = models.CharField(max_length=50,
                            blank=False,
                            null=False)
    password = models.TextField(blank=True,
                                null=True)

    companies = models.ManyToManyField('Company', through='UserCompany')

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(max_length=255)

    address = models.CharField(max_length=255)

    is_client = models.BooleanField(blank=False)


class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company = models.ForeignKey( Company, on_delete=models.CASCADE)


class Level(models.Model):
    label = models.CharField


class Status(models.Model):
    label = models.CharField


class Project(models.Model):
    name = models.CharField(max_length=55)

    created_at = models.DateTimeField

    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE)


class Ticket(models.Model):
    label = models.CharField

    user_client = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField

    updated_at = models.DateTimeField

    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE)

    level = models.ForeignKey(Level,
                              on_delete=models.CASCADE)

    user_dev = models.ForeignKey(User, on_delete=models.CASCADE)

    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)


class TicketUser(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        pass

