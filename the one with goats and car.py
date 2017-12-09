from random import SystemRandom
sr = SystemRandom()

doors = [0 for j in range(input("enter the number of doors: "))]
n = len(doors)
print("len(doors) = ",n)
sum1 = 0
sum2 = 0
inv = 0
nc = 0
iterations = 0
	
def not_car(random_chosen_door):
	global nc	
	if random_chosen_door == 1:
		nc += 1
		random_chosen_door = sr.choice(range(n))
		random_chosen_door = not_car(random_chosen_door)
	return random_chosen_door

def valid_door(a,b):
	global inv
	if (a == b) or (doors[b] == -1):
		inv += 1
		b = sr.choice(range(n))
		valid_door(a,b)
	return b
	
for i in range(100000):
	iterations += 0
	door_with_car = sr.choice(range(n))
	doors[door_with_car]=1#assign car to a random door
	user_chosen_door = sr.choice(range(n))#user chooses a random door
	opened_door = not_car(sr.choice(range(n)))
	doors[opened_door] = -1#opening a door with goat
	
	#case1 where choice changes
	new_chosen_door = valid_door(user_chosen_door,sr.choice(range(n)))
	if new_chosen_door == 1:
		sum1 += 1
	#case2 where choice doesn't change
	if user_chosen_door == 1:
		sum2 += 1
	
	#making doors[] usable again
	doors[door_with_car] = 0
	doors[opened_door] = 0
	
print(inv,nc)
print(sum1, ' ', sum2)
	
