# png-to-gif
这是一个能将一组PNG图片转成GIF文件的脚本

这里以能变大变小的“动态按钮”为例，并设置每帧的显示时间为0.04秒。
首先，将需要转换成gif的png图片按顺序排列好，放入“button”文件夹。
如果还没有安装Pillow库，可以使用以下命令进行安装：
```python
pip install Pillow
```

在如下代码中，请将 folder_path 设置为你的PNG图片所在的文件夹路径，并将 output_path 设置为你希望保存GIF文件的路径。
运行此脚本后，程序将读取文件夹中的所有PNG文件，并将它们合并成一个GIF动画，设置每帧的显示时间为0.04秒（40毫秒）。
```python
# 设置文件夹路径和输出GIF文件路径
folder_path = "path_to_your_folder"
output_path = "output.gif"
duration = 40  # 0.04秒 = 40毫秒
```

# 错误示范（wrong.py）
![image](https://github.com/motortor/png-to-gif/blob/main/wrong.gif)
在wrong.py代码中，生成的GIF出现上一帧残留的问题。
具体原因是，在GIF动画中，每一帧默认会叠加在前一帧的图像上，而不会自动清除前一帧的内容，除非明确指定要清除或替换前一帧的内容。
所以接下来需要对这个问题进行修改。


