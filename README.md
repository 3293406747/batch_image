# batch_image

## 项目说明

图片批量处理脚本目前只实现了**图片批量剪切**功能。

## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：
```
pip3 install -r requirements.txt
```

## 项目使用

- 第一步：实例化CutImage对象。
```
ci = CutImage()
```
- 第二步：解析一张图片，传入文件所在路径。
```
ci.add("img/ys1.png")
```
- 第二步：或图片批量解析，解析文件夹中的所有图片，传入文件夹所在路径。
```
ci.parse("img")
```
- 第三步：剪切并保存图片，传入需要剪切的位置左上角坐标和右下角坐标。
ci.w为图片原始宽度，ci.h为图片原始高度。
```
ci.handle(0, 98, ci.w, ci.h)
```
- 图片尺寸定位，传入文件所在路径。
```
ci.get_position("img/ys1.png")
```

