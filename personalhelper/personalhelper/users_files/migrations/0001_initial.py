# Generated by Django 3.2.7 on 2021-09-07 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='files/')),
                ('category', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]