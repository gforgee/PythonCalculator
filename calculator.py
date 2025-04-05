from tokens import ExpressionProcess
from calculate import Calculate

# ----  TODO  ----
# variables handling
# functions handling
# and bad things like user input: "2 (2)""
if __name__ == "__main__":
	while True:
		try:
			expr = input('Write an expression: ')   
			if expr == "exit" or expr == "quit" or expr == "q":
				print('Exiting...')
				break
			elif expr == "clear":
				print("\033[H\033[J")
			elif expr == "":
				continue
			elif expr == "help":
				print('''
				Commands:
				"exit" - exit the program
				"help" - show this help message
				"clear" - clear the screen
				"quit" - exit the program
				"q" - exit the program
				Also you can exit from the cli with ctrl + c''')
			else:
				result = ExpressionProcess(expr).get_result()
				calculate = Calculate(result)
				calculate.evaluate()
				print(calculate.get_result())
				
				
		except KeyboardInterrupt:
			break