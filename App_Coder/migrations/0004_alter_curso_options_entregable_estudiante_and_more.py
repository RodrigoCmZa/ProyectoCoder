# Generated by Django 4.0.6 on 2022-07-28 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Coder', '0003_entregable_profesor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ('nombre', '-camada'), 'verbose_name': 'Course', 'verbose_name_plural': 'My Courses'},
        ),
        migrations.AddField(
            model_name='entregable',
            name='estudiante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App_Coder.estudiante'),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together={('nombre', 'camada')},
        ),
    ]
