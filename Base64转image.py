import base64
from io import BytesIO
from PIL import Image

# Base64编码的字符串
base64_str =""
base64_data = base64_str.split(",")[1]
# 解码Base64字符串并将其转换为图像
decoded_img = base64.b64decode(base64_data)

# 将图像数据读取到PIL Image对象中
img = Image.open(BytesIO(decoded_img))

# 显示图像（可选）
img.save("logo.png")
