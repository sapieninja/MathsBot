import math as maths
class equation:
    def parse_value(self,solution):
        """Evaluates NON ALGEBRAIC maths equations where everything is clearly laid out. For example (1*5)(1*5) is not allowed and must be replaced with (1*5)*(1*5)"""
        #BIDMAS
        #brackets
        #indices
        #division
        #multiplication
        #addition
        #subtraction
        #do 1 each time and then call itself
        #i'm lazy so big try except
        try: #any errors in here (which will happen if incorrect functions are given will be flagged up by this)
            if '(' in solution: #brackets
                sub_equation = solution[solution.index('(') + 1: solution.index(')')]
                sub_equation = self.parse_value(sub_equation) #need to work out the value of whatever is in the brackets
                solution = solution[:solution.index('(')] + sub_equation + solution[solution.index(')')+1:
                ]
            elif '^' in solution:
                #first we need to get the number behind the ^ sign
                location = solution.index('^')-1
                while location > 0:
                    try:
                        int(solution[location])
                    except:
                        break
                    location -= 1
                base = int(solution[location+1:solution.index('^')])
                location = solution.index('^')-1
                

        except:
            pass      
        return solution
    def __init__(self,text):
        self.text = text
        self.value = self.parse_value(self.text)
if __name__ == "__main__":
    equation = equation('asdf10000^5asdfas')
    print(equation.value)
