# Generated by Django 4.1.6 on 2023-11-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('residencia', models.CharField(max_length=200)),
                ('megas', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'ModelName',
                'verbose_name_plural': 'ModelNames',
            },
        ),
    ]