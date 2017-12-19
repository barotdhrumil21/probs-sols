n = int(input('enter number of people: '))
curr_1=1
for i in range(n):
    curr_1 += i+1
    if n == curr_1:
        print(1)
        break
    if n < curr_1:
        curr_1 -= i+1
        print(2*(n - curr_1+1)-1)
        break