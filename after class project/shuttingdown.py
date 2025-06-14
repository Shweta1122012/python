import os
def shutdown():
    confirm=input("are you sure you want to shutdown your computer? (yes/no): ")
    if confirm=="yes":
        print("shutting down in 1 second.......")
        os.system("shutdown /s /t 1")
    else:
        print("shutdown cancelled")
shutdown()    