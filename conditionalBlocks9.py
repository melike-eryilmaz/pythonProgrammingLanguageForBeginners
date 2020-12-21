# 21/12/2020 Conditional Blocks

lights = ['red','yellow','green']

# currentLight = lights[0]
# currentLight = lights[1]
currentLight = lights[2]
print(currentLight)

if currentLight == 'red':
    print('STOP!')

elif  currentLight == 'yellow':
    print('READY!')
    
else:
    print('GO!')
