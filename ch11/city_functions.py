def city_country(city, country, population=0):
    """Generate a neatly formatted location string."""
    if population:
        return f'{city}, {country}'.title() + f' ‒ population {population}'
    else:
        return f'{city}, {country}'.title()
