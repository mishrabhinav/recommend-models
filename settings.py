from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern


class Settings(MongoModel):
    username = fields.CharField(primary_key=True, required=True)
    last_modified = fields.DateTimeField(required=True)

    show_walk = fields.BooleanField(required=False, default=True)
    limit_walk = fields.ListField(fields.IntegerField)

    show_car = fields.BooleanField(required=False, default=True)
    limit_car = fields.ListField(fields.IntegerField)

    show_bike = fields.BooleanField(required=False, default=True)
    limit_bike = fields.ListField(fields.IntegerField)

    show_transit = fields.BooleanField(required=False, default=True)
    limit_transit = fields.ListField(fields.IntegerField)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'recommend-ahp'

