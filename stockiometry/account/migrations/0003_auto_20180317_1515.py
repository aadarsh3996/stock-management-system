# Generated by Django 2.0.1 on 2018-03-17 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180317_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='user_mobile_number',
            new_name='mobile_number',
        ),
    ]