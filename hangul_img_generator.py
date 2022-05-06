import io
import os
import re
import glob

import pandas as pd
from PIL import Image, ImageFont, ImageDraw

class Generator:
    def __init__(self):
        self.SYLLABLE_LIST_PATH = './data/common-hangul-syllable.txt'
        self.FONT_LIST = glob.glob(os.path.join('./font', '*.ttf'))
        self.IMAGE_WIDTH = 48
        self.IMAGE_HEIGHT = 48
        self.is_gen = False
        
    def gen_img(self):        
        with io.open(self.SYLLABLE_LIST_PATH, 'r', encoding='utf-8') as f:
            syllable_list = f.read().splitlines()

        total_cnt = 0
        for syllable in syllable_list:
            for idx, font in enumerate(self.FONT_LIST):
                image = Image.new('L', (self.IMAGE_WIDTH, self.IMAGE_HEIGHT), color=0)
                font = ImageFont.truetype(font, 32)
                drawing = ImageDraw.Draw(image)
                w, h = drawing.textsize(syllable, font=font)
                drawing.text(
                    ((self.IMAGE_WIDTH-w)/2, (self.IMAGE_HEIGHT-h)/2),
                    syllable,
                    fill=(255),
                    font=font
                )
                image.save(f'./data/{syllable}_{idx}.jpeg', 'JPEG')
                print(f'✅ {total_cnt+1} img generated.')
                total_cnt += 1
        self.is_gen = True
        
    def link_csv(self):
        if self.is_gen:
            dataset = glob.glob(os.path.join('./data', '*.jpeg'))
            regex = re.compile('([가-힣])')
            dict_to_csv = {
                'path': dataset,
                'label': [regex.findall(dataset[i])[0] for i in range(dataset.__len__())]
            }
            pd.DataFrame(dict_to_csv).to_csv('train.csv', index=False)
        else:
            print('❎ Please run \'gen_img()\' first.')
