import subprocess
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


class Task:
    def __init__(self, name, command):
        """
        Initialize a Task.

        Args:
            name (str): Task name.
            command (str): Python expression or shell command to execute.
        """
        self.name = name
        self.command = command

    def execute(self, work_dir):
        """
        Execute the task and log results and errors.

        Args:
            work_dir (Path): Directory where task outputs and logs are stored.
        """
        output_path = work_dir / f"{self.name}.out"
        log_path = work_dir / f"{self.name}.log"
        error_path = work_dir / f"{self.name}.err"


        # Prepare command
        if isinstance(self.command, str):  # Command line
            cmd = self.command
            try:
                with log_path.open('w') as log_file, error_path.open('w') as error_file:
                    logging.info(f"Executing task {self.name}: {cmd}")
                    subprocess.run(cmd, shell=True, stdout=log_file, stderr=error_file, check=True, cwd=work_dir)
                    logging.info(f"Task {self.name} completed successfully.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Task {self.name} failed: {e}")
                raise
        elif callable(self.command):  # Python function
            try:
                result = self.command()  # Call the function
                logging.info(f"Executing callable task {self.name}")
                with output_path.open('w') as f:
                    f.write(str(result))  # Write result to output file
                logging.info(f"Callable task {self.name} completed successfully.")
            except Exception as e:
                logging.error(f"Callable task {self.name} failed: {e}")
                raise
        else:
            logging.error(f"Invalid command type for task {self.name}.")
            raise ValueError("Command must be a string or callable.")



class Workflow:
    def __init__(self):
        self.tasks = []
        # self.dependencies = {}

    def add_task(self, task, depends_on=None):
        """Add a task to the workflow."""
        self.tasks.append(task)
        # self.dependencies[task.name] = depends_on or []


    def execute(self, work_dir, start_task=None):
        """Execute tasks in the workflow sequentially"""
        start_index = 0

        # If starting from a specific task, determine the index
        if start_task:
            for i, task in enumerate(self.tasks):
                if task.name == start_task:
                    start_index = i
                    break

        for task in self.tasks[start_index:]:
            task.execute(work_dir)


