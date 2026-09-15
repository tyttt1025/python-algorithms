def process_task(tasks):
    if len(tasks) == 0:
        return "No tasks."
    for i in range(len(tasks)):
        print (f"Processing: {tasks[0]}")
        tasks.pop(0)
    return "All tasks complete!"

task = ["email", "backup", "report"]
print(process_task(task))