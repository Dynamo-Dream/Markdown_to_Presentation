from PIL import Image,ImageDraw, ImageFont
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(path)

def get_text(text,input_path=os.path.join(path,'gradient.jpeg'),output_path=os.path.join(parent_path,'temp','temp.png'),font_size=150,font=os.path.join(parent_path,'font','arial.ttf')):
    image = Image.open(input_path)
    w,h = image.size
    font = ImageFont.truetype(font,font_size)

    # Create new alpha channel - solid black
    alpha = Image.new('L', (w,h))
    draw = ImageDraw.Draw(alpha)
    
    length = draw.textlength(text, font=font)
    draw.text((20,10),text,fill='white',font=font)
    # Use text cutout as alpha channel for gradient image
    
    image.putalpha(alpha)
    image.save(output_path)
    return output_path,length,font_size

if __name__ == "__main__":
    get_text("JHON CENA")