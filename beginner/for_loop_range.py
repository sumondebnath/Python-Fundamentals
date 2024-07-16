

nums = input("Please Enter Numbers: ").split()

print(nums)
print(len(nums))

for num in range(0, len(nums), 2):
    print(f"Index is {num} And Value is {nums[num]} ")