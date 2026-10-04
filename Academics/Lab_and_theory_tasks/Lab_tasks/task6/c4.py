# question # 04 

prices = {"pen": 30, "notebook": 120, "bag": 1500, "calculator": 950,"marker": 60}

cart = [("pen", 3), ("notebook", 2), ("marker", 1), ("pen", 2),("eraser", 4), ("bag", 1), ("glue", 2)]


# combining cart quantities
cart_dic = {}
for i in range(len(cart)):
    s = 0
    for j in cart:
        if(cart[i][0] == j[0]):
            s += j[1]
    cart_dic[cart[i][0]] = s
print("Each element with its quantity being required :",cart_dic)


# finding unavailable items
unavailable = set()
for i in range(len(cart)):
    if(cart[i][0] not in prices.keys()):
        unavailable.add(cart[i][0])
l = list(unavailable)
l = sorted(l)
print(f"Sorted list of items not present in the prices :",l)


# calculating the line totals
iteem = ""
lin_total = 0
total = 0
for i, q in cart_dic.items():
    if i in prices:
        total += prices[i]*q
        print(f"{i} * {q} = {prices[i]*q}")
        if(lin_total < prices[i]*q):
            iteem = i
            lin_total = prices[i]*q
    else:
        print(f"The item '{i}' price is not present in the prices dict, so can't compute")

# printing the bill
discount = 0
if(total>1800):
    discount += (total*0.10)
print("Total bill :",total)
print("Discount on bill :",discount)
print("The amount to pay :",total-discount)



#  Highest line total
print(f"Item with highest line total :{iteem}, and its amount is :{lin_total}")





