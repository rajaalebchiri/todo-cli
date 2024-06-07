import os
import json
import datetime
from click.testing import CliRunner
from todo_cli.todo import cli, TODO_FILE


def test_list():
    runner = CliRunner()
    runner.invoke(cli, ['add', 'Test task 1'])
    runner.invoke(cli, ['add', 'Test task 2'])
    result = runner.invoke(cli, ['list-tasks'])
    assert result.exit_code == 0
    assert f'1. Test task 1 [x] - {str(datetime.date.today())}' in result.output
    assert f'2. Test task 2 [x] - {str(datetime.date.today())}' in result.output
