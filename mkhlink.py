import os
import sys

# 按结构创建目录和硬链接
def mkhlink(path,h):
    dir = ""
    for dirpath, dirnames, filenames in os.walk(path):
        if dir == "":
            dir = dirpath
        ps = dirpath.split("/")
        ps[0]=h
        newdir = "/".join(ps)
        try:
            os.mkdir(newdir)
            for file in filenames:
                print(file)
                os.link(dirpath+"/"+file,newdir+"/"+file)
        except Exception as e:
            print("创建目录失败：")
            print(e)
            exit()

def main():
    print("获取参数...")
    try:
        path = sys.argv[1]
        hlink = sys.argv[2]
    except Exception as e:
        print("获取参数错误")
        print("正确的使用方法：python3 mkhlink.py dir newdir")
        exit()
    if os.path.exists(path):
        if os.path.isabs(path):
            print("不能使用绝对路径，请将python文件放到要创建硬链接的相同目录中。")
            print(path)
            exit()
        else:
            mkhlink(path,hlink)
    else:
        print("要做硬链接的目录不存在："+path)

if __name__ == '__main__':
    main()
