# Generated by Django 4.0.4 on 2022-04-28 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='news.creator'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
    ]
