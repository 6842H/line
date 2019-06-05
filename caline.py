# coding: utf-8 
# @Time : 2019/6/5 上午 10:35 
# @Author : gyn 
# @email : guogyn@foxmail.com

import os


def calculate(file_path):
    c = 0
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line = line.encode()
            # print('len=%s, line=(%s)' % (len(line), line))
            if len(line) > 1:   # 忽略空行
                c += 1
    return c


def calculates(root):
    succeed = []   # 统计成功的文件
    failed = []
    ignored = []    # 忽略

    for dir_path, dir_names, file_names in os.walk(root):
        for file_path in file_names:
            try:
                file_path = os.path.join(dir_path, file_path)
                _, tail = os.path.splitext(file_path)
                print(file_path, 'tail=', tail)
                if tail in tails:
                    # if tail in ['']
                    t = calculate(file_path)    # 单文件内代码行数
                    succeed.append([file_path, t])
                else:
                    ignored.append(file_path)
            except Exception as e:
                failed.append(file_path)
                print(file_path, '统计错误', e)
    return succeed, failed, ignored


def show(root):
    succeed, failed, ignored = calculates(root)
    summ = 0
    print('\n统计成功文件数： ', len(succeed))
    for s in succeed:
        summ += s[1]
        print('代码行数：%s\t%s' % (s[1], s[0]))
    print('\n统计失败文件数： ', len(failed))
    for f in failed:
        print('统计失败', f)
    print('\n被忽略文件数： ', len(ignored))
    for i in ignored:
        print('忽略', i)

    print('\n该项目总代码函数：', summ)


tails = [
    # '.txt'
    '.py',
    '.c', '.h', '.cpp', '.bas',
    '.java',
    '.cs', '.asp', '.aspx',
    '.php',
    '.jsp',
    '.html', '.htm',
    '.css', '.js'
]
# ignore = ['jpg', 'png', 'jpeg', 'bmp', 'gif', 'doc', 'tar']

root = "D:\PyCharm_Project\\v5"
show(root)
