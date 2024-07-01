import matplotlib.pyplot as plt
import pdf2image
import cv2
from PIL import Image
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
def latex_to_image(latex_notation, output_path):
    fig = plt.figure()
    plt.axis('off')
    equation = fr'${latex_notation}$'
    plt.text(0.5, 0.5, equation, fontsize=24, ha='center', va='center')

    # Save the figure as an image
    plt.savefig('temp.pdf', bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

    image = pdf2image.convert_from_path('temp.pdf')
    image[0].save(output_path,'PNG')


# Example usage
latex_notation = r'\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}'
output_path = 'variance_formula.png'
img = cv2.imread('img.png')

latex_to_image(latex_notation, output_path)
image = Image.open('img.png')
image.show
cv2.imshow('img',img)

cv2.waitKey(0)

