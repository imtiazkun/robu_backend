# Generated by Django 5.0 on 2024-01-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_blood_group_user_gender_user_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='insta_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='robu_department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
