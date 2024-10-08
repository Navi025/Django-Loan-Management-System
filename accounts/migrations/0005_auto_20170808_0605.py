
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170808_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='loan_officer',
        ),
        migrations.RemoveField(
            model_name='client',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='person',
            name='basemodel_ptr',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.DeleteModel(
            name='person',
        ),
    ]
