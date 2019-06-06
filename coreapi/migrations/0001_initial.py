# Generated by Django 2.2.1 on 2019-06-05 06:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('imagefile', models.FileField(upload_to='images/')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InputVideo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('videofile', models.FileField(upload_to='videos/')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
