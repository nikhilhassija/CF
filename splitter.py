file = open("ratings.dat", "r")

train = open("ua.base", "w")
test  = open("ua.test", "w")

last  = 0
count = 0

for line in file:
	user, item, rating, timestamp = map(int, line.split("::"))

	if user != last:
		last = user
		count = 0

	if count < 10:
		count += 1
		test.write(line.replace("::", "\t"))

	else:
		train.write(line.replace("::", "\t"))

train.close()
test.close()