#problema de los astronautas y el agua
def water_left(astronauts, water_left, days_left):

    #Aqui se agrego lo de la validacion del tipo de dato
    for argument in [astronauts, water_left, days_left]:
        try:
            #Se intenta hacer una division si no se puede hacer genera un error de tipo
            argument / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben ser númericos, pero se ha recibido {argument}")

    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    
    #Se agrego este bloque para enviar un error personalizado con una excepcion
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    print(water_left(5,100,"A"))
except RuntimeError as err:
    print(err)