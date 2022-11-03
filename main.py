from Encoder import Encoder


def main():
    e = Encoder(0)

    data_path = 'resources/dummy.txt'
    image_path = 'resources/small_original.png'
    save_path = 'resources/small_edited.png'
    e.encode(data_path, image_path, save_path)

    image_path = 'resources/small_edited.png'
    save_path = 'resources/dummy_edited.txt'
    e.decode(image_path, save_path)


if __name__ == '__main__':
    main()
    # import os, psutil; print(f'Memory used: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} Mb')
