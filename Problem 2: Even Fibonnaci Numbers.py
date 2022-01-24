first = 1
second = 2

sum = 2
next = 0
while(next<4000000):
    next = first+second
    if(next%2==0):
        sum += next
    first = second
    second = next

print(sum)