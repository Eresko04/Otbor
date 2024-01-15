s = [int(x) for x in open("17_2.txt")]
k = 0 #количество подходящих лестничных клеток
mink = 10**9 #минимальная сумма квартир на лестничной клетке
for i in range(len(s)-2):
    a = s[i]
    b = s[i+1]
    c = s[i+2]
    if (1000<=a<=9999 and 1000<=b<=9999  and not(1000<=c<=9999)) or (1000<=a<=9999 and not(1000<=b<=9999) and 1000<=c<=9999) or (not(1000<=a<=9999) and 1000<=b<=9999 and 1000<=c<=9999):
        if a%7==0 or b%7==0 or c%7==0:
            if (a+b+c)%100==17:
                k += 1
                mink = min((a+b+c),mink)
print(k, mink)              
        
        