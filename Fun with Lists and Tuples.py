tuples_list = []

n = int(input("Enter the number of tuples: "))

for i in range(n):
    tuple_str = input(f"Enter tuple {i+1} (space-separated values): ")
    tuple_values = tuple(map(int, tuple_str.split()))
    tuples_list.append(tuple_values)

sorted_list = sorted(tuples_list, key=lambda x: x[-1])

print("Sorted list:")
for item in sorted_list:
    print(item)