# Generated by Django 3.2.3 on 2021-09-03 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Unit Price')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='book')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carts', related_query_name='mycustomer', to=settings.AUTH_USER_MODEL, verbose_name='Cart')),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_books', models.IntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('books', models.ManyToManyField(related_name='book_carts', to='carts.BooksInCart')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart', verbose_name='Cart')),
            ],
        ),
        migrations.AddField(
            model_name='booksincart',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='carts.cart', verbose_name='Cart'),
        ),
    ]
