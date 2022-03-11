from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='liked',
            field=models.CharField(max_length=255, null=True),
        ),
    ]