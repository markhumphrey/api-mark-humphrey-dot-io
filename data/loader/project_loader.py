from os import listdir
from os.path import isfile, join

from app.bp_project.models import ProjectSchema


class ProjectLoader():

    def __init__(self, data_dir):
        self.data_dir = data_dir
        pass

    def load_models(self):
        models = []
        project_files = self._find_all_project_files(self.data_dir)
        for f in project_files:
            models.append(self._load_project_model(f))
        return models

    def _find_all_project_files(self, dir):
        project_files = [
            join(dir, f)
            for f in listdir(dir)
            if isfile(join(dir, f))
        ]
        return project_files

    def _load_project_model(self, filename):
        print filename
        jsonstr = open(filename).read()
        print jsonstr
        project_schema = ProjectSchema()
        project = project_schema.loads(jsonstr).data
        print project.id
        print project.name
        print project.description
        return project
