# nano_airflow

`nano_airflow` is a lightweight Python library for managing workflows and tasks, in the spirit of Apache Airflow

## Features
- Supports shell commands and Python functions as tasks.
- Logs output, errors, and results for each task.
- Organizes workflows and allows restarting from specific tasks.

## Installation
Clone the repository and install the library:
```bash
git clone https://github.com/your_username/nano_airflow.git
cd nano_airflow
pip install .
```

## Usage
Define tasks and workflows in Python:

```python
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
```


## Testing
Run tests with pytest:

```bash
pytest tests/
```
