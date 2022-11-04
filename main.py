from Encoder import Encoder
from PIL import Image
import numpy as np


def main():
    e = Encoder(0)

    # data_path = 'resources/aild.txt'
    # image_path = 'resources/4k.png'
    # save_path = 'resources/4k_edited.png'
    # e.encode(data_path, image_path, save_path)

    image_path = 'resources/4k_edited.png'
    save_path = 'resources/aild_edited.txt'
    bit_str_len = 2808954
    e.decode(image_path, save_path, bit_str_len)


if __name__ == '__main__':
    main()
    # import os, psutil; print(f'Memory used: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} Mb')
    # img1 = Image.open('resources/small_original.png')
    # img2 = Image.open('resources/small_edited.png')
    #
    # print(np.asarray(img1).flatten())
    # print()
    # print(np.asarray(img2).flatten())

