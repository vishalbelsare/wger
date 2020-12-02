# Generated by Django 3.1.3 on 2020-12-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20190618_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Variation')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='variation',
            field=models.ManyToManyField(blank=True, to='exercises.ExerciseVariation', verbose_name='Variation'),
        ),
    ]