# Generated by Django 3.0.8 on 2020-08-11 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=264, verbose_name='Put a Word')),
                ('meaning', models.CharField(max_length=264, verbose_name='Meaning')),
                ('word_image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('google', models.URLField(max_length=264)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='MyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylist', to=settings.AUTH_USER_MODEL)),
                ('vocab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary', to='vocabulary.Vocabulary')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_comment', to='vocabulary.Vocabulary')),
            ],
            options={
                'ordering': ('-comment_date',),
            },
        ),
    ]