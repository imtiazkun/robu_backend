# Generated by Django 5.0 on 2024-01-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_insta_link_user_robu_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default.jpg', null=True, upload_to='avatars/'),
        ),
    ]
