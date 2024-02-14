import os
import ffmpeg
import json_handler
import verse_handler
from Fonts import Fonts

# Define paths and values
number_of_videos = 20
project_dir = os.getcwd().replace("\\", "/")

video_folder = f"{project_dir}/videos/nature"
audio_folder = f"{project_dir}/audio"
json_file = f"{project_dir}/sources/verses_data/movies_love_data.json"
fonts_dir = f"{project_dir}/sources/fonts"
output_folder = f"{project_dir}/customers"
text_source_font = f'{project_dir}/sources/MotionPicture.ttf'.replace(":/", "\:/")
image_file = f"{project_dir}/sources/logo.png"
customer_name = "your_name"
verse_text_image_path = f"{project_dir}/verse_images/{customer_name}"
fonts_paths = [f'{project_dir}/sources/fonts/All Things Pink.ttf', 
                f'{project_dir}/sources/fonts/AmaticSC-Bold.ttf',
                  f'{project_dir}/sources/fonts/charlotte.ttf', 
                f'{project_dir}/sources/fonts/Concetta Kalvani Signature.ttf',
                  f'{project_dir}/sources/fonts/Moon Flower Bold.ttf', 
                  f'{project_dir}/sources/fonts/Give It Your Heart.ttf',
                 
          ]
fonts_sizes = [80, 80, 80, 80, 85, 80]
fonts_maxcharsline = [20, 25, 20, 25, 25, 25]
# project_dir = os.getcwd()
# font_dir = "C:/Windows/Fonts"


if __name__ == "__main__":
    fonts = Fonts(fonts_paths, fonts_sizes, fonts_maxcharsline)

    # Create a file for estimated runtime calculation if it doesn't exist yet
    open(f"{project_dir}/runtime.pk", 'a').close()

    ffmpeg.create_videos(video_folder=video_folder, audio_folder=audio_folder, fonts=fonts, json_file=json_file,
                         fonts_dir=fonts_dir, output_folder=output_folder, text_source_font=text_source_font,
                         image_file=image_file, customer_name=customer_name, number_of_videos=number_of_videos)

