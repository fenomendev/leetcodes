digits = [1,9,9]
digits=list(map(lambda x : str(x),digits))
son=''.join(digits)
digits=list(str(int(son)+1))
digits=list(map(lambda x : int(x),digits))
print(digits)

