num = int(input())
i = 1
j = 0
hasil = i
while i <= num:
    hasil *= i
    i += 1
i = 0
while hasil > 0:
    i = hasil%10
    j += i
    hasil = hasil//10
print(j)
