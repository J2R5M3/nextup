# Generated by Django 3.2 on 2021-04-14 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('cover_art_url', models.CharField(max_length=200)),
            ],
        ),
    ]