# Generated by Django 2.2.13 on 2020-12-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0029_auto_20201206_1541'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['tag_name', 'club'], name='workshop_ta_tag_nam_238116_idx'),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['tag_name', 'entity'], name='workshop_ta_tag_nam_2f9375_idx'),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['club'], name='workshop_ta_club_id_aaa1a2_idx'),
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['entity'], name='workshop_ta_entity__b1a461_idx'),
        ),
    ]
