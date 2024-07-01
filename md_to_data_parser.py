import bs4
from bs4 import BeautifulSoup
import markdown
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_to_image.adding_text_on_image import *
from data_to_image.carbon_image import *
from data_to_image.crop_image import *
from data_to_image.latex_image import *
path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(path)

BACKGROUND_TEXT_PATH = os.path.join(path,'data_to_image','text_background.jpg')
OUTPUT_TEXT_IMAGE_PATH = os.path.join(path,'temp','temp.png')
OUTPUT_IMAGE_PATH = os.path.join(path,'final')
print(BACKGROUND_TEXT_PATH, OUTPUT_IMAGE_PATH,OUTPUT_TEXT_IMAGE_PATH)
import asyncio
def md_parser(md_path):
    
    with open (md_path,'rb') as fp:
        md = fp.read().decode('utf-8')

    data = markdown.markdown(md)
    html = BeautifulSoup(data,'html.parser')
    print(html)

    dict = {}
    count = 1
    list = []
    for tag in html.find_all():
        text = tag.get_text()
        if tag.name == 'h1':
            dict[count] = {
                "h1":text
            }
            count+=1
            header_on_image(text,background_image_path=BACKGROUND_TEXT_PATH,output_header_path=OUTPUT_IMAGE_PATH+"\count1.png")

        if tag.name == 'h4':
            li = tag.find_next('ul').find_all('li')
            list = [l.text for l in li]

            dict[count] = {
                "h2":{
                    "heading":text,
                    "points":list
                }
            }
            count+=1
            print("################################################################################################################")
            title_and_points_on_image(text,points=list,background_path=BACKGROUND_TEXT_PATH,output_image_path=OUTPUT_IMAGE_PATH+"\count2.png")
        if tag.name == 'p' and text.startswith('![[') and text.endswith(']]'):
            name = tag.find_next('h3')
            
            dict[count] = {
                "image":{
                    'path':text[3:-2],
                    'caption':name.get_text()
                }
            }
            count+=1
        
        if tag.name == 'p':
            code_tag = tag.find('code')
            if code_tag:
                code_content = code_tag.get_text()
                code_content ='\n'.join(line for line in code_content.splitlines() if line != 'python')

                dict[count] = {
                    "code": code_content
                }
                count += 1
                print(code_content)
                asyncio.run(get_code_carbon(code_content,OUTPUT_TEXT_IMAGE_PATH[:-4]))
                crop_image(input_image_path=OUTPUT_TEXT_IMAGE_PATH,output_image_path=OUTPUT_TEXT_IMAGE_PATH,code=True)
                overlay_image(main_image_path=os.path.join(path,'background.png'),overlay_image_path=OUTPUT_TEXT_IMAGE_PATH,output_image_path=OUTPUT_IMAGE_PATH+"\count3.png")

        if tag.name == 'p' and text.startswith('$$') and text.endswith('$$'):
            name = tag.find_next('h3')
            dict[count] = {
                "latex":{
                    'formula':text[2:-2],
                    'caption':name.get_text()
                }
            }
            count+=1

            latex_to_image(text[2:-2],OUTPUT_TEXT_IMAGE_PATH[:-5]+"q.png")
            crop_image(input_image_path=OUTPUT_TEXT_IMAGE_PATH[:-5]+"q.png",output_image_path=OUTPUT_TEXT_IMAGE_PATH)
            overlay_image(main_image_path=os.path.join(path,'background.png'),overlay_image_path=OUTPUT_TEXT_IMAGE_PATH,output_image_path=OUTPUT_IMAGE_PATH+"\count4.png")
        
    return dict
        
if __name__ == "__main__":
    md_parser(os.path.join(path,"test2.md"))