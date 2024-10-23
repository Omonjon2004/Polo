# Generated by Django 5.1.1 on 2024-10-23 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('rating', models.DecimalField(blank=True, choices=[(0.0, '0'), (1.0, '1 Star'), (2.0, '2 Stars'), (3.0, '3 Stars'), (4.0, '4 Stars'), (5.0, '5 Stars')], decimal_places=1, max_digits=2, null=True)),
                ('by_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('Autumn', 'Autumn')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='bags_images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bags', to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bags', to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bags', to='product.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('rating', models.DecimalField(blank=True, choices=[(0.0, '0'), (1.0, '1 Star'), (2.0, '2 Stars'), (3.0, '3 Stars'), (4.0, '4 Stars'), (5.0, '5 Stars')], decimal_places=1, max_digits=2, null=True)),
                ('by_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('Autumn', 'Autumn')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('4XL', '4XL'), ('5XL', '5XL')], max_length=5)),
                ('image', models.ImageField(upload_to='dress_images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dress', to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dress', to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dress', to='product.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Electrical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('rating', models.DecimalField(blank=True, choices=[(0.0, '0'), (1.0, '1 Star'), (2.0, '2 Stars'), (3.0, '3 Stars'), (4.0, '4 Stars'), (5.0, '5 Stars')], decimal_places=1, max_digits=2, null=True)),
                ('by_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('Autumn', 'Autumn')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='electrical_images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electrical', to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electrical', to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electrical', to='product.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jackets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('rating', models.DecimalField(blank=True, choices=[(0.0, '0'), (1.0, '1 Star'), (2.0, '2 Stars'), (3.0, '3 Stars'), (4.0, '4 Stars'), (5.0, '5 Stars')], decimal_places=1, max_digits=2, null=True)),
                ('by_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('Autumn', 'Autumn')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='jackets_images/')),
                ('size', models.CharField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('4XL', '4XL'), ('5XL', '5XL')], max_length=5)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jackets', to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jackets', to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jackets', to='product.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('rating', models.DecimalField(blank=True, choices=[(0.0, '0'), (1.0, '1 Star'), (2.0, '2 Stars'), (3.0, '3 Stars'), (4.0, '4 Stars'), (5.0, '5 Stars')], decimal_places=1, max_digits=2, null=True)),
                ('by_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('Autumn', 'Autumn')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='jewelry_images/')),
                ('size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('composition', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry', to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry', to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jewelry', to='product.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20)),
                ('rating', models.DecimalField(blank=True, choices=[(0.0, '0'), (1.0, '1 Star'), (2.0, '2 Stars'), (3.0, '3 Stars'), (4.0, '4 Stars'), (5.0, '5 Stars')], decimal_places=1, max_digits=2, null=True)),
                ('by_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter'), ('spring', 'Spring'), ('Autumn', 'Autumn')], max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField(choices=[(20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50)])),
                ('image', models.ImageField(upload_to='shoes_images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='product.color')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]