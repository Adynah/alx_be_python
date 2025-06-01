task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Urgent: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task. Create some time to work on it.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires attention before the end of today.")
        else:
            print(f"{task} is a medium priority task. It would be nice to get this done.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task but still has to be completed.")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid. Enter a priority!")
