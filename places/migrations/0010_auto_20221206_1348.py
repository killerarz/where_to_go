# Generated by Django 3.2.16 on 2022-12-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0009_auto_20221206_1307"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={"verbose_name": "Фотография", "verbose_name_plural": "Фотографии"},
        ),
        migrations.RemoveField(
            model_name="image",
            name="image",
        ),
        migrations.AddField(
            model_name="image",
            name="place_image",
            field=models.ImageField(
                blank=True, upload_to="places", verbose_name="Картинка"
            ),
        ),
    ]
