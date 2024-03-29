# Generated by Django 5.0.2 on 2024-02-29 17:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('Collection_image', models.ImageField(blank=True, null=True, upload_to='Collectionimages')),
                ('collection_title', models.CharField(max_length=70)),
                ('subtitle', models.CharField(blank=True, max_length=70, null=True)),
                ('collection_url', models.SlugField(blank=True, max_length=60, null=True)),
                ('followers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='Postimages')),
                ('title', models.CharField(max_length=70)),
                ('subtitle', models.CharField(blank=True, max_length=70, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Scheduled', 'Scheduled'), ('Publish', 'Publish')], default='Savings', max_length=10)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('last_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_viewed', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Posts_collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.collections')),
                ('post_id', models.ManyToManyField(to='home.posts')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='home.users'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
        migrations.AddField(
            model_name='collections',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users'),
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ManyToManyField(to='home.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
        migrations.CreateModel(
            name='Users_collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.ManyToManyField(to='home.collections')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
        migrations.CreateModel(
            name='Users_followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.ManyToManyField(to='home.users')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to='home.users')),
            ],
        ),
        migrations.CreateModel(
            name='Users_following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.ManyToManyField(to='home.users')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='home.users')),
            ],
        ),
    ]
