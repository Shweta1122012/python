num = int(input("Enter a number:"))
odd = [i for i in range(num) if i%2!=0]
even = [i for i in range(num) if i%2==0]
print("Odd numbers:",odd)
print("Even numbers:",even) 



fruits = ['apple','banana','watermelon','mango','orange']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)