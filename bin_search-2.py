#test info
seq = [10,2,99,34,48,10,83,743,210,67,39,66]
print seq
seq.sort()
number = input('Input a number from the sequence:')
length = len(seq)-1

def search(sequence, num, lower, upper):
	if upper ==None:
		upper = length
	if lower == upper:
		assert number == sequence[upper]
		print upper
		return upper
	else:
		middle = (lower+upper)//2
		if number > sequence[middle]:
			return search(sequence, number, middle+1, upper)
		else:
			upper = middle
			return search(sequence, number, lower, middle)
		
search(sequence=seq, num=number, lower=0, upper=None)