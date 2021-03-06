# Generated by Django 4.0.4 on 2022-05-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20220429_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('registration_num', models.IntegerField(db_column='Registration_num', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'airplane',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coorporation',
            fields=[
                ('co_name', models.CharField(db_column='Co_name', max_length=20, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=50, null=True)),
                ('phone_num', models.IntegerField(blank=True, db_column='Phone_num', null=True)),
            ],
            options={
                'db_table': 'coorporation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hangar',
            fields=[
                ('hangar_num', models.IntegerField(db_column='Hangar_num', primary_key=True, serialize=False)),
                ('capacity', models.IntegerField(blank=True, db_column='Capacity', null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=30, null=True)),
            ],
            options={
                'db_table': 'hangar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(blank=True, db_column='Owner_name', max_length=20, null=True)),
            ],
            options={
                'db_table': 'owner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('ssn', models.IntegerField(db_column='SSN', primary_key=True, serialize=False)),
                ('person_name', models.CharField(blank=True, db_column='Person_name', max_length=20, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, db_column='Phone', null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaneType',
            fields=[
                ('model', models.IntegerField(db_column='Model', primary_key=True, serialize=False)),
                ('capacity', models.IntegerField(blank=True, db_column='Capacity', null=True)),
                ('weight', models.IntegerField(blank=True, db_column='Weight', null=True)),
            ],
            options={
                'db_table': 'plane_type',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Adha',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='Plots',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('essn', models.OneToOneField(db_column='ESSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='travello.person')),
                ('shift_num', models.IntegerField(db_column='Shift_num')),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Owns',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='travello.owner')),
            ],
            options={
                'db_table': 'owns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('pssn', models.OneToOneField(db_column='PSSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='travello.person')),
                ('lic_num', models.IntegerField(db_column='Lic_num')),
            ],
            options={
                'db_table': 'pilot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('registration_num', models.OneToOneField(db_column='Registration_num', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='travello.airplane')),
                ('service_date', models.DateField(blank=True, db_column='Service_date', null=True)),
                ('service_time', models.TimeField(blank=True, db_column='Service_time', null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flies',
            fields=[
                ('pssn', models.OneToOneField(db_column='PSSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='travello.pilot')),
            ],
            options={
                'db_table': 'flies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorksOn',
            fields=[
                ('essn', models.OneToOneField(db_column='ESSN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='travello.employee')),
            ],
            options={
                'db_table': 'works_on',
                'managed': False,
            },
        ),
    ]
