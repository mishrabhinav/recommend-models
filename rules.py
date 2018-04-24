from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern


class Rules(MongoModel):
    user = fields.CharField(required=True)
    rules = fields.BinaryField(required=True)
    created_on = fields.DateTimeField(required=True)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'recommend-ahp'
