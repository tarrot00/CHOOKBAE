# Generated by Django 3.2.12 on 2022-11-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.TextField(blank=True, default='user/default.png', null=True),
        ),
    ]