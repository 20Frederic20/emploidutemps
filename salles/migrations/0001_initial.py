# Generated by Django 3.2.16 on 2007-04-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=60)),
                ('cycle', models.CharField(choices=[('licence', 'Licence'), ('master', 'Master'), ('doctorat', 'Doctorat')], max_length=9)),
            ],
        ),
    ]
