# Generated by Django 3.2.8 on 2021-10-27 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_treatment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='category',
            field=models.IntegerField(choices=[(1, 'Facial and Skin Treatments'), (2, 'Massage'), (3, 'Laser Treatments'), (4, 'Hand and Foot Treatments'), (5, 'Hair Services')], default=1),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('specialist', models.CharField(choices=[('Skin Care Specialist', (('sk1', 'Skin1'), ('sk2', 'Skin2'))), ('Registered Massage Therapist', (('rmt1', 'Reg.M.T.1'), ('rmt1', 'Reg.M.T.2'))), ('Laser Technitian', (('lsr1', 'Laser 1'), ('lsr2', 'Laser 2'))), ('Non-Registered Massage provider', (('Non-RMT1', 'Non-1'), ('Non-RMT2', 'Non-2'))), ('Hair Styles', (('HS-1', 'Hair Artist -1'), ('HS-2', 'Hair Artist -2'))), ('any', 'any')], max_length=50)),
                ('client', models.CharField(default='Client Name', max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'Scheduled'), (2, 'Performed'), (3, 'Cancelled')], default=1)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.treatment')),
            ],
        ),
    ]
