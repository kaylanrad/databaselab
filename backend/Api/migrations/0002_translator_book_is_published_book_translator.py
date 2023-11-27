# Generated by Django 4.2.6 on 2023-11-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=32)),
                ('translate_lang', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(null=True, to='Api.translator'),
        ),
    ]