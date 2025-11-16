import geo.utils as utils  

a, b = 3, 4 
c = utils.pythagoras(a, b)  
print(f'a={a}, b={b} 일 때 빗변 c = {c}') 

r = 10
area = utils.circle(r)
print(f'반지름 r={r} 일 때 원의 넓이 = {area}')
