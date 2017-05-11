# webwarrior-task - A Web Interface for Taskwarrior

**This is a work in progress project.**

webwarrior-task is a python, flask-based web interface for Taskwarrior, inspired from [taskwarrior-web](https://github.com/theunraveler/taskwarrior-web/).
Contributions are very welcome.

## Features (todos)

* task overview
* task filtering
* task manipulation

## Requirements

* [taskwarrior](https://taskwarrior.org/)
* python 3
* virtualenv (highly recommended)

## Usage

Since this is in development its highly recommended to use a `virtualenv`.

Setting up a `virtualenv` with python3.
`virtualenv --python=python3 venv`

Activate the `vitrualenv`.
`. venv/bin/activate`

Install the `webwarrior` in develop mode.
`pip install -e ./`

Run the application.
`python run.py`

## License

webwarrior-task is distributed under the MIT License.
See the LICENSE file for the full license text.
