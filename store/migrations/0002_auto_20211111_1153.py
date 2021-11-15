# Generated by Django 3.2.9 on 2021-11-11 11:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_session_id',
            field=models.CharField(default='GGG', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.customer'),
        ),
    ]
