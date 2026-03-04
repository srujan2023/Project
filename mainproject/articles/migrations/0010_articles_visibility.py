from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_articles_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='visibility',
            field=models.CharField(
                choices=[('public', 'Public'), ('private', 'Private')],
                default='public',
                max_length=10,
            ),
        ),
    ]
