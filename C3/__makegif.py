import os
import imageio

def make_gif_from_jpgs():
    jpg_files = [f for f in os.listdir('.') if f.endswith('.jpg')]
    jpg_files.sort()

    images = []
    for jpg_file in jpg_files:
        with open(jpg_file, 'rb') as f:
            images.append(imageio.imread(f))

    gif_filename = '__output.gif'

    try:
        dur = float(input("Duration of each image:"))
    except:
        dur = 0.5
    imageio.mimsave(gif_filename, images, duration=dur)

    print(f'GIF saved as {gif_filename}')

if __name__ == "__main__":
    make_gif_from_jpgs()
