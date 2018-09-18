#!/usr/bin/env.python
# _*_ coding:utf-8 _*_

"""
    将laya unity导出工具产生的冗余的资源合并
    使用：
    命令：python LayaUnityMergeFile.py srcPath destPath
    srcPath：laya unity插件工具设置的导出根路径，绝对路径
    destName: 合并的根目录名，绝对路径
    File: LayaUnityMergeFile.py
    Author: dcl-Cheng   
"""

import os
import shutil
import sys

unnessSize = 0

def getscenedir():
    global scenesRoots
    scenesRoots = []
    for scenePath in os.listdir(sourcePath):
        p = os.path.join(sourcePath, scenePath)
        if os.path.isdir(p):
            scenesRoots.append(p)


def mergeAllScenes():
    if os.path.exists(rootPath):
        shutil.rmtree(rootPath)
    os.mkdir(rootPath)
    for scenePath in scenesRoots:
        merge(rootPath, scenePath)
    print("==》》合并完成,节省资源大小" + str(unnessSize / 1024) + "kb")

def merge(rootPath,scenePath):
    global unnessSize
    for sf in os.listdir(scenePath):
        s_n_p = os.path.join(scenePath, sf)
        r_n_p = os.path.join(rootPath, sf)

        if os.path.isfile(s_n_p):
            if os.path.exists(r_n_p):
                unnessSize += os.path.getsize(s_n_p)
                print("[相同的文件] " + s_n_p + "," + str(os.path.getsize(s_n_p)))
            else:
                shutil.copy2(s_n_p, r_n_p)
        elif os.path.isdir(s_n_p):
            if os.path.exists(r_n_p):
                merge(r_n_p,s_n_p)
            else:
                shutil.copytree(s_n_p, r_n_p)


if __name__ == '__main__':
    global rootPath
    global sourcePath


    if len(sys.argv) == 3:
        sourcePath = sys.argv[1].strip()
        rootPath =  sys.argv[2].strip()

    else:
        print("错误的参数 ，使用: python LayaUnityMergeFile.py srcPath destPath")

    print("""==》》开始合并目录：""" + sourcePath +
    """到==> """ + rootPath)
    getscenedir()
    mergeAllScenes()
