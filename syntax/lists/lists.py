#!/usr/bin/python3

'nested list'

siblings = [['caleb', 21], ['abel', 26], ['peter', 17], ['kevin', 21]]

print("name = ", siblings[0][0])

for i in siblings:
    print(i)

print(siblings.index(['peter', 17]))

numbers = [1, 2, 3, 4,2 , 1,3 ,4, 2,2 , 5, 9, 4]

print("number of instances a number occurs: ", numbers.count(4))

numbers.sort(reverse=True)
print(numbers)


#scrimba exe

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

sales_w2.append(int(input('enter number of lemonades sold on last day week 2: ')))
sales = sales_w1

for i in sales_w2:
    sales_w1.append(i)
    
sales_w1 = sales
print(sales)

print(max(sales) * 1.5)
print(min(sales) * 1.5)