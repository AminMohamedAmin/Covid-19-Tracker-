# Generated by Django 2.2.3 on 2020-04-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egypt', '0004_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('puplish', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-puplish',),
            },
        ),
    ]
