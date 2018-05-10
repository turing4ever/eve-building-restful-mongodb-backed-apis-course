
MONGO_DBNAME = 'apitest'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
IF_MATCH = False

schema = {
    'firstname': {'type': 'string'},
    'lastname': {'type': 'string'},
}

DOMAIN = {
        'people':
            {
                'schema': schema
             },
        'works':
            {
                'resource_methods': ['GET'],
                'item_methods': ['GET'],
            }
}
