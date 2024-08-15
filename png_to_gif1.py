from PIL import Image
import os

def create_gif_from_images(folder_path, output_path, duration):
    # 获取文件夹中的所有PNG文件
    images = [img for img in os.listdir(folder_path) if img.endswith(".png")]
    images.sort()  # 确保按文件名排序
    frames = []

    # 获取第一张图片的尺寸
    first_image_path = os.path.join(folder_path, images[0])
    first_image = Image.open(first_image_path)
    width, height = first_image.size

    # 创建一个全透明的背景
    transparent_background = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # 打开所有图片并添加到frames列表
    for image in images:
        img_path = os.path.join(folder_path, image)
        img = Image.open(img_path).convert("RGBA")
        frame = transparent_background.copy()
        frame.paste(img, (0, 0), img)
        frames.append(frame)

    # 将frames列表中的图片保存为GIF
    if frames:
        frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=duration, loop=0, disposal=2)
    else:
        print("No PNG images found in the folder.")

# 设置文件夹路径和输出GIF文件路径
folder_path = "button"
output_path = "output1.gif"
duration = 40  # 0.04秒 = 40毫秒

# 调用函数生成GIF
create_gif_from_images(folder_path, output_path, duration)
