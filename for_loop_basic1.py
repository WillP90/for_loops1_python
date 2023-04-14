# #1 Basic - print 1 - 150
for i in range(0,151,1):
    print(i)

# #2 multiples of five
for m in range(5, 1005, 5):
    print(m)

#  #3 counting, the dojo way
for d in range(0, 101, 1):
    if d % 10 == 0:
        print("coding dojo")
    elif d % 5 == 0:
        print("coding")
    else:
        print(d)

#  #4 whoa. that sucker's huge
sum = 0
for h in range(500001):
    sum = sum + h
print(sum)

#  #5 countdown by 4
for n in range(2018, 0, -4):
    if n % 2 == 0:
        print(n)

#  #6 flexible counter
lowNum = 2
highNum = 18
mult = 3
for n in range(lowNum, highNum + 1):
    if n % mult == 0:
        print(n)