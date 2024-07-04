# 1st program
print(9**0.5*5)
# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)
# 3rd program
a = 1234# первое число
middle1 = a % 1000 // 10# серединная часть четырехзначного числа
b = 5678# второе число
middle2 = b % 1000 // 10# серединная часть четырехзначного числа
print(middle1 + middle2)
# 4th program
whole1 = int(13.42)# целая часть первого числа
fract1 = int(13.42*100) - int(whole1*100)# дробная часть первого числа
whole2 = int(42.13)# целая часть второго числа
fract2 = int(42.13*100) - int(whole2*100)# дробная часть второго числа
print(whole1==fract2 or whole2==fract1)



