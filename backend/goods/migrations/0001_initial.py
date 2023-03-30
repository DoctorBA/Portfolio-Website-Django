# Generated by Django 4.1.5 on 2023-03-30 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a description of the soap', max_length=100)),
                ('link', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='image-placeholder.png', upload_to='soap/')),
                ('aroma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aromas_soap', to='catalog.aroma')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturers_soap', to='catalog.manufacturer')),
                ('volume', models.ManyToManyField(blank=True, related_name='volume_soap', to='catalog.volume')),
            ],
        ),
        migrations.CreateModel(
            name='Cream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a description of the soap', max_length=100)),
                ('link', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='image-placeholder.png', upload_to='cream/')),
                ('aroma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aromas_cream', to='catalog.aroma')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturers_cream', to='catalog.manufacturer')),
                ('volume', models.ManyToManyField(blank=True, related_name='volume_cream', to='catalog.volume')),
            ],
        ),
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('summary', models.TextField(blank=True, help_text='Enter a description of the candle', max_length=100)),
                ('link', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='image-placeholder.png', upload_to='candle/')),
                ('aroma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aromas_candle', to='catalog.aroma')),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturers_candle', to='catalog.manufacturer')),
                ('volume', models.ManyToManyField(blank=True, related_name='volume_candles', to='catalog.volume')),
            ],
        ),
    ]
