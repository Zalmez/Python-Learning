#Notater
#forkorter position til pos, kortere og lett å forstå

alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium', 'points': 5}
print("original x_pos: " + str(alien_0['x_pos']))

#Move the alien to the right
# Determine how far to move the alien based on it's speed
if (alien_0['speed'] == 'slow'):
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# Updated position: xpos + x_increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print("New x_pos: " + str(alien_0['x_pos']))

print(alien_0)
#Det går ann å slette verdier fra et dictonary
del alien_0['points']
print(alien_0)
