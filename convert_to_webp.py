from PIL import Image
import os

input_folder = 'input_imgs/'
output_folder = 'output_imgs/'

for file_name in os.listdir(input_folder):
    if file_name.endswith('.png') or file_name.endswith('.jpg'):

        with Image.open(os.path.join(input_folder, file_name)) as img:
            
            if img.mode == 'RGBA':
                background = Image.new('RGBA', img.size, (255, 255, 255, 0))
                background.paste(img, mask=img.split()[3])
            else:
                img = img.convert('RGB')

            img.save(os.path.join(output_folder, os.path.splitext(file_name)[0] + '.webp'), 'webp', lossless=False, quality=80)

print('Conversion completada')