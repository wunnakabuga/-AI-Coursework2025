values = []
for i in range(5):
    value= float(input(f"Enter a value {i+1}: "))
    values.append(value)
average= sum(values)/len(values)
print(f"The values are: {values}")
print(f"The average is: {average}")
