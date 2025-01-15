import argparse

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("--number2",help="second number") #adding "--" makes it optional
    parser.add_argument("--operation",help="operation")

    args=parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)
    n1=int(args.number1)
    n2=int(args.number2)
    result=None
    if args.operation=="add":
        result=n1+n2
    elif args.operation=="subtract":
        result=n1-n2
    elif args.operation=="multiply":
        result=n1*n2
    elif args.operation=="divide":
        result=n1/n2
    else:
        print("unsupported operation")
    print("Result=",result)

# without "--"
# PS D:\VsCode\AiML> python -u "d:\VsCode\AiML\argparser.py" 5 6 multiply
# 5
# 6
# multiply
# Result= 30

# all optional
# PS D:\VsCode\AiML> python -u "d:\VsCode\AiML\argparser.py" --number1 5 --number2 6
# 5
# 6
# None
# Result= 0

# final result
# PS D:\VsCode\AiML> python -u "d:\VsCode\AiML\argparser.py"  5 --number2 6         
# 5
# 6
# None
# Result= 0