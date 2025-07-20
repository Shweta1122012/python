import random

def generate_password(length=12):
    chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password=''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        print("random password is", generate_password())
        cont= input("want to Generate another password?(y/n)").strip().lower()
        if cont!='y':
            break
