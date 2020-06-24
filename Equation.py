class Equation:
    def parse_value(self,text):
        #BIDMAS
        #brackets
        #indices
        #division
        #multiplication
        #addition
        #subtraction
        #do 1 each time and then call itself
        #i'm lazy so big try except
        solution = text
        if '(' in text: #brackets
            print('got to here')
            sub_string = text[text.index('(')+1:text.index(')')]
            #now we have the "sub" equation that we need to solve it
            #the logical solution is just to call our parse function again
            sub_answer = self.parse_value(sub_string)
            solution = sub_string[:text.index('(')] + sub_answer + sub_string[text.index(')'):]
                
        return solution
    def __init__(self,text):
        self.text = text
        self.value = self.parse_value(self.text)
if __name__ == "__main__":
    equation = Equation('asijdfja(123+13),aisdphfsd')
    
