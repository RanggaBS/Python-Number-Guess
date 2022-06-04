def main():
	import random
	print("\n-----------------\nGuess number game\n-----------------\n\nEnter number between 1 and 100\n")
	num = random.randint(1, 100)
	userNum = -1
	attempt = 0
	while userNum != num:
		userNum = int(input("Guess: "))
		if userNum < num:
			print("Too low.")
		elif userNum > num:
			print("Too high.")
		attempt += 1

	print(f"\nYour guess is right, the answer is {num}\nYour attempts: {attempt}\nThanks for playing this shit program!\n")

if __name__ == "__main__":
	main()
	
