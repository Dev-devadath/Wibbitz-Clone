# Generated by Django 5.0 on 2023-12-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_videoblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Testimonials/')),
                ('logo', models.FileField(blank=True, null=True, upload_to='Testimonials/')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField()),
            ],
        ),
    ]
