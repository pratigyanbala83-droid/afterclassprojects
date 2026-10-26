n = int(input("Enter the number whose sum you want to find:"))
sum = 0
m= int(input("Enter the number whose difference you want to find:"))
dif = 0
l = int(input("Enter the product you want to find:"))
mul = 0
k = float(input("Enter the division you want to find: 0"))
div = 0



for i in range(1,n+1):
    sum = sum+i

    print("n\sum = ",sum)



    for i in range(1,m-1):
      dif = dif-i

    print("n\dif = ",dif)

    for i in range(1,l*1):
       mul = mul*1

    print("n\mul =",mul)

    for i in range(1,k/1):
      div = div/i

    print("n\div = ",div)
