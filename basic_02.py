# logical operators
price = 25
print(price>10 and price<30) #answer=true
print(price>10 and price<20) #answer=false
print( price>10 or price<20) #answer=true
print(price>10 or price<30) #answer=true

#if statements
temperature = 25
if temperature>30:
    print("It's a hot day.")
elif temperature>20:
    print("It's nice day.")
elif temperature>10:
    print("It's kind a cold")
else:
    print("It's cold outside")
print("Done")

#Exercise
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: "+str(converted))
else:
    converted = weight*0.45
    print("Weight in Kgs: "+str(converted))
