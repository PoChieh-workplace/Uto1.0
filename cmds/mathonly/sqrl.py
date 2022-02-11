import math

def log(inf):
    inf = inf.replace('(','')
    inf = inf.replace(')','')
    if(not inf.find(',')==-1):
        try:
            get = inf.find(',')
            ab = float(inf[:get])
            ac = float(inf[get+1:])
            return math.log(ac,ab)
        except:
            return "對數給予資料錯誤"
    else:
        print(inf)
        return math.log10(float(inf))

def fabs(a):
    return math.fabs(float(a))

def sqr(a):
    if(a<0):
        return "無法計算虛數"
    else:
        return math.sqrt(float(a))