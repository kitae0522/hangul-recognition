import io
import os
import glob

from PIL import Image, ImageFont, ImageDraw

SYLLABLE_LIST_PATH = './data/common-hangul-syllable.txt'

font_list = glob.glob(os.path.join('./font', '*.ttf'))
with io.open(SYLLABLE_LIST_PATH, 'r', encoding='utf-8') as f:
    syllable_list = f.read().splitlines()

IMAGE_WIDTH, IMAGE_HEIGHT = (32, 32)

total_cnt = 0
for syllable in syllable_list:
    for idx, font in enumerate(font_list):
        image = Image.new('L', (IMAGE_WIDTH, IMAGE_HEIGHT), color=0)
        font = ImageFont.truetype(font, 22)
        drawing = ImageDraw.Draw(image)
        w, h = drawing.textsize(syllable, font=font)
        drawing.text(
            ((IMAGE_WIDTH-w)/2, (IMAGE_HEIGHT-h)/2),
            syllable,
            fill=(255),
            font=font
        )
        image.save(f'./data/{syllable}_{idx}.jpeg', 'JPEG')
        print(f'✅ {total_cnt+1} img generated.')
        total_cnt += 1