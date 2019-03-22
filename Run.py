from Data import LoadData


def run(car_path,road_path,cross_path,answer_path):
    car_info,road_info,cross_info = LoadData(car_path,road_path,cross_path)

    
if __name__ == "__main__":
    car_path = '../config/car.txt'
    road_path = '../config/road.txt'
    cross_path = '../config/cross.txt'
    answer_path = '../config/answer.txt'
    run(car_path,road_path,cross_path,answer_path)

