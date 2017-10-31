# AutoPython
自动裁剪图集工具。

在浏览器上抓取一些小的网络游戏的图片资源的时候，一般会抓到 `.png`图集文件和同名的图集信息文件（`.json`、 `.xml`、 `.html`）这些文件一般包含了图集中每个icon的名字、位置、大小等，运用该脚本可实现图集的快速裁剪，拿到每一个独立的icon。


![](https://github.com/zwp/AutoPython/blob/master/auto_slice.gif)

## 脚本运行环境

1、安装 `Python 3`；

2、`Python 3` 安装图片处理框架 `Pillow`，可参考脚本文件注释。


## 使用步骤

1、将该[脚本](https://github.com/zwp/AutoPython/blob/master/iconSlice/assets_slice.py)下载，并拷贝到一个新建文件夹下；

2、将图集文件.png 和同名的图集信息文件拷贝到该文件夹下；

3、核对脚本文件中的关键字是否和你的图集信息的关键字匹配；

4、终端 `cd` 到该文件夹下，运行 `python3 assets_slice.py`。
