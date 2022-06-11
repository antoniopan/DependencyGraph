import queue
import threading
import networkx as nx


class ThreadSafeQueue(object):

    def __init__(self):
        self.cond = threading.Condition()
        self.queue = queue.Queue()

    def push(self, item):
        self.cond.acquire()
        while self.queue.full():
            self.cond.wait()

        self.queue.put(item)
        self.cond.notify()
        self.cond.release()

    def pop(self):
        item = None
        self.cond.acquire()
        while self.queue.empty():
            self.cond.wait()

        item = self.queue.get()
        self.cond.notify()
        self.cond.release()
        return item


class ThreadSafeGraph(object):

    def __init__(self):
        self.graph = nx.DiGraph()
        self.mutex = threading.Lock()
        self.num_traversed = 0

    def is_traversed(self):
        self.mutex.acquire()
        is_traversed = (self.num_traversed == self.graph.number_of_nodes())
        self.mutex.release()
        return is_traversed

    def from_dot(self, dot_path):
        self.mutex.acquire()
        self.graph = nx.drawing.nx_agraph.read_dot(dot_path)
        self.num_traversed = 0
        for n in self.graph.nodes:
            self.graph.nodes[n]['IsTraversed'] = False
        self.mutex.release()

    def lowest_nodes(self):
        list_node = []
        self.mutex.acquire()
        for n in self.graph.nodes:
            if len(list(self.graph.successors(n))) == 0:
                list_node.append(n)
        self.mutex.release()
        print("%s are the lowest nodes." % list_node)
        return list_node

    def finish_node(self, node_name):
        list_node = []
        self.mutex.acquire()
        self.graph.nodes[node_name]['IsTraversed'] = True
        for node_next_level in list(self.graph.predecessors(node_name)):
            ready_to_be_built = True
            for node_dep in list(self.graph.successors(node_next_level)):
                if not self.graph.nodes[node_dep]['IsTraversed']:
                    ready_to_be_built = False
                    break
            if ready_to_be_built:
                list_node.append(node_next_level)

        self.num_traversed += 1
        print("%d of %d nodes trversed." % (self.num_traversed, self.graph.number_of_nodes()))
        self.mutex.release()
        print("Node %s finished." % node_name)
        return list_node
