# Generated by Django 2.1.5 on 2019-02-20 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20190217_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='framework',
            field=models.ManyToManyField(blank=True, related_name='projects', to='manager.Framework'),
        ),
        migrations.AlterField(
            model_name='project',
            name='keyword',
            field=models.ManyToManyField(blank=True, related_name='projects', to='manager.Keyword'),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='projects', to='manager.Language'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team_member',
            field=models.ManyToManyField(blank=True, related_name='projects', to='manager.TeamMember'),
        ),
    ]