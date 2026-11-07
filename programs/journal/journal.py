# ask user for input, the activity done
# write it in the file
# display activities done in an organized way

from datetime import datetime
import csv

print("----My Journal----")
print("1. Add activity")
print("2. View journal")
choice = input("Which do you want to do? (type number): ")
if choice == "1":
    activity = input("Activity done: ").replace(", ", " ")
    print(f"{activity} has been added.")
    with open("activity.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "task"])
        writer.writerow({"timestamp": datetime.now().strftime("%H:%M"), "task": activity})
elif choice == "2":
    print("----My Journal Entries----")
    with open("activity.csv") as file:
        for line in file:
            reader = csv.DictReader(file)
            time, task = line.split(",", 1)
            print(f"{time}: {task}", end="")
else:
    print("Invalid choice.")