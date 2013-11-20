# Prime factorization
# Enter a number and returns all its prime factors


# Checks if is a prime
def is_a_prime(a):
	for i in range (2, a):
		if (a%i==0):
			return False
	return True		

# Gets input from the user.
input_number = int(input("Please enter a number (or -1 to exit.): "))

while input_number!=-1:
	print "You entered:", input_number

	if input_number==0 or input_number==1:
		print ("%d is not a prime number nor does it have any prime factors.") % input_number

	else:	
		print ("Its prime factors are: ")

		for x in range(2, input_number):
			prime_marker = 0
			while (input_number%x==0):
				if is_a_prime(x) or prime_marker==1:
					input_number = input_number/x
					print x
		
					if input_number==1:
						break
						
			if input_number==1:
				break	

	input_number = int(input("Please enter a number (or -1 to exit.): "))

print "Exiting..."