def build_url(args):
    URL = 'https://www.airbnb.com/s/homes?'

    # Add pagination
    if 'search_type' in args and args['search_type']:
        URL = URL + 'search_type=' + args['search_type']
        if  args['search_type'] == 'pagination' and 'page' in args and args['page']:
            items_offset = str(int(args['page']) * 20)
            URL = URL + '&items_offset=' + items_offset

    # Add location, these are required fields
    if 'city' in args and args['city'] and 'state' in args and args['state']:
        URL = URL + '&query=' + args['city'] + '%2C%20' + args['state']

    # Add logistics
    if 'checkin' in args and args['checkin'] and 'checkout' in args and args['checkout']:
        URL = URL + '&checkin=' + args['checkin'] + '&checkout=' + args['checkout']

    # Add adults, there is default='1' but check just for safety
    if 'adults' in args and args['adults']:
        URL = URL + '&adults=' + args['adults']

    # Add min_price
    if 'min_price' in args and args['min_price']:
        URL = URL + '&min_price=' + args['min_price']

    # Add max_price
    if 'max_price' in args and args['max_price']:
        URL = URL + '&max_price=' + args['max_price']

    # Add min_bedrooms
    if 'min_beds' in args and args['min_beds']:
        URL = URL + '&min_beds=' + args['min_beds']

    # Add min_bedrooms
    if 'min_bedrooms' in args and args['min_bedrooms']:
        URL = URL + '&min_bedrooms=' + args['min_bedrooms']

    # Add min_bathrooms
    if 'min_bathrooms' in args and args['min_bathrooms']:
        URL = URL + '&min_bathrooms=' + args['min_bathrooms']

    # Add flexible_cancellation
    if 'flexible_cancellation' in args and args['flexible_cancellation']:
        URL = URL + '&flexible_cancellation=' + args['flexible_cancellation']

    # Add instant booking
    if 'instant_booking' in args and args['instant_booking']:
        URL = URL + '&ib=' + args['instant_booking']

    # Add work trip
    if 'work_trip' in args and args['work_trip']:
        URL = URL + '&work_trip=' + args['work_trip']

    # Add superhost
    if 'superhost' in args and args['superhost']:
        URL = URL + '&superhost=' + args['superhost']

    # Add property types
    if 'property_types' in args and args['property_types']:
        property_types = args['property_types'].split(',')
        for property_type_id in property_types:
            URL = URL + '&property_type_id%5B%5D=' + property_type_id

    # Add neighborhoods
    if 'neighborhoods' in args and args['neighborhoods']:
        neighborhoods = args['neighborhoods'].split(',')
        for neighborhood_id in neighborhoods:
            URL = URL + '&neighborhood_ids%5B%5D=' + neighborhood_id

    # Add languages
    if 'languages' in args and args['languages']:
        languages = args['languages'].split(',')
        for language_id in languages:
            URL = URL + '&languages%5B%5D=' + language_id

    # For debugging let's see the URL
    print(URL, flush=True)
    return URL
