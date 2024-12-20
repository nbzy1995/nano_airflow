from nano_airflow.core import Task, Workflow
from pathlib import Path

# Define tasks
task1 = Task("hello", "echo 'Hello, World!' > hello.txt")
task2 = Task("add", lambda: sum(range(10)))

# Define workflow
workflow = Workflow()
workflow.add_task(task1)
workflow.add_task(task2)

# Execute workflow
work_dir = Path("results/")
workflow.execute(work_dir)
