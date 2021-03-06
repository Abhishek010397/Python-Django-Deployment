# Generated by Django 3.1.1 on 2020-09-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('refuse', 'refuse'), ('paper', 'paper'), ('mgp', 'mgp')], max_length=20)),
                ('borough', models.CharField(choices=[('Brooklyn', 'Brooklyn'), ('Manhattan', 'Manhattan'), ('Bronx', 'Bronx'), ('Queens', 'Queens'), ('Statenisland', 'Statenisland')], max_length=20)),
                ('community_district', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18')], max_length=20)),
            ],
        ),
    ]
