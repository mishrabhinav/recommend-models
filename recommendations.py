from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern

from .directions import Directions
from .forecast import Forecast


class Recommendations(MongoModel):
    user = fields.CharField(required=True)
    created_on = fields.DateTimeField(required=True)
    selected = fields.ReferenceField(Directions, blank=True)
    available = fields.ListField(fields.ReferenceField(Directions))
    forecast = fields.ListField(fields.ReferenceField(Forecast))
    method = fields.CharField(blank=True)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'recommend-ahp'
