# Generated by Django 4.0 on 2022-01-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0002_category_object_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Целевой приоритет', 'verbose_name_plural': 'Целевые приоритеты'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'ordering': ['title', 'time_create'], 'verbose_name': 'Возможные направления', 'verbose_name_plural': 'Возможные направления'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Приоритет'),
        ),
    ]
