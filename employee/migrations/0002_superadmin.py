# Generated by Django 3.2.6 on 2021-11-12 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Superadmin',
            fields=[
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]