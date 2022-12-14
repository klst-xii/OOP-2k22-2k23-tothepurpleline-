# Generated by Django 4.1.1 on 2022-09-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=10.0, max_digits=20)),
                ('image', models.FileField(blank=True, null=True, upload_to='products/')),
            ],
        ),
    ]
