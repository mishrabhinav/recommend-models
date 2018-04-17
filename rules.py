from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern

from .user import User


class Rules(MongoModel):
    user = fields.ReferenceField(User, required=True)
    rules = fields.BinaryField(required=True)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'recommend-ahp'
