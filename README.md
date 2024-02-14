# Custom Video Creation Project

This project is designed to create custom videos using pre-existing images and audio, along with dynamically embedded texts in the images.

## Requirements

- Python 3.x
- ffmpeg
- Python Dependencies: `ffmpeg-python`, `Pillow`

## Installation

1. Clone this repository to your local machine:

```cmd
git clone https://github.com/your_username/custom_video_project.git
pip install ffmpeg-python Pillow\
```

## Usage
Place your video files in the videos/nature folder.
Place your audio files in the audio folder.
Ensure you have a JSON file with the required data at sources/verses_data/movies_love_data.json.
Ensure you have the necessary fonts in the sources/fonts folder.
Run the main.py script.

```python
python main.py
```

Custom videos will be generated in the customers folder.

## Configuration

- `number_of_videos`: Number of videos to generate.
- `project_dir`: Project directory.
- `video_folder`: Folder containing the video files.
- `audio_folder`: Folder containing the audio files.
- `json_file`: Path to the JSON file with verse data.
- `fonts_dir`: Directory containing the text fonts.
- `output_folder`: Output folder for the generated videos.
- `text_source_font`: Text font for the verses.
- `image_file`: Image file to embed in the videos.
- `customer_name`: Customer's name.
- `verse_text_image_path`: Path for text images.
- `fonts_paths`: Paths of the text fonts.
- `fonts_sizes`: Sizes of the text fonts.
- `fonts_maxcharsline`: Maximum number of characters per line for each font.


## Notes
Ensure you have ffmpeg tool installed and accessible in your system's PATH.
This project uses the ffmpeg-python package to interact with ffmpeg from Python.
It's assumed that the current directory is the project directory when running the script.