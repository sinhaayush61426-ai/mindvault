from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("vault", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="diaryentry",
            name="title",
            field=models.CharField(default="New Reflection", max_length=100),
        ),
        migrations.AddField(
            model_name="diaryentry",
            name="category",
            field=models.CharField(default="General", max_length=50),
        ),
        migrations.AddField(
            model_name="diaryentry",
            name="release_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="diaryentry",
            name="is_time_locked",
            field=models.BooleanField(default=False),
        ),
    ]
