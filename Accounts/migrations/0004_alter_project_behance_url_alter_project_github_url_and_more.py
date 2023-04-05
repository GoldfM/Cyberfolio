# Generated by Django 4.1.7 on 2023-04-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_user_behance_url_alter_user_hh_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='behance_url',
            field=models.URLField(blank=True, max_length=128, verbose_name='BH'),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.URLField(blank=True, max_length=128, verbose_name='github'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='user',
            name='behance_url',
            field=models.URLField(max_length=128, verbose_name='BH'),
        ),
        migrations.AlterField(
            model_name='user',
            name='hh_url',
            field=models.URLField(max_length=128, verbose_name='HH'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sur_name',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sur_sur_name',
            field=models.CharField(max_length=20, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='vk_url',
            field=models.URLField(max_length=128, verbose_name='VK'),
        ),
    ]
