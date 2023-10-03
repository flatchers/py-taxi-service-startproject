# Generated by Django 4.0.2 on 2023-10-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to. '
                          'A user will get all permissions granted '
                          'to each of their groups.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Group',
                verbose_name='groups'
            ),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='user_permissions',
            field=models.ManyToManyField(
                blank=True,
                help_text='Specific permissions for this user.',
                related_name='user_set', related_query_name='user',
                to='auth.Permission', verbose_name='user permissions'
            ),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
