import math as maths
class equation:
    def parse_value(self,solution):
        """Evaluates NON ALGEBRAIC maths equations where everything is clearly laid out. For example (1*5)(1*5) is not allowed and must be replaced with (1*5)*(1*5)"""
        def get_operands(equation,operator):
            location_operand_one = solution.index(operator)-1
            while location_operand_one >= 0:
                try:
                    int(solution[location_operand_one])
                except:
                    if solution[location_operand_one] != '.':
                        break
                location_operand_one -= 1
            operand_one = float(solution[location_operand_one+1:solution.index(operator)])
            location_operand_two = solution.index(operator)+1
            while location_operand_two <= len(solution)-1:
                try:
                    int(solution[location_operand_two])
                except:
                    if solution[location_operand_two] != '.':
                        break
                location_operand_two += 1
            operand_two = float(solution[solution.index(operator)+1:location_operand_two])
            return operand_one,operand_two,location_operand_one,location_operand_two            
        #BIDMAS
        #brackets
        #indices
        #division
        #multiplication
        #addition
        #subtraction
        #do 1 each time and then call itself
        try:#i'm lazy so big try except
            if '(' in solution: #brackets
                sub_equation = solution[solution.index('(') + 1: solution.index(')')]
                sub_equation = self.parse_value(sub_equation) #need to work out the value of whatever is in the brackets
                solution = solution[:solution.index('(')] + f"{sub_equation:.20f}" + solution[solution.index(')')+1:]
            elif '^' in solution: #indices
                base,exponent,location_base,location_exponent = get_operands(solution,'^')
                print(base,exponent)
                answer = maths.pow(base,exponent) #has floating point support whcih is good (complete accuracy of values is not essential
                #now we need to splice this value back into the equation as a whole
                solution = solution[:location_base+1] + f"{answer:.20f}" + solution[location_exponent:]
            elif '/' in solution:#division
                dividend,divisor,location_dividend,location_divisor = get_operands(solution,'/')
                answer = dividend/divisor
                solution = solution[:location_dividend+1] + f"{answer:.20f}" + solution[location_divisor:]
            elif '*' in solution:#multiplication
                no_1,no_2,location_1,location_2 = get_operands(solution,'*')
                answer = no_1*no_2
                solution = solution[:location_1+1] + f"{answer:.20f}" + solution[location_2:]
            elif '+' in solution:#addition
                no_1,no_2,location_1,location_2 = get_operands(solution,'+')
                answer = no_1+no_2
                solution = solution[:location_1+1] + f"{answer:.20f}" + solution[location_2:]
            elif '-' in solution:#subtraction
                no_1,no_2,location_1,location_2 = get_operands(solution,'*')
                answer = no_1-no_2
                solution = solution[:location_1+1] + f"{answer:.20f}" + solution[location_2:]
        except:
            solution = 0
        try:
            float(solution)
        except:
            return self.parse_value(solution)
        return float(solution)
    def __str__(self):
        return f"{self.value:.10f}"
    def __init__(self,text):
        self.text = text
        self.value = self.parse_value(self.text)
if __name__ == "__main__":
    equation = equation('1000000*(533^2)+24')
    print(equation.value)
