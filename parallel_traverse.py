import threading
import thread_safe
import abc
import build_config
import simple_ioc


class IDependencyExtractor(metaclass=abc.ABCMeta):
    # 解析工程配置到文本文件
    @abc.abstractmethod
    def read_repo_config(self, code_path, output_path):
        pass


class IGraphConverter(metaclass=abc.ABCMeta):
    # 将文本文件转化成dot文件
    @abc.abstractmethod
    def convert(self, txt_path, output_path):
        pass


class IRepoBuilder(metaclass=abc.ABCMeta):
    # 构建某一个具体repo
    @abc.abstractmethod
    def build(self, repo_name):
        pass


class BuildProcess(object):
    def __init__(self):
        # TODO: 依赖注入
        self.dep_parser = None
        self.txt_converter = None
        self.builder = None
        self.code_path = ''
        self.txt_path = 'slnDpd_Releasex64.txt'
        self.dot_path = 'mcsf.gv'
        self.max_thread = 4
        self.graph = thread_safe.ThreadSafeGraph()
        self.queue = thread_safe.ThreadSafeQueue()

        self.cond = threading.Condition()
        self.is_running = True

    def from_xml(self, xml_path):
        config = build_config.CreateFromDocument(open(xml_path).read())
        # config = build_config.parallel_buildType()
        self.txt_path = config.text_path
        self.dot_path = config.dox_path
        self.max_thread = config.num_thread
        self.dep_parser = simple_ioc.Container().get(config.dependency_parser)
        self.txt_converter = simple_ioc.Container().get(config.graph_parser)
        self.builder = simple_ioc.Container().get(config.repo_builder)

    def thread_fun(self):
        while not self.graph.is_traversed():
            repo = self.queue.pop()
            self.builder.build(repo)
            list_repo_next = self.graph.finish_node(repo)
            for repo_next in list_repo_next:
                self.queue.push(repo_next)

        print("Thread quit.")

    def build(self):
        self.dep_parser.read_repo_config(self.code_path, self.txt_path)
        self.txt_converter.convert(self.txt_path, self.dot_path)
        self.graph.from_dot(self.dot_path)
        list_repo = self.graph.lowest_nodes()
        for repo in list_repo:
            self.queue.push(repo)

        list_thread = []
        for i in range(1, self.max_thread + 1):
            build_thread = threading.Thread(target=self.thread_fun())
            list_thread.append(build_thread)
            build_thread.start()

        for build_thread in list_thread:
            build_thread.join()

        print("All threads have stopped.")
