# Generated by Django 3.1.7 on 2021-07-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_auto_20210702_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fechaRegistro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]