# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='alternativeA',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='alternativeB',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='alternativeC',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='alternativeD',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='alternativeE',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
