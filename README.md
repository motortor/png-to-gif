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

# 修改1（png_to_gif1.py）
![image](https://github.com/motortor/png-to-gif/blob/main/output1.gif)

为了确保每一帧之间不会有上一帧的残留，可以在创建每一帧时添加透明背景。这样可以避免前一帧的内容干扰下一帧。
关键改动点：
1. 创建一个全透明的背景图 transparent_background。
2. 在每一帧的图片上使用 transparent_background.copy() 以确保每一帧开始时都是全透明的。
3. 使用 paste 方法将实际图像粘贴到透明背景上，确保每帧都是独立的，不会受到前一帧的影响。
4. 在 save 方法中使用 disposal=2 参数，这样可以确保每一帧在显示之前都会清除之前的帧。

但是生成的GIF图案仍然存在出现黑边的问题。

