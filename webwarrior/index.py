''' index '''

from flask import Flask, render_template, redirect, url_for
from .webwarrior import Webwarrior

import pprint

app = Flask(__name__)

app.config.update(dict(
    Warrior = Webwarrior(),
    DEBUG = True,
))

def format_date(date):
    pass

def format_tags(tags):
    pass

@app.route("/")
def index():
    ''' Landing page, redirect to list of 'pending' tasks. '''
    # return redirect(url_for('/tasks/pending'))
    return list_tasks('pending')


@app.route("/tasks/<command>")
def list_tasks(command='pending'):
    ''' List tasks given by `load_taks` method.
        We can specify a command by which the resulting task list is filtered.
            all - all tasks
            pending - all pending tasks
            complete - all completed tasks
    '''

    tw = app.config['Warrior']
    tasks = tw.load_tasks(command)
    app.logger.debug('rendering tasks/index.html: {} tasks'.format(len(tasks[command])))
    pprint.pprint(tasks)
    return render_template('tasks/index.html', tasks=tasks[command], status=command)


# @app.route("/projects/<project_name>")
@app.route("/projects")
def list_projects(project_name=None):

    warrior = app.config['Warrior']
    tasks = warrior.tasks_per_project()
    pprint.pprint(tasks)
    return render_template('projects/index.html', project_tasks=tasks)
