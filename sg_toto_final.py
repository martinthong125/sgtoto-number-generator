import random
   
system =int(input("Key in the quick pick system: "))
draw= int(input ("Key in the number of draws you want: "))

#least likely outcome based on last 30 outcomes
cold_num =[2, 3, 5, 6, 14, 18, 36, 37, 42, 47]
#high likely outcome based on last 30 outcomes
hot_num = [4, 7, 8, 9, 10, 11, 16, 19, 21, 22, 24, 25, 26, 28, 29, 30, 31, 33, 35, 38, 40, 43, 44, 46, 49]

final = []
count =0
while count < draw:
	for i in range(system):
		draw_num = random.randrange(1,50)
		while draw_num in final or draw_num in cold_num:
			draw_num = random.randrange(1,50)
		final.append(draw_num)

	final.sort()
	total = sum(final)
    
	points = 0
	even = 0
	odd = system
	low = 0
	high = system
	#for sys 6, sum of 115 to 175
	system_low = system * 19
	system_high = system * 29
	
	#find how many odd even numbers and low high numbers than 24
	for j in final:
		if (j%2)==0:
			even= even + 1
		if j <= 24:
			low = low + 1
	odd = system - even
	high = system - low
	
	#calculate points
	if even >= system//3 and odd >= system//3:
	#if (odd == system//2 or odd + 1 == system//2):
		points = points + 1
	if (low >= system //3) and (high >= system//3):
		points = points + 1
	if (total >= system_low) and (total <= system_high):
		points = points + 1
		
	#find num of cold num
	cold = 0
	for k in final:
		if k in cold_num:
			cold = cold + 1
			
	#find num of hot num
	hot = 0
	for k in final:
		if k in hot_num:
			hot = hot + 1 
	
	if system%2 == 0 and (system//2 == even or system//2 == even + 1): #even system
		odd_even = 1
	elif system%2 == 1 and (system//2 == even): #odd system
		odd_even = 1
	else:
		odd_even = 0
		 
    
	if points == 3 and (odd_even == 1):
		print( final, total, odd, even)
		count +=1
	final = []
	
print("[numbers], sum, odd, even")
