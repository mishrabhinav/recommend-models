from pymodm import MongoModel, fields
from pymodm.errors import ValidationError
from pymongo.write_concern import WriteConcern

_REQUIRED_KEYS = ['distance', 'duration', 'WALKING', 'BICYCLING', 'DRIVING', 'TRANSIT']
_REQUIRED_MODE_KEYS = ['distance', 'duration', 'show']


def _dist_dur_validation(key, value):
    if not isinstance(value, list) or len(value) != 2 or not all(isinstance(e, int) and e > 0 for e in value):
        raise ValidationError('field must have {} with value list of length 2 and positive integers.'.format(key))


def _mode_validation(key, value):
    if not isinstance(value, dict) or len(value) != 3 or not all(k in value.keys() for k in _REQUIRED_MODE_KEYS):
        raise ValidationError(
            'field must have {} key with value dict of length 3 and keys {}.'.format(key, _REQUIRED_MODE_KEYS))

    dist_dur = _REQUIRED_MODE_KEYS[:2]
    for key in dist_dur:
        _dist_dur_validation(key, value[key])

    show = value[_REQUIRED_MODE_KEYS[2]]
    if not isinstance(show, bool):
        raise ValidationError('field show in {} must be a boolean'.format(key))


def validate_settings(value: dict):
    if len(value) != 6 or not all(k in value.keys() for k in _REQUIRED_KEYS):
        raise ValidationError('field must have 6 keys {}.'.format(_REQUIRED_KEYS))

    dist_dur = _REQUIRED_KEYS[:2]
    for key in dist_dur:
        _dist_dur_validation(key, value[key])

    modes = _REQUIRED_KEYS[2:]
    for key in modes:
        _mode_validation(key, value[key])


class Settings(MongoModel):
    username = fields.CharField(primary_key=True, required=True)
    last_modified = fields.DateTimeField(required=True)
    data = fields.DictField(required=True, validators=[validate_settings])

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'recommend-ahp'
