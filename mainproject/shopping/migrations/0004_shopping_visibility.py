from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_shopping_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='visibility',
            field=models.CharField(
                choices=[('public', 'Public'), ('private', 'Private')],
                default='public',
                max_length=10,
            ),
        ),
    ]
