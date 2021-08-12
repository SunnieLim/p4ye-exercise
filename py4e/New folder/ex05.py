largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        numb = int(num)
        if smallest is None:
            smallest = numb
        elif numb < smallest:
            smallest =numb
        elif numb > largest:
            largest=numb


    except:
        print("Invalid input")

print ("Maximum is",largest)
print ("Minimum is",smallest)
