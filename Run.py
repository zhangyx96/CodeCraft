import numpy as np

from Data import LoadData
from floyd import Floyd

def GenerateGraph(road_info,cross_info,max_speed):  #初始化图
    road_nums =  road_info.shape[0]
    cross_nums = cross_info.shape[0]
    MAXWEIGHT = 99999  #用来表示不存在路径
    ROADINVALID = -1 #表示不存在路径
    road_table = np.zeros([cross_nums,cross_nums],dtype = int) + ROADINVALID
    graph = np.zeros([cross_nums,cross_nums],dtype = float) + MAXWEIGHT #初始化图
    for i in range(road_nums):
        start_id = int(road_info[i,4])-1  #cross编号从1开始
        end_id = int(road_info[i,5])-1
        speed_limit = min(max_speed,float(road_info[i,2]))
        graph[start_id,end_id] = float(road_info[i,1])/speed_limit#路径长度/最高限速
        road_table[start_id,end_id] = int (road_info[i,0]) 
        if int(road_info[i,6]):
            graph[end_id,start_id] = float(road_info[i,1])/speed_limit ##单双向判断
            road_table[end_id,start_id] = int (road_info[i,0]) 
    for j in range(cross_nums): #对角线置为0
        graph[j,j] = 0
    return graph,road_table

def run(car_path,road_path,cross_path,answer_path):
    car_info,road_info,cross_info = LoadData(car_path,road_path,cross_path)
    for i in range(car_info.shape[0]):
        car_id = int(car_info[i,0])
        start = int(car_info[i,1])-1
        end = int(car_info[i,2])-1
        max_speed = float(car_info[i,3])
        start_time = float(car_info[i,4])
        graph_init,road_table = GenerateGraph(road_info,cross_info,max_speed)
        graph, path =  Floyd(graph_init)
        car_path = path[start][end]
        road = []
        for j in range(len(car_path)-1):
            road.append(road_table[car_path[j],car_path[j+1]])
        print(path)    
        print(car_path)
        print(road)
    
        
    


    
if __name__ == "__main__":
    car_path = '../config/car.txt'
    road_path = '../config/road.txt'
    cross_path = '../config/cross.txt'
    answer_path = '../config/answer.txt'
    run(car_path,road_path,cross_path,answer_path)

