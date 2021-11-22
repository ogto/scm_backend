import decimal
import json
import datetime

from sqlalchemy import types
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, decimal.Decimal):
                        fields[field] = float(data)
                    elif isinstance(data, datetime.datetime):
                        fields[field] = data.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        json.dumps(data) # this will fail on non-encodable values, like other classes
                        fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
