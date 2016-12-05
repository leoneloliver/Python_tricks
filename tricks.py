#example 1
bag = [1, 2, 3, 4, 5]
for i in range(len(bag)):
	bag[i]= bag[i]* 2
	
print bag
bag = [elem * 2 for elem in bag]
print "new:", bag

#example 2
recent_cart = ['product id 2', 'product_id 5', 'product id 4']
print 'My products: %s.' % ', '.join(recent_cart)

#example 3
a = ['Cart', 'Products', 'float', 'true']
print " ".join(a)

#example 4
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']

for x, y in zip(list1,list2):
	print x, y
	
#example 5
a=7
b=5
b, a = a, b
print a 
print b

#example 6
print 'float'*4+' '+'cart'*5

#example 7
a = [[1, 2], [3, 4], [5, 6]]

import itertools
print list(itertools.chain.from_iterable(a))

#example 8
a = 'ilovepython'
print 'Reverse is',a[::-1]

#example 9
numbers = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []

while len(numbers) > 0:
	number = numbers.pop()
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)
		
print even
print odd

#example 10
def best_way(number):
    if number%2==0:
        print "even"
    else:
        print "odd"

best_way(4)

#exemple 11
l = [[1, 2, 3], [4, 5, 6]]
print zip(*l)

#exemple 12
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %s cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

	print "We can just give the function numbers directly:"

cheese_and_crackers(20, 30)

#exemple 13
drinks = ["coffee", "tea", "milk", "water"]
for drink in drinks:
    print("thirsty for", drink)


