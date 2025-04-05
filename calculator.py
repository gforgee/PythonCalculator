from tokens import ExpressionProcess
from calculate import Calculate

# ---- TODO  ----
# variables handling
# functions handling
# and bad things like user input: "2 (2)""
if __name__ == "__main__":
	while True:
		try:
			expr = input('Podaj wyrazenie: ')   
			if expr == "exit":
				break
				print('Wyjscie')
			else:
				result = ExpressionProcess(expr).get_result()
				calculate = Calculate(result)
				calculate.evaluate()
				print(calculate.get_result())
				
				
		except KeyboardInterrupt:
			break