import numpy as np
from Data import LoadData

def GenerateGraph(road_info,cross_info):  #初始化图
    road_nums =  road_info.shape[0]
    cross_nums = cross_info.shape[0]
    MAXWEIGHT = 99999  #用来表示不存在路径
    graph = np.zeros([cross_nums,cross_nums],dtype = float) + MAXWEIGHT #初始化图
    for i in range(road_nums):
        start_id = road_info[i,4] - 1  #cross编号从1开始
        end_id = road_info[i,5] - 1
        graph[start_id,end_id] = road_info[1]/road_info[2] #路径长度/最高限速
    for j in range(cross_nums): #对角线置为0
        graph[j,j] = 0

    return graph



def run(car_path,road_path,cross_path,answer_path):
    car_info,road_info,cross_info = LoadData(car_path,road_path,cross_path)
    graph = GenerateGraph(road_info，cross_info)


    
if __name__ == "__main__":
    car_path = '../config/car.txt'
    road_path = '../config/road.txt'
    cross_path = '../config/cross.txt'
    answer_path = '../config/answer.txt'
    run(car_path,road_path,cross_path,answer_path)

