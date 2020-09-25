刚才在微信朋友圈看到关于Yolo目标检测的新的网络：YOLObile

它的paper下载链接是 https://arxiv.org/abs/2009.05697
github代码地址是 https://github.com/CoCoPIE-Pruning/CoCoPIE-ModelZoo/tree/master/YOLObile
我把代码和模型.pt文件下载到本地后运行了一下，可以看到它是基于pytorch框架实现的，下载到的.pt文件有245M，这么大，我有些怀疑YOLObile是否真的如paper种所说的“在移动设备上实时检测”。

接下来我就想编写一个用opencv的dnn模块做YOLObile的目标检测，但是模型文件时.pt格式的，这是dnn模块不支持的格式，于是我就想把它提供的.pt文件转换成darknet框架里的.weights文件。
方法是本代码仓库里的convert_darknet.py文件，把它拷贝到YOLObile文件夹里，然后运行，程序会读取.cfg文件和.pt文件，最后生成.weights文件。
有了.cfg文件和.weights文件，我们就可以利用opencv的dnn木块做目标检测，此时就不依赖pytorch框架了。
.weights文件有245M，无法直接上传到github，百度云盘的下载
链接: https://pan.baidu.com/s/1FsTGBoGuJNYSdGvFSw9Trg 提取码: mc9b

把.weights文件下载完成之后放在本仓库代码的文件夹里，运行main_yolobile.py
