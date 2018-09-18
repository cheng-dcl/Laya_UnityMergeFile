# Laya_UnityMergeFile

## 作用将Laya Unity导出工具产生的冗余资源合并。

在使用LayaUnity导出工具导出unity资源时，工具是按每个场景导出的。每个场景都独立导出依赖的资源并放在不同的文件夹。   
往往多个场景里面可能引用同一个物体，材质，贴图等。 这时候导出的的资源就产生了冗余。自然产生了多余的资源体积。  
写了个简单的工具，将冗余的资源合并。多个场景只引用同一个资源。

## 栗子
>* export_laya目录：从unity中导出的两个测试场景根路径。Test0【场景中一个Cube】和Test1【场景中一个Cube和一个Shpere】。导出后资源体积多出一个Cube模型文件和一个默认材质文件。
>* export_merge目录：重新合并的路径。合并减掉了cube模型文件和默认材质文件。节省了2.36kb。

## 使用
>* 1，下载`LayaUnityMergeFile.py`文件  
>* 2，安装python环境  
>* 3，命令：`python LayaUnityMergeFile.py srcPath destPath`  
      srcPath : LayaUnity导出的根路径，即export_laya目录（绝对路径）  
      destPath ： 重新合并的根路径，即export_merge目录（绝对路径）  
      

