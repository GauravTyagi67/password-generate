import random

lower="abcdefghijklmnopqrstuvwxyz"

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number="0123456789"

symbol="[]{}()*;/,-_"

a=lower+upper+number+symbol

length=8

password="".join(random.sample(a,length))

print(password)
