# Generated by Django 5.2 on 2025-04-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(choices=[('Политика', 'Политика'), ('Технологии', 'Технологии'), ('Бизнес', 'Бизнес')], max_length=20, null=True, verbose_name='Тег'),
        ),
    ]
