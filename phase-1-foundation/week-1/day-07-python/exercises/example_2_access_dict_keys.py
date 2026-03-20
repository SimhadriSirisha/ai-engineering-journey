alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0['points'] -> this will create error

point_value = alien_0.get('points', "No key with name point")
print(point_value)