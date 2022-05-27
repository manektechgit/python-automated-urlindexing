# Generated by Django 3.2.11 on 2022-05-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('tigger_url', models.URLField()),
                ('ranking', models.IntegerField()),
                ('system_ip', models.GenericIPAddressField()),
                ('country', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Url_index',
                'ordering': ['content'],
            },
        ),
    ]