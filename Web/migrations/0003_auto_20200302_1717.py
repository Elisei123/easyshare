# Generated by Django 3.0.3 on 2020-03-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0002_auto_20200302_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='discord',
            field=models.CharField(default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='facebook',
            field=models.CharField(default='https://www.facebook.com/', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='github',
            field=models.CharField(default='https://github.com/', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='gmail',
            field=models.CharField(default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='instagram',
            field=models.CharField(default='https://www.instagram.com/', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='linkedin',
            field=models.CharField(default='https://www.linkedin.com/in/', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='paypal',
            field=models.CharField(default='https://www.paypal.me/', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='skype',
            field=models.CharField(default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='steam',
            field=models.CharField(default='https://steamcommunity.com/profiles/', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='retele_de_socializare_utilizator',
            name='youtube',
            field=models.CharField(default='https://www.youtube.com/channel/', max_length=60, null=True),
        ),
    ]
