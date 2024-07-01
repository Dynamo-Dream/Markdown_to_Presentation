from PIL import Image,ImageDraw, ImageFont
import os
#from get_grad_text import *
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(path)
print(parent_dir)

background_image_path = os.path.join(path,'text_background.jpg')
output_header_path = os.path.join(parent_dir,'temp')
font_path = os.path.join(parent_dir,'font','arial.ttf')

def get_text(text,input_path=os.path.join(path,'gradient.jpeg'),output_path=os.path.join(parent_dir,'temp','temp.png'),font_size=150,font=os.path.join(parent_dir,'font','arial.ttf')):
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

def header_on_image(text,background_image_path,output_header_path):
    pverlay_path,length,font_size = get_text(text)
    image = Image.open(background_image_path)
    w,h = image.size
    text_image = Image.open(pverlay_path)
    image.paste(text_image, mask=text_image,box=(int((w-length)/2),int((h-font_size)/2)))
    image.save(output_header_path)

def title_and_points_on_image(header_text = "Text",points = [],background_path='bg4.jpg',output_image_path='temp.png',font_size_header=100,font_size_points = 60):
    image = Image.open(background_path)
    w,h = image.size
    overlay_path, length, font_size_header = get_text(header_text,font_size=100)
    text_image = Image.open(overlay_path)
    coordinates = (50,50)
    image.paste(text_image, mask=text_image,box=coordinates)
    fnt = ImageFont.truetype(os.path.join(parent_dir,'font','arial.ttf'), font_size_points)
    d = ImageDraw.Draw(image)
    new_y = coordinates[1]+font_size_header+60
    for i,point in enumerate(points):
        if i==0:
            d.text((coordinates[0]+50,new_y), point, font=fnt, fill=(255, 255, 255, 128))
        else:
            d.text((coordinates[0]+50,new_y), point, font=fnt, fill=(255, 255, 255, 128))
        new_y+=100
    image.save(output_image_path)

if __name__ == "__main__":
    header_on_image("ANISH KUMAR",background_image_path,os.path.join(output_header_path,'temp1.png'))
    title_and_points_on_image("ANISH KUMAR", points = ["This is Me","This is not how it gonna be"],background_path=background_image_path, output_image_path=os.path.join(output_header_path,'temp2.png'))

# get_text("This is a header type",font_size=100)
# title_and_points_on_image(points=["This is First POint","This is Second Point","This is THird POint"])
def resize_image_to_fit(overlay_image, main_width, main_height, padding):
    overlay_width, overlay_height = overlay_image.size
    
    # Calculate the maximum allowed width and height for the overlay image with padding
    max_width = main_width - 4 * padding
    max_height = main_height - 2 * padding
    
    # Calculate the scaling factor to resize the overlay image
    scale_factor = min(max_width / overlay_width, max_height / overlay_height)
    
    # Resize the overlay image
    new_width = int(overlay_width * scale_factor)
    new_height = int(overlay_height * scale_factor)
    resized_overlay = overlay_image.resize((new_width, new_height))
    
    return resized_overlay
def overlay_image(main_image_path, overlay_image_path, output_image_path,caption = "", padding = 10):
    # Open the main image and overlay image
    main_image = Image.open(main_image_path)
    overlay_image = Image.open(overlay_image_path)
    
    # Calculate the position to paste the overlay image
    main_width, main_height = main_image.size
    overlay_width, overlay_height = overlay_image.size
    
    # Ensure the overlay image fits within the main image considering padding
    if overlay_width + 2 * padding > main_width or overlay_height + 2 * padding > main_height:
        overlay_image = resize_image_to_fit(overlay_image, main_width, main_height, padding)
        overlay_width, overlay_height = overlay_image.size
        #raise ValueError("Overlay image with padding is larger than the main image")

    position_x = (main_width - overlay_width) // 2
    position_y = (main_height - overlay_height) // 2
    
    # Calculate coordinates to place the overlay image with padding
    position_x = max(position_x, padding)
    position_y = max(position_y, padding)
    
    # Paste the overlay image onto the main image
    main_image.paste(overlay_image, (position_x, position_y))
    fnt = ImageFont.truetype("arial.ttf", 20)
    d = ImageDraw.Draw(main_image)
    if caption:
        d.text((position_x,position_y+overlay_height+20), caption, font=fnt, fill=(0, 0, 0, 128))
    
    # Save the result
    main_image.save(output_image_path)

# # Example usage
# main_image_path = 'white_overlayed.jpg'
# overlay_image_path = 'cropped_variance_formula.png'
# output_image_path = 'final.jpg'
# padding = 10

# overlay_image(main_image_path, overlay_image_path, output_image_path, padding)