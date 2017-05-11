'''     webwarrior
This module hides the `TaskWarrior` object from the `taskw` library.
Hence we have the possiblity to create our own methods to get
the data we want to present.  '''

from taskw import TaskWarrior

class Webwarrior(TaskWarrior):

    def __init__(self):
        super().__init__()

    #TODO: bad naming
    def project_tasks(self):
        ''' Return all tasks that have a project.
        :rtype: list of tasks
        '''
        tasks = self.filter_tasks({ 'status': 'pending' })
        return [ task for task in tasks if 'project' in task ]

    def tasks_per_project(self):
        ''' Construct a dict with a project name as keys and a list of the
        corresponding tasks to that project. '''
        tasks = self.project_tasks()
        # TODO: how to represent this mapping between project name and task related
        #       to that porject?
        #       list of tuples: [ ( 'projectname' [ tasks ... ] ) ... ]
        #       or better as dict: { 'projectname' [ tasks ... ] }

        tasks_per_project = dict()
        for task in tasks:
            proj_name = task['project']
            if proj_name in tasks_per_project:
                tasks_per_project[proj_name].append(task)
            else:
                tasks_per_project[proj_name] = [task]

        return tasks_per_project
