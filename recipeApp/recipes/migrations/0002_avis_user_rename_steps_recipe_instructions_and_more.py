# Generated by Django 4.2.16 on 2024-11-18 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("rating", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name="recipe", old_name="steps", new_name="instructions",
        ),
        migrations.RemoveField(model_name="recipe", name="author",),
        migrations.RemoveField(model_name="recipe", name="created_at",),
        migrations.AlterField(
            model_name="ingredient", name="description", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="recipe", name="description", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(to="recipes.ingredient"),
        ),
        migrations.DeleteModel(name="Review",),
        migrations.AddField(
            model_name="avis",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="recipes.recipe"
            ),
        ),
        migrations.AddField(
            model_name="avis",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="recipes.user"
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="recipes.user",
            ),
        ),
    ]