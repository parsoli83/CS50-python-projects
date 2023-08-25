exp=input("Expression:").lower().strip().split()
n1=float(exp[0])
n2=float(exp[-1])
match exp[1]:
    case "+":
        print(round(n1+n2,1))
    case "-":
        print(round(n1-n2,1))
    case "/":
        print(round(n1/n2,1))
    case "*":
        print(round(n1*n2,1))