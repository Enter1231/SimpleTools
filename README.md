# Simple Tools For Images - 简单图片工具箱

这是一个用于简单调整和计算图片数据集的系列代码工具，支持批量操作，让一些简单实用的功能不再一次次上网查询
***********

## 工具说明：

### Resize - 尺寸调整

位于.\SimpleTools\Size\resize.py内

用于批量调整图像尺寸，文件内包含函数resize()也可对单张图像操作。

操作参数有：

-path 想要调整的图像的所在目录

-size 想要调整的目标图像宽度，宽高比锁定

示例：将位于E:\images 的图像调整为宽度500的图像
```
cd
python .\SimpleTools\Size\resize.py -path E:\images -size 500
```
输出图像位置位于输入目录下的\resized文件夹内，本例中位于E:\images\resized

***
### Align - 尺寸对齐

位于.\SimpleTools\Size\align.py内

用于将两个目录的同名图像尺寸对齐一致，文件内包含函数size_align()也可用于批量对齐。

操作参数有：

-rpath 尺寸参考目录，输出图像尺寸将与此目录下图像一致

-ppath 对齐处理目录，此为欲处理的图片存在的目录

-opath 输出目录，最终对齐的图像将在此目录保存

示例：将位于E:\images2 内的图像调整致 E:\image1 中图像大小并保存致E:\image2\aligned 下
```
cd
python .\SimpleTools\Size\align.py -rpath E:\images1 -ppath E:\images2 -opath E:\image2\aligned
```

***
### Entropy - 求1维信息熵

位于.\SimpleTools\Entropy\1d_entropy.py内

用于计算图像的一维灰度信息熵，内含函数entropy()可用于计算单张图像一维灰度信息熵。

操作参数有：

-p 或 --path 欲计算熵的图片目录

-s 或 -save_path 计算结果保存的目录

-f 或 --format 计算结果保存的格式，目前支持txt(默认)与mat格式，mat格式方便Matlab读取

示例：计算位于E:\images1 内的图像的信息熵并将结果保存在E:\image1\Entropy 格式为.mat
```
cd
python .\SimpleTools\Entropy\1d_Entropy.py -p E:\image1  -s E:\image1\Entropy -f mat
```

将计算单张图片信息熵并计算均值，保存致txt文件时内容如：

```
"image1.png" : "0.00000"
"image2.png" : "0.00000"
"image3.png" : "0.00000"
Mean Entropy : 0.00000
```

保存致mat文件时内容为：

|名称|值|
|---|---|
|entropy|1x1 struct|
|mean_entropy|0.0000|

entropy 1x1 struct
|字段|值
|---|---
|image1.png|0.0000
|image2.png|0.0000
|image3.png|0.0000
