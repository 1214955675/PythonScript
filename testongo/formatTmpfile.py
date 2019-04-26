import xlwt
import xlrd
import threading
import os
allFileNum = 0
fileList = []
distdir={"攀枝花":"56666","凉山":"56571","甘孜":"56146","阿坝州":"56172","宜宾":"56492","乐山":"56386",
         "内江":"57503","成都":"56187","眉山":"56391","德阳":"56198","绵阳":"56196","广元":"57206",
         "泸州":"57508","广安":"57415","南充":"57411","达州":"57328","巴中":"57313"}
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
            if 'dist' in f:
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
def formatfile(filepath,num):
    distcitycode = distdir.get(list(distdir.keys())[num])
    distcity = list(distdir.keys())[num]
    print(filepath+"------"+str(distcity))
    #用于写入xls
    mywriteWorkbook = xlwt.Workbook()
    mywriteSheet = mywriteWorkbook.add_sheet(str(num),cell_overwrite_ok=True)
    for f in fileList:
        workfile = xlrd.open_workbook(f)
        table = workfile.sheet_by_index(0)
        numrow=0
        for i in range(table.nrows):
            citycodeinmiddlefile=table.row_values(i)[0]
            if  citycodeinmiddlefile == distcitycode:
                mywriteSheet.write(numrow,0,table.row_values(i)[0])
                mywriteSheet.write(numrow,1,table.row_values(i)[1])
                mywriteSheet.write(numrow,2,table.row_values(i)[2])
                mywriteSheet.write(numrow,3,table.row_values(i)[3])
                mywriteSheet.write(numrow,4,table.row_values(i)[4])
            numrow=numrow+1;
            print(table.row_values(i))
    mywriteWorkbook.save(filepath+str(distcity)+".xls")
if __name__ == '__main__':
    printPath(1, 'F:/2018')
    finalpath='F:/2018/final/'
    isExists = os.path.exists(finalpath)
    if not isExists:
        os.makedirs(finalpath)
    threads=[]
    num=0
    for i in range(len(distdir)):
        tt = threading.Thread(target=formatfile, args=(finalpath, num,))
        threads.append(tt)
        num=num+1
    for t in threads:
        # t.setDaemon(True)
        t.start()

