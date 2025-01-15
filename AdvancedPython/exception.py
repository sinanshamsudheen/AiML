class UserException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def printException(self):
        print("User Exception Occurred: ",self.msg)

try:
    raise UserException('User caused an error')
except UserException as e:
    e.printException()

try:
    num=6/0
    # print(num)
except Exception as e:
    print("An exception occured:",e)
finally:
    print("finally block")