from os import listdir
from os.path import isdir, isfile, join

from app.bp_blog.models import PostSchema


class BlogLoader():

    def __init__(self, data_dir):
        self.data_dir = data_dir
        pass

    def load_models(self):
        models = []
        year_dirs = self._find_all_year_dirs(self.data_dir)
        for d in year_dirs:
            post_files = self._find_all_post_files(d)
            for f in post_files:
                models.append(self._load_post_model(f))
        return models

    def _find_all_year_dirs(self, dir):
        year_dirs = [
            join(self.data_dir, f)
            for f in listdir(self.data_dir)
            if isdir(join(self.data_dir, f))
        ]
        return year_dirs

    def _find_all_post_files(self, dir):
        post_files = [
            join(dir, f)
            for f in listdir(dir)
            if isfile(join(dir, f))
        ]
        return post_files

    def _load_post_model(self, filename):
        print filename
        jsonstr = open(filename).read()
        print jsonstr
        post_schema = PostSchema()
        post = post_schema.loads(jsonstr).data
        return post
