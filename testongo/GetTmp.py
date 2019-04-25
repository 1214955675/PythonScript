import os
import threading

allFileNum = 0
distdir={"攀枝花":"56666","凉山":"56571","甘孜":"56146","阿坝州":"56172","宜宾":"56492","乐山":"56386",
         "内江":"57503","成都":"56187","眉山":"56391","德阳":"56198","绵阳":"56196","广元":"57206",
         "泸州":"57508","广安":"57415","南充":"57411","达州":"57328","巴中":"57313"}
fileList = []
def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(path+'/'+f)
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print( '-' * (int(dirList[0])), dl  )
            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        print('-' * (int(dirList[0])), fl)
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1


def getDataFromOneFile(filepath):
    try:
        fin = open(filepath, "r")
    except IOError:
        print("Error: open file failed.")
        return

    for line in fin:
        everyrow=line.split('\n')
        everyword=everyrow[0].split(' ')
        for i in range(len(everyword)):
            if everyword[0] in distdir.values():
                print(everyword)


if __name__ == "__main__":
    # printPath(1, 'F:/3.26/2018温度')
    printPath(1, 'F:/2018')
    print('总文件数 =', allFileNum)
    threads = []
    for item_file in fileList:
        tt=threading.Thread(target=getDataFromOneFile, args=(item_file,))
        threads.append(tt)
    # t1 = threading.Thread(target=getDataFromOneFile, args=(u'F:/2018/201801.000',))
    # threads.append(t1)
    # t2 = threading.Thread(target=getDataFromOneFile, args=(u'F:/2018/201802.000',))
    for t in threads:
        t.setDaemon(True)
        t.start()
    getDataFromOneFile("F:/2018/201801.000")
    # getDataFromOneFile("F:/3.26/2018温度/201801.000")