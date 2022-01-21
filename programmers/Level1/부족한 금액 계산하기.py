def solution(input_price, money, count):
    for i in range(1,count+1):
        price=input_price*i
        money=money-price
    if money<0:
        money=abs(money)
    else:
        money=0
    return money