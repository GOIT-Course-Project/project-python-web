# Generated by Django 3.2.7 on 2021-09-11 11:48

from django.db import migrations, models
import storages.backends.sftpstorage
import users_files.models


class Migration(migrations.Migration):

    dependencies = [
        ('users_files', '0002_alter_userfile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='category',
            field=models.CharField(choices=[('videos', 'videos'), ('audios', 'audios'), ('documents', 'documents'), ('fotos', 'fotos')], max_length=25),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='file',
            field=models.FileField(storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='files/', validators=[users_files.models.file_size]),
        ),
    ]
