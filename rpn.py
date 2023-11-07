import math

class RPN:
    
    function_list = ["sqrt", "pow"]
    
    def __init__(self) -> None:
        pass
        
    def checkctype(self, c):
        """Verifing type of char c
        returning: 
        0 type not found
        1 is numeber
        2 is letter (funct)
        3 is comma (function argument separator)
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
        output = list()
        stack = list()
        
        for i, e in enumerate(l):
                        
            if type(e) == float:
                output.append(e)
                continue
            if self.function_list.count(e):
                stack.append(e)
                continue
            if e == ",":
                while stack[-1] != "(":
                    try:
                        output.append(stack.pop())
                    except:
                        return "equasion error"
                continue
            if e == "(":
                stack.append(e)
                continue
            if e == ")":
                while stack[-1] != "(":
                    try:
                        output.append(stack.pop())
                    except:
                        return "equasion error"
                stack.pop()
                if self.function_list.count(stack[-1]):
                    output.append(stack.pop())
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
        
        while True:
            try:
                output.append(stack.pop())
            except:
                break

        return output

    def count(self, input):

        arglist = self.strToList(input)
        onplist = self.listToRPN(arglist)

        stack = list()
        for c in onplist:
            try:
                if type(c) == float:
                    stack.append(c)
                    continue
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
                            stack.append(b / a)
                        case "^":
                            stack.append(math.pow(b, a))
                    continue
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
