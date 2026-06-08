import time

def collect_list(list_name):
    """Prompt user to fill a list until they say they are done."""
    result = []
    while True:
        item = input(f"Enter an item for {list_name}: ")
        result.append(item)
        done = input("Are you through? (yes/no): ").strip().lower()
        if done == 'yes':
            break
    return result

# Collect list1
print("\n--- Building List 1 ---")
list1 = collect_list("list1")

# Collect list2
print("\n--- Building List 2 ---")
list2 = collect_list("list2")

# Check lengths
if len(list1) != len(list2):
    print("\nlength of lists don't match")
else:
    print("\nlengths match. Proceeding", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()  # newline after the dots

    # Build the dictionary
    result_dict = dict(zip(list1, list2))

    print("\nResulting dictionary:")
    for key, value in result_dict.items():
        print(f"  {key}: {value}")