# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import graphviz
import parallel_traverse


class SolutionGraphConverter(parallel_traverse.IGraphConverter):
    def __init__(self):
        return

    def convert(self, txt_path, output_path):
        g = graphviz.Digraph('G', filename=output_path, format='svg')
        sln_list = []
        f = open(txt_path, 'r')
        depender = ''
        while True:
            line = f.readline()
            if line == '':
                break
            if not line.find(' ') == 0:
                depender = line.split('.')[0]
                g.node(depender)
                sln_list.append(depender)
            else:
                line = line.strip()
                depended = line.split('.')[0]
                if not depended == depender:
                    g.edge(depender, depended)

        g.view()
        print("SolutionGraphConverter::convert Finished.")


class ProjectGraphConverter(parallel_traverse.IGraphConverter):
    def __init__(self):
        return

    def convert(self, txt_path, output_path):
        g = graphviz.Digraph('G', filename='mcsf.cpp.app.gv', format='svg')
        proj_list = []
        solution_name = ''
        project_name = ''
        edge_list = []
        solution_num = 0
        project_num = 0
        dependency_num = 0
        is_to_continue = True
        f = open(txt_path, 'r')
        while is_to_continue:
            with g.subgraph(name='mcsf_%s' % solution_name) as c:
                if solution_name != '':
                    # c.attr(style='filled', color='black')
                    c.attr(label=solution_name)
                while True:
                    line = f.readline()
                    if line == '':
                        f.close()
                        is_to_continue = False
                        break
                    line = line[:-1]
                    line = line.strip()
                    names = line.split('.')
                    if len(names) == 2 and names[1] == 'sln':
                        solution_name = names[0]
                        solution_num += 1
                        break
                    else:
                        names = line.split('/')
                        if len(names) == 1:  # project within the solution
                            project_name = names[0]
                            if not check_ut_proj(project_name):
                                c.node(project_name)
                                proj_list.append(project_name)
                                project_num += 1
                        elif not check_ut_proj(project_name):
                            ds = names[0].split('.')[0]
                            dependency_num += 1
                            if ds == solution_name:  # dependency within the solution
                                c.edge(project_name, names[1])
                            elif True:  # dependency between solutions
                                edge_list.append([project_name, names[1]])

        for e in edge_list:
            g.edge(e[0], e[1])

        print('Solution Number: %d' % solution_num)
        print('Project Number: %d' % project_num)
        print('Dependency Number: %d' % dependency_num)
        g.view()


def check_ut_proj(proj_name):
    return proj_name[::-1].find('TU') == 0


def check_cpp_proj(proj_name):
    return proj_name.find('Mcsf') == 0


def check_algo_proj(proj_name):
    return  proj_name.find('McsfAlgo') == 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sc = SolutionGraphConverter()
    if len(sys.argv) == 1:
        #  project_dependency_graph('ProjDpd_Releasex64.txt')
        sc.convert('slnDpd_Releasex64.txt', 'mcsf.solution.gv')
    else:
        sc.convert(sys.argv[1], sys.argv[2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
