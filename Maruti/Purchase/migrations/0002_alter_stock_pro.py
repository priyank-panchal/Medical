# Generated by Django 3.2.5 on 2021-07-25 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
        ('Purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.products'),
        ),
    ]
