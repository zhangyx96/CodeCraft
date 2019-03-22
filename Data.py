import numpy as np

def LoadData(car_path,road_path,cross_path):
    car_info = np.loadtxt(car_path,dtype=str)
    road_info = np.loadtxt(road_path,dtype=str)
    cross_info = np.loadtxt(cross_path,dtype=str)
    return car_info,road_info,cross_info