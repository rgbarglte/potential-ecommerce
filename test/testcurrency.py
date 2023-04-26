from moneyed import Money, USD , EUR , ARS , UYU ,  RUB

amount = 12321
usd = Money(amount, USD)
eur =Money(amount, EUR)
uyu = Money(amount, UYU)
ars = Money(amount, ARS) 

rub  = Money(amount,RUB)
 
print(usd,eur,uyu,ars,rub)