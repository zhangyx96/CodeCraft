import numpy as np
def Floyd(graph_init):
    graph_ini = np.array(graph_init)
    graph = np.array(graph_init)
    length = len(graph)
    path = {}
    for k in range(length):
        for i in range(length):
            path.setdefault(i, {})
            for j in range(length):
                if i == j:
                    continue
                path[i].setdefault(j, [i,j])  #初始化直接路径
                new_node = None

                if k == j or k == i:
                    continue
                    
                new_len = graph[i][k] + graph[k][j]
                if graph[i][j] > new_len:
                    graph[i][j] = new_len
                    new_node = k
                if not new_node is None: # 不要用if new_node：None和0无法区分 
                    if graph[i][new_node]<graph_ini[i][new_node]: #i和newnode之间距离比初始值短
                        path[i][j]= path[i][new_node][:] #不要浅复制
                        if graph[new_node][j]<graph_ini[new_node][j]: #j和newnode之间距离比初始值短
                            path[i][j] = path[i][j]+path[new_node][j][1:]
                        else:                                      #j和newnode之间距离不比初始值短
                            path[i][j].append(j)
                    else:                                          #i和newnode之间距离不比初始值短
                        path[i][j] = [i,new_node]
                        if graph[new_node][j]<graph_ini[new_node][j]:
                            path[i][j] = path[i][j]+path[new_node][j][1:]
                        else:                                      #j和newnode之间距离不比初始值短
                            path[i][j].append(j)
                
                
    return graph, path
