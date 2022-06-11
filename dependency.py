# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import graphviz
import networkx as nx


def solution_dependency_graph(filename):
    g = graphviz.Digraph('G', filename='mcsf.solution.gv', format='svg')
    nxg = nx.DiGraph()
    sln_list = []
    f = open(filename, 'r')
    depender = ''
    while True:
        line = f.readline()
        if line == '':
            break
        if not line.find(' ') == 0:
            depender = line.split('.')[0]
            g.node(depender)
            nxg.add_node(depender, depth=0)
            sln_list.append(depender)
        else:
            line = line.strip()
            dependee = line.split('.')[0]
            if not dependee == depender:
                g.edge(depender, dependee)
                nxg.add_edge(depender, dependee)

    print('Solution Number: %d' % nxg.number_of_nodes())
    print('Dependency Number: %d' % nxg.number_of_edges())
    #g.view()
    cal_depth(sln_list, nxg)
    # print('Depth of the Graph: %d' % nx.shortest_path_length(nxg, source='McsfReview', target='McsfSystemEnvironmentConfig'))


def cal_depth(sln_list, nxg):
    while not len(sln_list) == 0:
        for n, nbrs in nxg.adj.items():
            if n in sln_list:
                depth = 0
                is_deepest = True
                for nbr in nbrs:
                    if nbr in sln_list:
                        is_deepest = False
                        break
                    depth = max(depth, nxg.nodes()[nbr]['depth'] + 1)
                if is_deepest:
                    print(depth)
                    nxg.nodes()[n]['depth'] = depth
                    sln_list.remove(n)


def project_dependency_graph(filename):
    # Use a breakpoint in the code line below to debug your script.
    g = graphviz.Digraph('G', filename='mcsf.cpp.app.gv', format='svg')
    nxg = nx.DiGraph()
    proj_list = []
    solution_name = ''
    project_name = ''
    edge_list = []
    solution_num = 0
    project_num = 0
    dependency_num = 0
    is_to_continue = True
    f = open(filename, 'r')
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
                            nxg.add_node(project_name, depth=0)
                            proj_list.append(project_name)
                            project_num += 1
                    elif not check_ut_proj(project_name):
                        ds = names[0].split('.')[0]
                        dependency_num += 1
                        if ds == solution_name:  # dependency within the solution
                            c.edge(project_name, names[1])
                            nxg.add_edge(project_name, names[1])
                        elif True:  # dependency between solutions
                            edge_list.append([project_name, names[1]])

    for e in edge_list:
        g.edge(e[0], e[1])
        nxg.add_edge(e[0], e[1])

    print('Solution Number: %d' % solution_num)
    print('Project Number: %d' % project_num)
    print('Dependency Number: %d' % dependency_num)
    #g.view()
    #cal_depth(proj_list, nxg)


def check_ut_proj(proj_name):
    return proj_name[::-1].find('TU') == 0


def check_cpp_proj(proj_name):
    return proj_name.find('Mcsf') == 0


def check_algo_proj(proj_name):
    return  proj_name.find('McsfAlgo') == 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) == 1:
        #  project_dependency_graph('ProjDpd_Releasex64.txt')
        solution_dependency_graph('slnDpd_Releasex64.txt')
    else:
        project_dependency_graph(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
