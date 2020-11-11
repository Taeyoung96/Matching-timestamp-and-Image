import os
import argparse

"""
def get_args():
    parser = argparse.ArgumentParser('To split txt files - Taeyoung96')
    parser.add_argument('--txt_path', required=True, help="Absolute Path of txt file", type=str)

    args = parser.parse_args()
    return args

def split_txt(opt):
"""
#file_path = opt.image_path
file_path = '/home/taeyoungkim/Desktop/ORB_SLAM2/Examples/Monocular/rgbd_dataset_freiburg1_xyz/rgb.txt'
f = open(file_path,'r')
result = open('timestamp.txt','w')

while True:  # 모든 줄 다 읽기
    line = f.readline().splitlines()  # 한 줄씩 읽어오고 개행문자 제거
    if not line: break
    str = line[0]
    str_split = str.split(" ")[0]
    print(str_split)
    result.write(str_split)
    result.write('\n')

f.close()
result.close()

"""
if __name__ == '__main__':
    opt = get_args()
    split_txt(opt)
"""