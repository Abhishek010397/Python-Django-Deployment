from django.db import models

# Create your models here.
types_options = ['refuse', 'paper', 'mgp']
borough_options = ['Brooklyn', 'Manhattan', 'Bronx', 'Queens', 'Statenisland']
community_district = ['01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18']


class CollectionDetails(models.Model):
    types = models.CharField(max_length=20,
                             choices=((i, i) for i in types_options))
    borough = models.CharField(max_length=20,
                               choices=((i, i) for i in borough_options))
    community_district = models.CharField(max_length=20,
                                          choices=((i, i) for i in community_district))
    values = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.types

    class Meta:
        db_table = 'collection_details'
