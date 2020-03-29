def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
