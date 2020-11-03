import argparse
import os
from PIL import Image


def convert_img(input, output):
    img = Image.open(input)
    fig = img.convert('RGBA')
    fig.save(output, loseless=True)


def convert_all_in_folder(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.eps'):
            convert_img(os.path.join(input_dir, filename), os.path.join(output_dir, filename.replace('.eps', '.png')))


def main():
    args = parser.parse_args()
    if args.input_file_path is not None and args.output_file_path is not None:
        convert_img(args.input_file_path, args.output_file_path)
    elif args.input_dir_path is not None and args.output_dir_path is not None:
        convert_all_in_folder(args.input_dir_path, args.output_dir_path)
    else:
        print("You must provide either input file path and output file path or input directory path and output "
              "directory path")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A small script capable of recognizing two leading numbers in png files.')

    parser.add_argument('--input', '-i', dest='input_file_path',
                        help='path to the target eps file')

    parser.add_argument('--input-dir', '-idir', dest='input_dir_path', help='path to the folder with eps files')

    parser.add_argument('--output', '-o', dest='output_file_path',
                        help='Path to where the output file is to be created')

    parser.add_argument('--output-dir', '-odir', dest='output_dir_path', help='path to the output folder')
    main()
