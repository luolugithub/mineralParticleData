## Description
This project major to work with instance or semantic segmentation dataset process
- split files in specify ratio with range 0-1
- annotation to instance/semantic dataset, coco,voc ...
## Requirements

- Ubuntu / macOS / Windows
- Python3.8


## Installation
- requirements.txt

## Usage
configure param:
- div_ratio  "specify ratio [train, val, test], train + val + test == 1.0"
- file_path  "file all, example: *.png and *.json ..."
- type_file
- dst_path  "target output path with train val test"

Run `python split_files_with_ratio.py`.  
The annotations file and png/jpg/.. image file in same dir.

Run `python labelme2coco.py -h`.  
Run `python labelme2voc.py -h`.  