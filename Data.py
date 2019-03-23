import numpy as np

def LoadData(car_path,road_path,cross_path):
    car_info = np.loadtxt(car_path,dtype=str,delimiter = ', ')
    road_info = np.loadtxt(road_path,dtype=str,delimiter = ', ')
    cross_info = np.loadtxt(cross_path,dtype=str,delimiter = ', ')
    for i in range (car_info.shape[0]):  #去括号
        car_info[i,0] = car_info[i,0][1:]
        car_info[i,4] = car_info[i,4][:-1]
    for i in range (road_info.shape[0]):
        road_info[i,0] = road_info[i,0][1:]
        road_info[i,6] = road_info[i,6][:-1]
    for i in range (cross_info.shape[0]):
        cross_info[i,0] = cross_info[i,0][1:]
        cross_info[i,4] = cross_info[i,4][:-1]
        
    return car_info,road_info,cross_info