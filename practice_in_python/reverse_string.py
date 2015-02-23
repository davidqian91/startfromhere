input = "a cat goes to market"
stack = []
top = -1
output = ""
for w in input:
	if w== ' ':
		while top>=0:
			output = output+(stack.pop())
			top = top-1
		output = output+(' ')
	else:
		stack.append(w)
		top = top+1
while top>=0:
	output = output+(stack.pop())
	top = top-1
print(output)