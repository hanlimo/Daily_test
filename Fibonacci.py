print "Please input number what you wanna stop" 
num = int(raw_input())

def fibonacci(num):
	'This func can caculate Fabonacci Sequence flexibly'
	result = [0,1]
	for i in range(num):
		result.append(result[-1]+result[-2])
	return result

print fibonacci(num)
print 'Function instruction:'+fibonacci.__doc__
#__doc__:print the first_raw info before the func ith the style of ''