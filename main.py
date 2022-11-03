from Encoder import Encoder


def main():
    data_path = 'resources/dummy.txt'
    image_path = 'resources/small_original.png'

    e = Encoder(0)
    e.encode(data_path, image_path)


if __name__ == '__main__':
    main()
    # import os, psutil; print(f'Memory used: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} Mb')
