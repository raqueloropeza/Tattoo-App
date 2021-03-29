# Generated by Django 2.2.4 on 2021-03-05 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('profile_pic', models.ImageField(null=True, upload_to='images/')),
                ('website', models.CharField(max_length=200, null=True)),
                ('bio', models.TextField(null=True)),
                ('books_open', models.BooleanField()),
                ('walk_ins', models.BooleanField()),
                ('is_apprentice', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('birth_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='tattoo_app.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Studios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_name', models.CharField(max_length=255)),
                ('profile_pic', models.ImageField(null=True, upload_to='images/')),
                ('website', models.CharField(max_length=200, null=True)),
                ('bio', models.TextField(null=True)),
                ('walk_ins', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artists_at_studio', models.ManyToManyField(related_name='studios_joined', to='tattoo_app.Profile')),
                ('followers', models.ManyToManyField(related_name='favorite_studios', to='tattoo_app.Users')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio_location', to='tattoo_app.Locations')),
                ('styles', models.ManyToManyField(related_name='studio_with_styles', to='tattoo_app.Styles')),
            ],
        ),
        migrations.CreateModel(
            name='StudioPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio_post', to='tattoo_app.Studios')),
            ],
        ),
        migrations.CreateModel(
            name='StudioComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio_comments', to='tattoo_app.StudioPosts')),
                ('user_comment', models.ManyToManyField(related_name='studio_comment_by_user', to='tattoo_app.Users')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_post', to='tattoo_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_comments', to='tattoo_app.ProfilePosts')),
                ('user_comment', models.ManyToManyField(related_name='profile_comment_by_user', to='tattoo_app.Users')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='favorite_artists', to='tattoo_app.Users'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_location', to='tattoo_app.Locations'),
        ),
        migrations.AddField(
            model_name='profile',
            name='styles',
            field=models.ManyToManyField(related_name='artists_with_styles', to='tattoo_app.Styles'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='tattoo_app.Users'),
        ),
    ]