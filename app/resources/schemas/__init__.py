from flask_restful_swagger_2 import Schema

class Entity(Schema):
    type = 'object'
    properties = {
        'term': {
            'type': 'string'
        },
        'entity': {
            'type': 'string',
            'enum': [
                'author',
                'booktitle',
                'date',
                'editor',
                'institution',
                'journal',
                'location',
                'note',
                'pages',
                'publisher',
                'tech',
                'title',
                'volume'
            ]
        }
    }

class ParseResponse(Schema):
    type = 'object'
    properties = {
        'reference_string': {
            'type': 'string'
        },
        'data': Entity.array()
    }

class ParseBatchResponse(Schema):
    type = 'object'
    properties = {
        'reference_strings': {
            'type': 'array'
        },
        'data': {
            'type': 'array',
            'items': Entity.array()
        }
    }
