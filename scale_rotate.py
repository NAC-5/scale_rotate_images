#!/usr/bin/env python3

from PIL import Image
import os

input_dir = os.path.join(os.getcwd(), 'icons')
output_dir = os.path.join(os.getcwd(), 'icons_fixed')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.startswith('ic_'):
        file_path = os.path.join(input_dir, filename)
        new_filename = os.path.splitext(filename)[0] + '.png'
        new_file_path = os.path.join(output_dir, new_filename)

        with Image.open(file_path) as img:
            new_image = img.rotate(270).resize((128, 128)).convert("RGBA").save(new_file_path, "PNG")