def func(son):
    result=0
    while son>0:
        result+=(son%10)**2
        son=son//10
    return result

def aylanish(result):       
    if result==1:
        return True
    if result<7:   
        return False
    return aylanish(func(result))

print(aylanish(8))


