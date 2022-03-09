# Generated by Django 3.2.9 on 2022-03-09 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_course_courseold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.talk')),
                ('slot', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
            bases=('core.talk',),
        ),
    ]
