money=float(input("money:"))

a=int(money//1000)
money=money-1000*a

b=int(money//500)
money=money-500*b

c=int(money//100)
money=money-100*c

d=int(money//50)
money=money-50*d

e=int(money//20)
money=money-20*e

f=int(money//10)
money=money-10*f

g=int(money//5)
money=money-5*g

h=int(money//2)
money=money-2*h

i=int(money//1)
money=money-1*i

j=int(money//0.5)
money=money-0.5*j

k=int(money//0.2)
money=money-0.2*k

l=int(money//0.1)
money=money-0.1*l

print('$1000 bill:', a)
print('$500 bill:', b)
print('$100 bill:', c)
print('$50:', d)
print('$20:', e)
print('$10:', f)
print('$5:', g)
print('$2:', h)
print('$1:', i)
print('$0.5:', j)
print('$0.2:', k)
print('$0.1:', l)
