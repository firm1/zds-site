# Generated by Django 2.1.5 on 2019-01-15 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0021_auto_20190114_1301"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="alerts_on_this_comment",
                to="utils.Comment",
                verbose_name="Commentaire",
            ),
        ),
        migrations.AlterField(
            model_name="alert",
            name="content",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="alerts_on_this_content",
                to="tutorialv2.PublishableContent",
                verbose_name="Contenu",
            ),
        ),
    ]
