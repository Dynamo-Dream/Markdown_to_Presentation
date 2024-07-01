import carbon
import asyncio
import os
#from get_grad_text import *
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
async def get_code_carbon(code,output_image_name):
    cb = carbon.Carbon()  # Create a Carbon instance
    opts = carbon.CarbonOptions(code=code,vertical_padding_px=0,horizontal_padding_px=0)  # Set the options for the image
    image = await cb.generate(opts)  # Generate the image
    await image.save(output_image_name)  # Save the image in png format

code = """import matplotlib.pyplot as plt
import pdf2image
import cv2
def latex_to_image(latex_notation, output_path):
    fig = plt.figure()
    plt.axis('off')
    equation = fr'${latex_notation}$'
    plt.text(0.5, 0.5, equation, fontsize=24, ha='center', va='center')

    # Save the figure as an image
    plt.savefig('temp.pdf', bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    image = pdf2image.convert_from_path('temp.pdf')
    image[0].save('img.path','PNG')


# Example usage
latex_notation = r'\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}'
output_path = 'variance_formula.png'
latex_to_image(latex_notation, output_path)
"""
asyncio.run(get_code_carbon(code,"main"))

