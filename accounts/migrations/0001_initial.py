
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0025_auto_20170730_0208'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.baseModel')),
                ('title', models.CharField(blank=True, choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=200)),
                ('fullname', models.CharField(blank=True, max_length=200)),
                ('full_address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('zip', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
                ('state_of_origin', models.CharField(blank=True, max_length=200)),
                ('current_salary', models.CharField(blank=True, max_length=200)),
                ('employment_date', models.DateField(blank=True, null=True)),
                ('lga', models.CharField(blank=True, max_length=200)),
                ('job_description', models.TextField(blank=True)),
                ('marital_status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married')], max_length=200)),
                ('picture', models.ImageField(blank=True, max_length=200, upload_to='employee/')),
                ('bio', models.TextField(blank=True, max_length=200)),
            ],
            bases=('dashboard.basemodel',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.person')),
                ('current_employer', models.CharField(blank=True, max_length=200)),
                ('years_in_workplace', models.TextField(blank=True, max_length=100)),
                ('vehicles_owned', models.CharField(blank=True, max_length=200)),
                ('years_at_residence', models.CharField(blank=True, max_length=200)),
                ('residential_status', models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Renting', 'Renting'), ('Staying with Parent', 'Staying with Parent')], max_length=200)),
                ('educational_status', models.CharField(blank=True, choices=[('Graduate', 'Graduate'), ('High School', 'High School'), ('Phd', 'Phd'), ('Masters', 'Masters')], max_length=200)),
                ('loan_officer', models.ForeignKey(blank=True, help_text='Someone who manages the client among your staffs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('accounts.person',),
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.person')),
                ('years_in_workplace', models.TextField(blank=True, max_length=100)),
                ('educational_status', models.CharField(blank=True, choices=[('Graduate', 'Graduate'), ('High School', 'High School'), ('Phd', 'Phd'), ('Masters', 'Masters')], max_length=200)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('accounts.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
    ]
