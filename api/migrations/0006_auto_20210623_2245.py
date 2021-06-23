# Generated by Django 3.2.4 on 2021-06-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210623_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='publishedAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blog'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageData',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageType',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
