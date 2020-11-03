import argparse
import cv2
import pytesseract
import numpy as np

parser = argparse.ArgumentParser(
    description='A small script capable of recognizing two leading numbers in png files.')

parser.add_argument('--input', '-i', dest='input_file_path', default='file.png',
                    help='path to the target eps file')

parser.add_argument('--output', '-o', dest='output_file_path', default='file.txt',
                    help='Path to where the output file is to be created')

parser.add_argument('--verbose', '-v', dest='store_true', help='If set to true will print the text to the console')


def load_and_preprocess_img(input):
    img = cv2.imread(input, cv2.IMREAD_GRAYSCALE)  # Loading in grayscale for easier noise removal
    img = cv2.fastNlMeansDenoising(img, None, 13, 13, 7)
    img = cv2.threshold(img, 25, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # Threshold for removing background noise
    kernel = np.ones((5,5), np.float32) / 25
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    img = cv2.filter2D(img, -1, kernel) # https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
    img = cv2.filter2D(img, -1, sharpen_kernel) # Didn't change the accuracy TODO: Highlight the edges

    return img


def format_output(txt):
    output_arr = txt.replace("-", "").splitlines()
    output = ""
    for s in output_arr:
        # for i in range(0, len(string)):
        #     if i % 2 == 0 and i != 0:
        #         string = string[:i] + ' ' + string[i:]
        # output += string + "\r\n"
        output += ' '.join(s[i:i + 2] for i in range(0, len(s), 2)) + "\n"
    return output


def main():
    # 91% accuracy:
    # fastNlMeansDenoising(img, None, 13, 13, 7), threshold(img, 30, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # --oem 3 --psm 6 outputbase digits
    custom_config = r'--oem 3 --psm 6'
    args = parser.parse_args()
    img = load_and_preprocess_img(args.input_file_path)

    output = pytesseract.image_to_string(img, config=custom_config)
    print("Not Only Digits:\r\n" + output.replace("-", "").replace("F", "7").replace("f", "7"))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
