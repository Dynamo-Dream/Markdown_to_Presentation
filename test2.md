# Test1

CH
#### Test 4
- P1
- P2
- P3

CH

![[words-no-regrets-hand-written-on-purple-blue-night-foggy-window-glass-photo-transformed.jpeg]]
### No Regrets Image

CH

```python
import matplotlib.pyplot as plt
import pdf2image
def latex_to_image(latex_notation, output_path):
    fig, ax = plt.subplots()
    ax.axis('off')
    equation = fr'${latex_notation}$'
    ax.text(0.5, 0.5, equation, fontsize=24, ha='center', va='center')
    fig.tight_layout(pad=0)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    return
latex_notation = r'\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}'
output_path = 'variance_formula.png'
latex_to_image(latex_notation, output_path)
```

CH

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$
### NORMAL DISTRIBUTION PDF
CH


