sample_list = [1,2,3,4,5]
sample_str = "salman"
for i in sample_str:
    print(i)


#for i in sample_list:
#sample_list is a iterable
iterator_obj = iter(sample_str)
print(iterator_obj.__iter__())

#1: return iterator object via __iter__()
#2: Assign pointer or index value of each item

print(iterator_obj)

print(next(iterator_obj)) # index = 1
#if index<len(data): move forward and increment the index value
    #first he checks the current position. oi position er value 

#else: stopiterator

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))