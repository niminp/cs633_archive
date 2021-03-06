# Generated by Django 2.1.5 on 2019-02-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_keyword_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.ManyToManyField(related_name='projects', to='manager.Language'),
        ),
    ]
