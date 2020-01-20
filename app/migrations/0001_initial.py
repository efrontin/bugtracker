# Generated by Django 2.2.7 on 2020-01-20 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('is_client', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Level')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Status')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('password', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='companies',
            field=models.ManyToManyField(through='app.UserCompany', to='app.Company'),
        ),
        migrations.CreateModel(
            name='TicketUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='user_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_client', to='app.User'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user_dev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_dev', to='app.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Status'),
        ),
    ]
