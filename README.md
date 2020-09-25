刚才在微信朋友圈看到关于Yolo目标检测的新的网络：YOLObile
它的paper下载链接是 https://arxiv.org/abs/2009.05697
github代码地址是 https://github.com/CoCoPIE-Pruning/CoCoPIE-ModelZoo/tree/master/YOLObile
我把代码和模型.pt文件下载到本地后运行了一下，可以看到它是基于pytorch框架实现的，于是我就想把它提供的.pt文件转换成darknet框架里的.weights文件。
方法是本代码仓库里的convert_darknet.py文件，把它拷贝到YOLObile文件夹里，然后运行，就可以生成.weights文件。这个文件有245M，无法直接上传到github，百度云盘的下载链接是

链接: https://pan.baidu.com/s/1FsTGBoGuJNYSdGvFSw9Trg 提取码: mc9b

把.weights文件下载完成之后放在本仓库代码的文件夹里，运行main_yolobile.py，就可以看到在一张图片上的检测结果
