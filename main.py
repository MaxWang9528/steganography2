from Encoder import Encoder
from PIL import Image
import numpy as np

def main():
    e = Encoder(0)

    # data_path = 'resources/dummy.txt'
    # image_path = 'resources/big_original.png'
    # save_path = 'resources/big_edited.png'
    # e.encode(data_path, image_path, save_path)

    image_path = 'resources/big_edited.png'
    save_path = 'resources/james.txt'
    bit_str_len = 189
    e.decode(image_path, save_path, bit_str_len)


if __name__ == '__main__':
    # main()
    # import os, psutil; print(f'Memory used: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} Mb')
    img1 = Image.open('resources/big_original.png')
    img2 = Image.open('resources/big_edited.png')

    print(np.asarray(img1))
    print()
    print(np.asarray(img2))
