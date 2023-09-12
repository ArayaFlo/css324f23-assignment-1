def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0]==4 and s[1]==4

def successors(s):
    x, y, z = s
    #EMPTY
    if x > 0:
        yield ((0,y,z),x)
    if y > 0:
        yield ((x,0,z),y)
    if z > 0:
        yield ((x,y,0),z)

    #FILL
    if x < 8:
        yield ((8,y,z),8-x)
    if y < 5:
        yield ((x,5,z),5-y)
    if z < 3:
        yield ((x,y,3),3-z)
    
    #POUR
    #FROM 8 TO 5
    t=5-y
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t,5,z),t)
        else:
            yield ((0,y+x,z),x)
    
    #FROM 8 TO 3
    t=3-z
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t,y,3),t)
        else:
            yield ((0,y,z+x),x)
    
    #FROM 5 TO 8
    t=8-x
    if y > 0 and t > 0:
        if y > t:
            yield ((8,y-t,z),t)
        else:
            yield ((x+y,0,z),y)

    #FROM 5 TO 3
    t=3-z
    if y > 0 and t > 0:
        if y > t:
            yield ((x,y-t,3),t)
        else:
            yield ((x,0,z+y),y)

    #FROM 3 TO 8
    t=8-x
    if z > 0 and t > 0:
        if z > t:
            yield ((8,y-t,z),t)
        else:
            yield ((x+z,y,0),z)

    #FROM 3 TO 5
    t=5-y
    if z > 0 and t > 0:
        if z > t:
            yield ((x,5,z-t),t)
        else:
            yield ((x,y+z,0),z)
