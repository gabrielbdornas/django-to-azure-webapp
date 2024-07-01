# Generated by Django 4.2.7 on 2024-06-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_question_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='status',
        ),
        migrations.AddField(
            model_name='question',
            name='illustrator_status',
            field=models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete'), ('approved', 'Approved')], default='incomplete', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='proofreader_status',
            field=models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete'), ('approved', 'Approved'), ('pending', 'Pending')], default='incomplete', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='sinhala_status',
            field=models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete'), ('approved', 'Approved')], default='incomplete', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='tamil_status',
            field=models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete'), ('approved', 'Approved')], default='incomplete', max_length=20),
        ),
    ]
