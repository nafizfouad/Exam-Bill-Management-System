# Generated by Django 4.1.2 on 2022-10-15 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semesterbill',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.semester'),
        ),
    ]