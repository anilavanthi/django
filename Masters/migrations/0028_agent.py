# Generated by Django 4.0.4 on 2023-06-02 05:58

import Masters.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Masters', '0027_rename_educaton_staff_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('maritalStatus', models.CharField(blank=True, max_length=15, null=True)),
                ('aadharno', models.CharField(blank=True, max_length=15, null=True)),
                ('dob', models.CharField(blank=True, max_length=50, null=True)),
                ('bankaccno', models.CharField(blank=True, max_length=15, null=True)),
                ('bankname', models.CharField(blank=True, max_length=50, null=True)),
                ('bankifsccode', models.CharField(blank=True, max_length=15, null=True)),
                ('bankbranchname', models.CharField(blank=True, max_length=50, null=True)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('modifiedon', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.SmallIntegerField(default=1, null=True)),
                ('photo', models.ImageField(blank=True, default='blank_pic', null=True, upload_to=Masters.models.agents_upload_to)),
                ('createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='agentcreated', to=settings.AUTH_USER_MODEL)),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='agent', to='Masters.education')),
                ('modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='agentupdated', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='agent_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
