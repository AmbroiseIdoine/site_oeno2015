# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(default=b'AC', max_length=2, choices=[(b'AC', b'Actualit\xc3\xa9s'), (b'PA', b'partenaires')])),
                ('titre', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'img')),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de parution')),
            ],
        ),
    ]
