import argparse
from PIL import Image

parser = argparse.ArgumentParser(
    description='A small script capable of recognizing two leading numbers in png files.')

parser.add_argument('--input', '-i', dest='input_file_path', default='file.eps',
                    help='path to the target eps file')

parser.add_argument('--output', '-o', dest='output_file_path', default='file.png',
                    help='Path to where the output file is to be created')


def main():
    args = parser.parse_args()
    img = Image.open(args.input_file_path)
    fig = img.convert('RGBA')
    fig.save(args.output_file_path, loseless=True)


if __name__ == "__main__":
    main()
