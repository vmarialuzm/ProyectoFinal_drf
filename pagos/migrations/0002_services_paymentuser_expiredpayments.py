# Generated by Django 4.2.3 on 2023-07-24 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('N', 'Netflix'), ('A', 'Amazon Video'), ('S', 'Star +'), ('P', 'Paramount +')], max_length=1)),
                ('description', models.TextField()),
                ('logo', models.URLField()),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='PaymentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(auto_now_add=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.services')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment_user',
            },
        ),
        migrations.CreateModel(
            name='ExpiredPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.FloatField()),
                ('payment_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.paymentuser')),
            ],
            options={
                'db_table': 'expired_payments',
            },
        ),
    ]
