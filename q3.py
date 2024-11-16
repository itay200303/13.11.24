
cubes_dict = {num: num**3 for num in range(1, 21)}
print(cubes_dict)

user_input: int = int(input("Enter a number: "))
if user_input in cubes_dict:
    print(f"the result {user_input} is power 3: {cubes_dict[user_input]}")
else:
    print("is not exist")