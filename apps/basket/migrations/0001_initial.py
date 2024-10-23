# Generated by Django 5.1.1 on 2024-10-23 02:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('bag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.bags')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='basket.basket')),
                ('dress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.dress')),
                ('jewelry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.jewelry')),
                ('shoes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.shoes')),
            ],
        ),
    ]
