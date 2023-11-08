import math

class RPN:
    
    function_list = ["sqrt", "pow"]
    
    def __init__(self) -> None:
        pass
        
    def checkctype(self, c):
        """Verifing type of char c\n
        returning: \n
        0 type not found\n
        1 is numeber\n
        2 is letter (funct)\n
        3 is comma (function argument separator)\n
        4 is operator ["-", "+", "*", "/", "%", "^"]\n
        5 is left parenthesis\n
        6 is right parenthesis\n
        """
        numbers = ["0","1","2","3","4","5","6","7","8","9", "."]
        operators = ["-", "+", "*", "/", "%", "^"]

        c = str(c)
        
        if c.isnumeric() or c == ".":
            return 1 # number
        if c.isalpha():
            return 2 # letter
        if c == ",":
            return 3 # comma
        if operators.count(c):
            return 4 # operator
        if c == "(":
            return 5 # left parentesis
        if c == ")":
            return 6 # right parentesis
        return 0
    
    def strToList(self, equasion):
        """
        Method coverts string into list\n
        eg: str("2+5-4*sqrt(25,2)")\n
        return: [2.0, "+", 5.0, "-", 4.0, "*", "sqrt", "(", 25.0, ",", 2.0, ")"]\n
        """
        out = list()
        ctype = 0
        t = ""
        
        append = lambda t, ctype: float(t) if ctype == 1 else t

        # preparing a list from str

        for i, c in enumerate(equasion):
            actype = self.checkctype(c)
            
            # if actype is number or digit
            if actype > 2:
                if ctype < 3 and ctype > 0:
                    out.append(append(t, ctype))
                    t = ""
                out.append(c)
                ctype = 0
            else:
                if ctype == actype or ctype == 0:
                    t += c
                    ctype = actype
                else:
                    out.append(append(t, ctype))
                    t = ""
                    ctype = 0

        out.append(append(t, ctype))
        
        # removes double -- to proper count -x and y--x
        outlen = len(out)
        if outlen > 1:

            # if out begin with ["-", ...] insert 0 [0.0, "-", ...]
            if out[0] == "-":
                out.insert(0, 0.0)
                
            # search every pattern ["* / - + ^", "-", float, ...] and convert that into ["* / - + ^", -float, ...]
            i = 1
            while True:
                try:
                    if self.checkctype(out[i - 1]) == 4 and out[i] == "-" and type(out[i + 1]) == float:
                        out.insert(i + 1, -out.pop(i + 1))
                        out.pop(i)
                        i += 2
                        continue
                    if out[i - 1] == "-" and out[i] == "-":
                        out.insert(i + 1, "+")
                        out.pop(i)
                        out.pop(i - 1)
                        i += 2
                        continue
                    i += 1
                    if i > len(out) - 1:
                        break
                except:
                    break        
        
        return out
    
    def getPrior(self, c):
        """
        Returns priority of operator to compare
        """
        match c:
            case "(":
                return 0
            case "+":
                return 1
            case "-":
                return 1
            case ")":
                return 1
            case "*":
                return 2
            case "/":
                return 2
            case "%":
                return 2
            case "^":
                return 3
        
    def listToRPN(self, l):
        """
        Method converts list returned by strToList() to list in RPN notation\n
        eg: [2.0, "+" 3.0] to [2.0, 3.0, "+"]\n
        """
        output = list()
        stack = list()
        
        # for every element from list
        for i, e in enumerate(l):
            
            # if float, put on output    
            if type(e) == float:
                output.append(e)
                continue
            
            # if function, put on stack
            if self.function_list.count(e):
                stack.append(e)
                continue
            
            # if comma, take from stack and put on output until left parenthesis on stack will be found
            # if left parenthesis will not be found, equation has wrong parenthesis count
            if e == ",":
                while stack[-1] != "(":
                    try:
                        output.append(stack.pop())
                    except:
                        return "equasion error"
                continue
            
            # if left parenthesis, put on stack
            if e == "(":
                stack.append(e)
                continue
            
            # if right parenthesis, take from stack and put on output until left parenthesis on stack will be found
            # if left parenthesis will not be found, equation has wrong parenthesis count
            if e == ")":
                while stack[-1] != "(":
                    try:
                        output.append(stack.pop())
                    except:
                        return "equasion error"
                stack.pop()
                
                # if function on stack, take that function from stack and put on output
                if len(stack):
                    if self.function_list.count(stack[-1]):
                        output.append(stack.pop())
                    
            # if operator, take operators from stack until operator on stack will have higher or equal priority
            if self.checkctype(e) == 4:
                prio = self.getPrior(e)
                while True:
                    try:
                        if self.checkctype(stack[-1]) == 4:
                            sprio = self.getPrior(stack[-1])
                            if sprio >= prio:
                                output.append(stack.pop())
                            else:
                                stack.append(e)
                                break
                        else:
                            stack.append(e)
                            break
                    except:
                        stack.append(e)
                        break
        
        # until stack will be empty take from stack and put on output
        while True:
            try:
                output.append(stack.pop())
            except:
                break

        return output

    def count(self, quation):
        """
        Method counts result of equation in str\n
        Returns result of equation as float 
        """

        arglist = self.strToList(quation)
        rpnlist = self.listToRPN(arglist)

        stack = list()
        
        # for every element from rpn list
        for c in rpnlist:
            try:
                
                # if float, put on stack
                if type(c) == float:
                    stack.append(c)
                    continue
                
                # if operator, take arguments from stack and put result on stack
                if self.checkctype(c) == 4:
                    a = stack.pop()
                    b = stack.pop()
                    match c:
                        case "+":
                            stack.append(b + a)
                        case "-":
                            stack.append(b - a)
                        case "*":
                            stack.append(b * a)
                        case "/":
                            if a == 0:
                                return False
                            stack.append(b / a)
                        case "^":
                            stack.append(math.pow(b, a))
                    continue
                
                # it's fuction, take arguments from stack and put result on stack
                match c:
                    case "sqrt":
                        stack.append(math.sqrt(stack.pop()))
                    case "pow":
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(math.pow(b, a))
                    case _:
                        continue
            except:
                break
        return stack[-1]
