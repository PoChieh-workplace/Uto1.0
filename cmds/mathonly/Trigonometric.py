import math

def sin(a):
    while a>=360:
        a-=360
    minus = False
    if(a>=180):
        a-=180
        minus = True
    a = math.sin(math.radians(a))
    if(minus):
        a = -a
    return a
def cos(a):
    while a>=360:
        a-=360
    minus = False
    if(a>=180):
        a-=180
        minus = True
    a = math.cos(math.radians(a))
    if(minus):
        a = -a
    return a
def tan(a):
    while a>=180:
        a-=180
    if a==90:
        return "tan極端值(錯誤)"
    a = math.tan(math.radians(a))
    return a
def sec(a):
    while a>=360:
        a-=360
    minus = False
    if(a>=180):
        a-=180
        minus = True
    a = 1/(math.cos(math.radians(a)))
    if(minus):
        a = -a
    return a
def csc(a):
    while a>=360:
        a-=360
    minus = False
    if(a>=180):
        a-=180
        minus = True
    a = 1/(math.sin(math.radians(a)))
    if(minus):
        a = -a
    return a
def cot(a):
    while a>=180:
        a-=180
    if a==0:
        return "cot極端值(錯誤)"
    a = 1/(math.tan(math.radians(a)))
    return a
