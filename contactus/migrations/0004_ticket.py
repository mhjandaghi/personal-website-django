# Generated by Django 5.0.3 on 2024-03-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_rename_isntagram_footer_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('mail', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=80)),
                ('text', models.TextField()),
            ],
        ),
    ]
