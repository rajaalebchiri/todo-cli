import click
import datetime
import json
import os

TODO_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'todos.json')


def read_todos():
    """Get todos from the json file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []


def display_task(i=1, todo=""):
    """Display a task in good format"""
    return f"{i}. {todo['task']} {'[✓]' if todo['status'] == 'done' else '[x]'} - {todo['date']}"


def create_todos(todos):
    """create a task with status and date to the file"""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)


@click.group()
def cli():
    """cli click group"""
    pass


@cli.command()
def list_tasks():
    """get the list of todos"""
    todos = read_todos()
    if todos:
        click.echo("Tasks:")
        for i, todo in enumerate(todos, 1):
            click.echo(display_task(i, todo))
    else:
        click.echo("No tasks in the todo list")


@cli.command()
@click.argument('task')
def add(task):
    """add new task to the list"""
    todos = read_todos()
    todo = {"task": task, "status": "to do",
            "date": str(datetime.date.today())}
    todos.append(todo)
    create_todos(todos)
    click.echo(f"Task added successfully, {display_task(todo=todo)}")
