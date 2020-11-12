import os
from os.path import basename # 맨 마지막 디렉토리 명 가지고 올 때 사용
import argparse

def get_args():
    parser = argparse.ArgumentParser('To make rgb.txt or depth.txt files - Taeyoung96')
    parser.add_argument('--image_path',required=True,help="Absolute Path of Image(RGB or Depth)",type=str)
    parser.add_argument('--time_stamp',required=True,help="To get Timestamp.txt ",type=str)
    parser.add_argument('--ext', required=False, default='.jpg', help="To extract Image extension", type=str)
    parser.add_argument('--image_list_name',required=False,default="image.txt",help="Naming the output list of Image",type=str)
    parser.add_argument('--final_list_name',required=False,default='final.txt',help="Naming the final output",type=str)

    args = parser.parse_args()
    return args

def make_timestamp(opt):
    file_path = opt.image_path
    final_file_path = basename(file_path)  # 맨 마지막 디렉토리 가져오기
    file_Ext = opt.ext          # 어떤 확장자만 추출할 것인가 설정

    # 이미지 폴더의 file path
    #file_path = "/home/taeyoungkim/Desktop/Matching_TimeStamp_Images/Images"
    global str # NameError: free variable 'str' referenced before assignment in enclosing scope 오류 해결
    file_list = os.listdir(file_path)   # file path에 있는 파일들 list 불러오기
    file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    image_list = opt.image_list_name
    # test.txt라는 파일에 .jpg파일 이름을 txt 파일로 반환
    with open(image_list,'w') as f:
        for file in file_list:
            if file.endswith(file_Ext):  # 특정 확장자의 file만 꺼내오기
                str_write = final_file_path+'/'+file
                f.write(str_write)           # .jpg 이름만 추출해서 읽어오기 - 폴더 이름 합침
                f.write("\n")


    # 방금 만든 test.txt,
    # Time stamp가 적혀져 있는 label.txt를 읽고
    # final.txt에 time stamp와 방금 만든 test.txt파일을 한 줄씩 읽어 반환
    time_stamp_name = opt.time_stamp
    final_list_name = opt.final_list_name

    text = open(time_stamp_name,'r')    # time stamp.txt 파일 읽기
    f = open(image_list,'r')        # 방금 만든 .jpg 이름들로 이루어진 txt 파일 읽기
    final = open(final_list_name,'w')

    while True: # 모든 줄 다 읽기
        line = text.readline().splitlines() # 한 줄씩 읽어오고 개행문자 제거
        f_line = f.readline().splitlines()
        if not line: break
        if not f_line: break
        str = line[0]   # 리스트로 반환하므로 첫번째 원소를 다시 변수에 저장
        str_f = f_line[0]

        sum_str = str+" "+str_f
        final.write(sum_str)    # final.txt파일에 쓰기
        final.write("\n")

    # All files closed
    text.close()
    f.close()
    final.close()



if __name__ == '__main__':
    opt = get_args()
    make_timestamp(opt)









