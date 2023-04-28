def over_age(data, getter):
    return getter(data) >= 18
 
user = { 'username': 'rolf123', 'age': '35' }
 
print(over_age(user, lambda x: int(x['age'])))

def operacao(f, *a):
    return f(*a)

def soma(*a):
    total = 0
    for i in a:
        total += i
    return total

def multiplica(*a):
    total = 1
    for i in a:
        total *= i
    return total
        

print(operacao(soma, 1,2,3,4)) # 10

print(operacao(multiplica, 1,2,3,4)) # 24

funcao = lambda g: int(g)**3 #3^3 = 27

#print(operacao(funcao, 3))
print( operacao( lambda g: g**3, 3))
