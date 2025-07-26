class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructor created")
def creat_object():
    print("making object......")
    obj=employee()
    print("function end")
    return obj
print("calling creat_object")
obj=creat_object()
print("programe end")