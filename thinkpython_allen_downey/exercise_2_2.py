width = 17
height = 12.0
delimiter = '.'

l_format = '{:<6} -> '
print(l_format.format(width/2), type(width/2))
print(l_format.format(width/2.0), type(width/2.0))
print(l_format.format(height/3), type(height/3))
print(l_format.format(1 + 2 * 5), type(1 + 2 * 5))
print(l_format.format(delimiter * 5), type(delimiter * 5))
