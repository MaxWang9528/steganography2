import numpy as np
from PIL import Image
import random
import os


class Encoder:
    def __init__(self, seed):
        random.seed(seed)

    @staticmethod
    def get_bits_arr(data_path):
        bits_arr = []
        with open(data_path, 'rb') as f:
            data = f.read()
            byte_arr = list(data)
        for byte in byte_arr:
            bits = bin(byte)[2:].zfill(9)
            bits_arr.append(bits)
        return bits_arr

    # @staticmethod
    # def write_image(bits_arr):
    #     byte_arr = []
    #     for bits in bits_arr:
    #         byte = int(bits, 2)
    #         byte_arr.append(byte)
    #     immutable_byte_arr = bytes(bytearray(byte_arr))
    #     with open('resources/test.bin', 'wb') as f:
    #         f.write(immutable_byte_arr)

    @staticmethod
    def gen_bit_loc(n, b):
        used = {}
        locs = []
        while len(locs) < n:
            randint = random.randint(0, b - 1)
            if used.get(randint) is True:
                continue
            locs.append(randint)
            used[randint] = True
        locs = np.arange(0, 88)
        return locs

    @staticmethod
    def write_data(img_arr, bits_arr):
        width = len(img_arr[0])
        height = len(img_arr)
        flat = img_arr.flatten()
        bit_str = ''
        for bits in bits_arr:
            bit_str += bits
        print(flat)
        print(bit_str)
        locs = Encoder.gen_bit_loc(len(bit_str), len(flat))
        print(locs)

        for bit, i in enumerate(bit_str):
            subpixel = flat[locs[i]]
            if subpixel == 255 and bit == '0':
                subpixel = 254

            if subpixel // 2 * 2 == subpixel and bit == '1':            # if even and 1, change to odd
                subpixel += 1                                           # if even and 0, do nothing
            if subpixel // 2 * 2 != subpixel and bit == 0:              # if odd and 1, do nothing
                subpixel += 1                                           # if odd and 0, change to even

    @staticmethod
    def encode(data_path, image_path):
        img = Image.open(image_path)
        img_arr = np.asarray(img)
        bits_arr = Encoder.get_bits_arr(data_path)
        print(bits_arr)

        Encoder.write_data(img_arr, bits_arr)




