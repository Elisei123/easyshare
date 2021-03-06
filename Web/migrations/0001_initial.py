# Generated by Django 3.0.3 on 2020-02-26 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='retele_de_socializare_utilizator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.CharField(max_length=40, null=True)),
                ('facebook', models.CharField(max_length=40, null=True)),
                ('instagram', models.CharField(max_length=40, null=True)),
                ('gmail', models.CharField(max_length=40, null=True)),
                ('youtube', models.CharField(max_length=40, null=True)),
                ('linkedin', models.CharField(max_length=40, null=True)),
                ('discord', models.CharField(max_length=40, null=True)),
                ('skype', models.CharField(max_length=40, null=True)),
                ('steam', models.CharField(max_length=40, null=True)),
                ('paypal', models.CharField(max_length=40, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
