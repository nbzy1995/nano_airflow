import pytest
from nano_airflow.core import Task, Workflow
from pathlib import Path


def test_task_execution_shell_command(tmp_path):
    task = Task("write_hello", "echo 'Hello, World!' > hello.txt")
    work_dir = tmp_path / "test_task"
    work_dir.mkdir(parents=True)

    task.execute(work_dir)
    output_file = work_dir / "hello.txt"
    assert output_file.exists()
    assert output_file.read_text().strip() == "Hello, World!"


def test_task_execution_callable(tmp_path):
    task = Task("compute_sum", lambda: sum(range(10)))
    work_dir = tmp_path / "test_task_callable"
    work_dir.mkdir(parents=True)

    task.execute(work_dir)
    output_file = work_dir / "compute_sum.out"
    assert output_file.exists()
    assert output_file.read_text().strip() == "45"


def test_workflow_execution(tmp_path):
    task1 = Task("task1", "echo 'Task 1 completed!' > task1.txt")
    task2 = Task("task2", "echo 'Task 2 completed!' > task2.txt")

    workflow = Workflow()
    workflow.add_task(task1)
    workflow.add_task(task2)

    work_dir = tmp_path / "test_workflow"
    work_dir.mkdir(parents=True)

    workflow.execute(work_dir)

    assert (work_dir / "task1.txt").read_text().strip() == "Task 1 completed!"
    assert (work_dir / "task2.txt").read_text().strip() == "Task 2 completed!"
