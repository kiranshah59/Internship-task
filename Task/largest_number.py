def find_largest(numbers):
    if len(numbers) == 0:
        return "List is empty"
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest
nums = input("Enter numbers separated by space: ")
num_list = list(map(int, nums.split()))
result = find_largest(num_list)

print("Largest number is:", result)