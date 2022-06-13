import parallel_traverse
import random
import time


class DummyDependencyExtractor(parallel_traverse.IDependencyExtractor):
    def __init__(self):
        print("This is an instance of DummyDependencyExtractor.")
        return

    def read_repo_config(self, code_path, output_path):
        print("DummyDependencyExtractor::read_repo_config()")
        return


class DummyGraphConverter(parallel_traverse.IGraphConverter):
    def __init__(self):
        print("This is an instance of DummyGraphConverter.")
        return

    def convert(self, txt_path, output_path):
        return


class DummyRepoBuilder(parallel_traverse.IRepoBuilder):
    def __init__(self):
        print("This is an instance of DummyRepoBuilder.")
        return

    def build(self, repo_name):
        time.sleep(float(random.randint(1, 100)) / 1000)
        return


