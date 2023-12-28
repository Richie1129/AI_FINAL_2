from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, output_image_path, text):
    # 打開圖片
    image = Image.open(input_image_path)

    # 建立一個可以在圖片上繪製的物件
    draw = ImageDraw.Draw(image)

    # 使用 TrueType 字型
    font = ImageFont.load_default()  # 使用默認字型，你也可以換成其他字型
    font_size = 500

    # 設定文字位置（這裡是放在左上角，你可以根據需要調整）
    text_position = (50, 50)

    # 設定文字顏色
    text_color = (0, 0, 0)  # 黑色

    # 在圖片上繪製文字
    draw.text(text_position, text, font=font, fill=text_color,font_size=font_size)

    # 儲存修改後的圖片
    image.save(output_image_path)

if __name__ == "__main__":
    input_path = "C:/人工智慧期末linbot/lotus1.png"
    output_path = "C:/人工智慧期末linbot/lotus1_txt.png"
    text_to_add = "星期一要記得吃藥喔"

    add_text_to_image(input_path, output_path, text_to_add)
