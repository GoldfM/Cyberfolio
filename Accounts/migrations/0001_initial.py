# Generated by Django 4.1.7 on 2023-04-25 17:26

import Accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Специализация проекта')),
            ],
            options={
                'verbose_name': 'Специализация проекта',
                'verbose_name_plural': 'Специализации проектов',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, verbose_name='Тип проекта')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sur_sur_name', models.CharField(blank=True, max_length=20, verbose_name='Фамилия')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('descriptions', models.TextField(blank=True, max_length=300, verbose_name='Описание')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('photo', models.ImageField(blank=True, upload_to=Accounts.models.user_directory_path, verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('vk_url', models.URLField(blank=True, max_length=128, verbose_name='VK')),
                ('hh_url', models.URLField(blank=True, max_length=128, verbose_name='HH')),
                ('behance_url', models.URLField(blank=True, max_length=128, verbose_name='BH')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('spec', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='Accounts.specs', verbose_name='Специализация')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Юзер',
                'verbose_name_plural': 'Юзеры',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('sum_registred', models.IntegerField(default=0, verbose_name='Сумма оценок зареганных')),
                ('count_registred', models.IntegerField(default=0, verbose_name='Колисчество оценок зареганных')),
                ('sum_unregistred', models.IntegerField(default=0, verbose_name='Сумма оценок незареганных')),
                ('count_unregistred', models.IntegerField(default=0, verbose_name='Количество оценок незареганных')),
                ('descriptions', models.TextField(max_length=300, verbose_name='Описание')),
                ('key_words', models.TextField(max_length=100, verbose_name='Ключевые слова')),
                ('url', models.URLField(blank=True, max_length=128, verbose_name='URL')),
                ('time_developing', models.CharField(max_length=30, verbose_name='Время разработки')),
                ('teammate1', models.URLField(blank=True, max_length=128, verbose_name='Тиммейт1')),
                ('teammate2', models.URLField(blank=True, max_length=128, verbose_name='Тиммейт2')),
                ('teammate3', models.URLField(blank=True, max_length=128, verbose_name='Тиммейт3')),
                ('teammate4', models.URLField(blank=True, max_length=128, verbose_name='Тиммейт4')),
                ('teammate5', models.URLField(blank=True, max_length=128, verbose_name='Тиммейт5')),
                ('avatar_image', models.ImageField(blank=True, upload_to=Accounts.models.user_directory_path, verbose_name='Аватар')),
                ('main_image', models.ImageField(blank=True, upload_to=Accounts.models.user_directory_path, verbose_name='Основное фото')),
                ('spec_proj', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Accounts.specproject', verbose_name='Специализация')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Accounts.typeproject', verbose_name='Тип преокта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=Accounts.models.image_directory_path)),
                ('proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.project', verbose_name='Фото проекта')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Кто подписался')),
                ('follow_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='На кого подписался')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ['id'],
            },
        ),
    ]
