from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_articles_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-id']},
        ),
    ]
