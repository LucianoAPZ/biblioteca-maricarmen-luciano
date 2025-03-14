# Generated by Django 4.2.18 on 2025-03-05 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_usuari_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='br',
            name='cataleg_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.categoria'),
        ),
        migrations.AlterField(
            model_name='cd',
            name='cataleg_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='dispositiu',
            name='cataleg_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='cataleg_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='exemplar',
            name='cataleg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='imatge',
            name='cataleg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='llibre',
            name='cataleg_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='llibre',
            name='llengua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.llengua'),
        ),
        migrations.AlterField(
            model_name='llibre',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.pais'),
        ),
        migrations.AlterField(
            model_name='prestec',
            name='exemplar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.exemplar'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='exemplar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.exemplar'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='cataleg_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.cataleg'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='llengua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.llengua'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.pais'),
        ),
        migrations.AlterField(
            model_name='usuari',
            name='centre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.centre'),
        ),
    ]
