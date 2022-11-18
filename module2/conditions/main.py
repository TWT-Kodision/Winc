# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_date, cow_milking_status, location_of_cows, season, slurry_tank, grass_is_long):
    if location_of_cows == 'pasture' and (time_of_date == 'night' or weather == 'rainy'):
        return 'take cows to cowshed'
    elif cow_milking_status:
        if location_of_cows == 'cowshed':
            return 'milk cows'
        return"""take cows to cowshed
milk cows
take cows back to pasture"""
    elif slurry_tank and (weather != 'sunny' or weather != 'windy'):
        if location_of_cows != 'pasture':
            return 'fertilize pasture'
        return """take cows to cowshed 
fertilize pasture
take cows back to pasture"""
    elif grass_is_long and season == 'spring' and weather == 'sunny':
        if location_of_cows != 'pasture':
            return 'mow grass'
        return"""take cows to cowshed 
mow grass
take cows back to pasture"""
    return 'wait'

action =  farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
print(action)