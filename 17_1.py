k = 0 #количество подходящих ответов
maxk = 0 #максимальный подходящий ответ
for n in range(1000,9999+1):
    s = str(n)
    if (n%10)%2==1 and s.count('7')==1:
        k += 1
        maxk = max(n,maxk)
print(k,maxk)