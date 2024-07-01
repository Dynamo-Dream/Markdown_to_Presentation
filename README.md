# Markdown to PowerPoint Converter

Welcome to the Markdown to PowerPoint Converter project! This tool is designed to seamlessly transform your Markdown notes into professional PowerPoint presentations, making it easier to share your ideas with the world.

## Project Overview

The Markdown to PowerPoint Converter is an innovative application that takes your Markdown-formatted notes and converts them into a visually appealing PowerPoint presentation. The tool is currently in the development stage, but it promises to simplify the process of creating presentations from textual notes.

### Key Features

- **Automatic Title Conversion**: Converts H1 tags in Markdown to the main titles in PowerPoint slides.
- **Structured Content**: Transforms H4 tags and arrow points into structured slide titles and bullet points.
- **Image Handling**: Processes images with H3 tags to include both the image and its caption in slides.
- **LaTeX Support**: Converts LaTeX equations into images, preserving the mathematical formatting in your presentation.

## Technology Stack

This project leverages a variety of powerful libraries and tools to achieve its functionality:

- **Markdown to HTML Conversion**: Utilizes Markdown libraries to convert Markdown text into HTML format.
- **HTML Parsing**: Employs Beautiful Soup to parse the HTML and extract relevant tags.
- **Image Processing**: Combines OpenCV and Pillow libraries to crop and create images for the PowerPoint slides.
- **Presentation Generation**: Uses Python-pptx to create and manipulate PowerPoint files.

### Libraries Used

- **Markdown**: For converting Markdown text to HTML.
- **Beautiful Soup**: For parsing HTML and extracting specific tags and content.
- **OpenCV**: For advanced image processing and manipulation.
- **Pillow**: For handling image operations such as cropping and resizing.
- **Python-pptx**: For creating and editing PowerPoint presentations.

## Workflow

1. **Markdown Parsing**: The input Markdown file is parsed and converted into HTML.
2. **HTML Extraction**: Beautiful Soup is used to extract relevant tags and content from the HTML.
3. **Content Conversion**:
    - H1 tags are converted to the main titles of slides.
    - H4 tags and arrow points are used to create structured titles and bullet points.
    - H3 tags associated with images are converted into slides with images and captions.
    - LaTeX equations are converted into images with captions using H3 tags.
4. **Image Processing**: OpenCV and Pillow are used to process images, ensuring they are properly formatted for PowerPoint.
5. **Presentation Creation**: The processed content is assembled into a PowerPoint presentation using Python-pptx.

## Example Outputs

Here are some example outputs to showcase what the converted PowerPoint slides look like:

<div align="center">
  <img src="images/example1.png" alt="Example 1" width="45%"/>
  <img src="images/example2.png" alt="Example 2" width="45%"/>
</div>
<div align="center">
  <img src="images/example3.png" alt="Example 3" width="45%"/>
  <img src="images/example4.png" alt="Example 4" width="45%"/>
</div>

## Future Plans

As the project progresses, we aim to add more features and improve the existing functionality. Stay tuned for updates!

---

*Made with ❤️ by [Anish Kumar](https://github.com/dynamo_dream)*


