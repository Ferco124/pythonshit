money=int(input())
def bill(num):
    global money
    no=money//num
    for i in range(no):
        print(num)
        money=money-num
if money%10==0 and money>=10 and money<=10000:
    if money>=1000:
        bill(1000)
    if money>=500:
        bill(500)
    if money>=100:
        bill(100)
    if money>=50:
        bill(50)
    if money>=20:
        bill(20)
    if money>=10:
        bill(10)