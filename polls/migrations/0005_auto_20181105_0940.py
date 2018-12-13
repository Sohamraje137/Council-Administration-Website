# Generated by Django 2.1.2 on 2018-11-05 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181022_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Candidate Name')),
                ('votes', models.IntegerField(default=0, verbose_name='Votes Gained')),
            ],
            options={
                'verbose_name': 'Candidates List',
                'verbose_name_plural': 'Candidates List',
            },
        ),
        migrations.CreateModel(
            name='ClassElections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_year', models.IntegerField(null=True, verbose_name='Participating Year')),
                ('student_branch', models.CharField(max_length=2, null=True, verbose_name='Branch')),
                ('student_section', models.IntegerField(null=True, verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Class Elections',
                'verbose_name_plural': 'Class Elections',
            },
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AlterUniqueTogether(
            name='classelections',
            unique_together={('student_year', 'student_branch', 'student_section')},
        ),
        migrations.AddField(
            model_name='candidate',
            name='ClassElection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ClassElections'),
        ),
    ]