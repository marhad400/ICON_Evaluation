
class Calculator:
    def eval(self, expression):
        ''' Insert your code to process the string input here '''
        result = 0
        tokens = expression.split()

        # Counting number of tokens
        count = 0
        for token in tokens:
            print(token, end=' ')
            count += 1
        
        # Valid case: Making sure there are 3 tokens which are 2 numeric operands and a '+' operator in infix format
        if count == 3:
            if tokens[1] == "+":
                try:
                    result = int(tokens[0]) + int(tokens[2])
                except ValueError:
                    try:
                        result = float(tokens[0]) + float(tokens[2])
                    except ValueError:
                        print("Incorrect format, please enter in the form 'a + b'")
            else:
                print("Operator must be a plus (+)")
        
        # Invalid Cases: 
        # Not 3 tokens
        elif count != 3:
            print("Incorrect format, please enter only 2 numbers and 1 '+' in your expression in the form 'a + b'")
            # Empty String
            if count == 0:
                print("Input is empty, please enter an addition operation.")

        return result


    def run(self):
        # Run until the user cancels, ctl + C
        while True:
            expression = input('Enter an infix addition statement: ')
            result = self.eval(expression)
            print(' = ', result)

if __name__ == "__main__":
    # If this file is run directly from the command line, run the calculator
    c = Calculator()
    c.run()