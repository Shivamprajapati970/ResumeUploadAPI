# Generated by Django 5.0.6 on 2024-05-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('MP', 'MP'), ('UP', 'UP'), ('AP', 'AP'), ('GJ', 'GJ')], max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('dock', models.FileField(blank=True, upload_to='dock')),
            ],
        ),
    ]
