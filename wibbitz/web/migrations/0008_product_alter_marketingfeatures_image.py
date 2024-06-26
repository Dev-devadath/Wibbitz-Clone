# Generated by Django 5.0 on 2023-12-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_marketingfeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='products/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='products/')),
            ],
        ),
        migrations.AlterField(
            model_name='marketingfeatures',
            name='image',
            field=models.FileField(upload_to='features/'),
        ),
    ]
