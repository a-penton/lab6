# define lists containing different elements
list1 = [0,1,2,3,4]
list2 = [i for i in range(-1, -7, -1)]
list3 = [(2*i+3)%5 for i in range(10) if (2*i+3)%5 != 0]
list4 = [(i+2)%4 for i in range(8) if (i+2)%4 != 0]
list5 = [(4*i+2)%3 for i in range(4)]

def find_max(my_list):
	# compute maximum of elements
	max = 0
	for i in my_list:
		if my_list[i] > max:
			max = my_list[i]
	return max

def find_min(my_list):
	# compute minimum of elements
	min = 0
	for i in my_list:
		if my_list[i] < min:
			min = my_list[i]
	return min

def find_sum(my_list):
	# compute sum of elements
	sum = 0
	for i in my_list:
		sum += my_list[i]
	return sum

def find_length(my_list):
	# compute length of list
	length = 0
	for i in my_list:
		length += 1
	return length


print('The maximum of', list2, 'is', find_max(list2))		# should be -1
print('The minimum of', list3, 'is', find_min(list3))		# should be 1
print('The minimum of', list4, 'is', find_min(list4))		# should be 1
print(' + '.join(map(str, list5)), '=', find_sum(list5))	# should be 5
