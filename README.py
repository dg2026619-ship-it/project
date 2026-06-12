Web VPython 3.2

b = box()
while True :        
    rate(100)
    k = keysdown()
    if 'c' in k:    
        b.color = color.red
    else:   
        b.color = color.white
