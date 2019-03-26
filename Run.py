import numpy as np
from math import ceil
import matplotlib.pyplot as plt

from data import LoadData
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

def GetAnswer(car_id,start_time,car_path,road_table):
    ans = '(' + str(car_id)   #car_id
    ans = ans + ', ' + (str(start_time)) #计划出发时间
    for j in range(len(car_path)-1):
        ans = ans + ', ' +str(road_table[car_path[j],car_path[j+1]])
    ans += ')' 
    return ans

def WriteFile(answer_path,ans,first_flag):
    if first_flag == 0:  #若是第一次打开，则新建文件
        file = open(answer_path,'w')
    else:
        file = open(answer_path,'a') #继续读写
    file.write(ans)
    file.close()


def run(car_path,road_path,cross_path,answer_path):  #每辆车一张图
    car_info,road_info,cross_info = LoadData(car_path,road_path,cross_path)
    ans = []
    car_nums = car_info.shape[0]
    for i in range(car_nums):
        car_id = int(car_info[i,0])
        start = int(car_info[i,1])-1
        end = int(car_info[i,2])-1
        max_speed = int(car_info[i,3])
        start_time = int(car_info[i,4])
        graph_init,road_table = GenerateGraph(road_info,cross_info,max_speed)
        graph, path =  Floyd(graph_init)
        car_path = path[start][end]
        #print('car {} path:{}'.format(car_id,car_path))
        ans.append(GetAnswer(car_id,start_time,car_path,road_table))
        print('[{}/{}]'.format(i+1,car_nums))
    np.savetxt(answer_path,ans,fmt='%s')

def run_0(car_path,road_path,cross_path,answer_path):
    car_info,road_info,cross_info = LoadData(car_path,road_path,cross_path)
    ans = []
    car_nums = car_info.shape[0]
    cars_speed = np.array(car_info[:,3],dtype = int)
    speeds = [8,6,4,2]
    N =500
    time = np.linspace(10,700,N,dtype=int)
    car_info_group =[]
    for s in speeds:
        car_info_group.append(car_info[cars_speed == s])
    count = 0
    for i in range(len(speeds)):
        graph_init,road_table = GenerateGraph(road_info,cross_info,speeds[i])
        graph, path =  Floyd(graph_init)   
        for j in range(car_info_group[i].shape[0]):
            count += 1
            car_id = int(car_info_group[i][j,0])
            start = int(car_info_group[i][j,1])-1
            end = int(car_info_group[i][j,2])-1
            start_time = int(car_info_group[i][j,4])
            car_path = path[start][end]
            if car_path == -1:
                a = 0
            time_id = ceil(count/car_nums*N)-1
            ans.append(GetAnswer(car_id,time[time_id],car_path,road_table))
    np.savetxt(answer_path,ans,fmt='%s')

if __name__ == "__main__":
    car_path = '../config/car.txt'
    road_path = '../config/road.txt'
    cross_path = '../config/cross.txt'
    answer_path = '../config/answer.txt'
    run_0(car_path,road_path,cross_path,answer_path)

