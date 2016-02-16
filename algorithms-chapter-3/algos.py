play_list = range(1,11)
def linSearch(x, lis):
	i = 0
	while i<=len(lis) and x != lis[i]:
		i += 1
	if i<= len(lis):
		return i + 1
	else:
		return 0

print linSearch(9, play_list)

def binSearch(x, lis):
	#first set up two end points
	i = 0
	j = len(lis) -1
	while i<j:
		m = (i+j)/2
		if x > lis[m]:
			i=m+1
		else:
			j = m
	if x == lis[i]:
		return i + 1
	else:
		return 0
'''
Running binSearch for 5
1st loop
i = 0 j = 9 m = 4 lis[4] = 5
j becomes 4
2nd loop
i = 0 j = 4 m = 2 lis[2] = 3
i becomes 3
3rd loop
i = 3 j = 4 m = 3 lis[3] = 4
i becomes 4
while loop is no longer true
x == lis[4]
	return 5 for fifth spot in list
'''
print binSearch(5,play_list)