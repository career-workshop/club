# Generated by Django 3.2.13 on 2024-04-28 13:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20240428_1319'),
        ('payments', '0005_auto_20200721_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subscription_id', models.CharField(db_index=True, max_length=256)),
                ('reference', models.CharField(db_index=True, max_length=256)),
                ('product_code', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('active', 'active'), ('stopped', 'stopped')], default='active', max_length=32)),
                ('data', models.TextField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_subscriptions', to='users.user')),
            ],
            options={
                'db_table': 'subscriptions',
            },
        ),
    ]
