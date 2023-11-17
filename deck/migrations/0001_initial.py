# Generated by Django 4.2.7 on 2023-11-17 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Enter a question', max_length=1000)),
                ('answer', models.TextField(help_text='Enter an answer', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Pick a subject', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.subject')),
            ],
        ),
    ]