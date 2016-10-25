#
bag = [1, 2, 3, 4, 5]
for i in range(len(bag)):
	bag[i]= bag[i]* 2
	
print bag

bag = [elem * 2 for elem in bag]
print "new:", bag

# 
recent_cart = ['product id 2', 'product_id 5', 'product id 4']
print 'My products: %s.' % ', '.join(recent_cart)

#
a = ['Cart', 'Products', 'float', 'true']
print " ".join(a)

#
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']

for x, y in zip(list1,list2):
	print x, y
	
#
a=7
b=5
b, a = a, b
print a 
print b

#
print 'float'*4+' '+'cart'*5

#
a = [[1, 2], [3, 4], [5, 6]]

import itertools
print list(itertools.chain.from_iterable(a))

#
a = 'ilovepython'
print 'Reverse is',a[::-1]
