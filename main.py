import argparse
import os
import random
import shutil
import json
from PIL import Image
import numpy as np
import tensorflow as tf
from tqdm import tqdm

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


def get_classes_color(classes):
    colors = []
    for classes_index in range(len(classes)):
        colors.append([classes_index + 1, ] * 3)
    return colors


def crop_char_image(mnist_char_image):
    x_min, y_min, x_max, y_max = 0, 0, mnist_char_image.shape[1], mnist_char_image.shape[0]

    x_sum_mnist_char_image = np.sum(mnist_char_image, axis=0)
    y_sum_mnist_char_image = np.sum(mnist_char_image, axis=1)

    for i in range(x_sum_mnist_char_image.shape[0]):
        if x_sum_mnist_char_image[i] > 0:
            x_min = i
            break

    for i in range(y_sum_mnist_char_image.shape[0]):
        if y_sum_mnist_char_image[i] > 0:
            y_min = i
            break

    x_revert_sum_diff_bool_image = x_sum_mnist_char_image[::-1]
    y_revert_sum_diff_bool_image = y_sum_mnist_char_image[::-1]

    for i in range(x_revert_sum_diff_bool_image.shape[0]):
        if x_revert_sum_diff_bool_image[i] > 0:
            x_max = x_revert_sum_diff_bool_image.shape[0] - i
            break

    for i in range(y_revert_sum_diff_bool_image.shape[0]):
        if y_revert_sum_diff_bool_image[i] > 0:
            y_max = y_revert_sum_diff_bool_image.shape[0] - i
            break

    return mnist_char_image[y_min:y_max, x_min:x_max]


def write(output_sub_dir_path, sample_num, image_max_size, image_min_size, char_max_size, char_min_size, char_max_num,
          char_min_num, x, y, colors):
    os.makedirs(output_sub_dir_path, exist_ok=True)

    for file_index in tqdm(range(sample_num), desc=f'write at {output_sub_dir_path}'):
        canvas = np.zeros(
            (random.randint(image_min_size, image_max_size), random.randint(image_min_size, image_max_size), 3),
            dtype=np.uint8)
        segmentation_canvas = np.zeros(canvas.shape, dtype=canvas.dtype)
        for char_index in range(random.randint(char_min_num, char_max_num)):
            mnist_index = random.randint(0, y.shape[0] - 1)
            mnist_char_image = np.array(Image.fromarray(x[mnist_index]).resize(
                (random.randint(char_min_size, char_max_size), (random.randint(char_min_size, char_max_size)))))
            mnist_char_image = np.clip((mnist_char_image > 125) * 255, 0, 255)
            mnist_char_image = crop_char_image(mnist_char_image)
            mnist_color_char_image = np.zeros(mnist_char_image.shape + (3,), dtype=np.uint8)
            mnist_color_char_image[:, :, 0] = np.clip((mnist_char_image * random.uniform(0., 1.)).astype(np.uint8), 0,
                                                      255)
            mnist_color_char_image[:, :, 1] = np.clip((mnist_char_image * random.uniform(0., 1.)).astype(np.uint8), 0,
                                                      255)
            mnist_color_char_image[:, :, 2] = np.clip((mnist_char_image * random.uniform(0., 1.)).astype(np.uint8), 0,
                                                      255)
            mnist_segmentation_color_char_image = np.zeros(mnist_char_image.shape + (3,), dtype=np.uint8)
            mnist_segmentation_color_char_image[mnist_char_image > 0] = colors[y[mnist_index]]

            paste_start_x = random.randint(0, canvas.shape[1] - mnist_color_char_image.shape[1])
            paste_end_x = paste_start_x + mnist_color_char_image.shape[1]
            paste_start_y = random.randint(0, canvas.shape[0] - mnist_color_char_image.shape[0])
            paste_end_y = paste_start_y + mnist_color_char_image.shape[0]

            canvas[paste_start_y:paste_end_y, paste_start_x:paste_end_x, :][mnist_char_image > 0] = \
                mnist_color_char_image[mnist_char_image > 0]

            segmentation_canvas[paste_start_y:paste_end_y, paste_start_x:paste_end_x, :][mnist_char_image > 0] = \
                mnist_segmentation_color_char_image[mnist_char_image > 0]

        file_name = f'{os.path.basename(output_sub_dir_path)}_{file_index:09d}'

        output_raw_image_path = os.path.join(output_sub_dir_path, f'{file_name}_raw.jpg')
        Image.fromarray(canvas).save(output_raw_image_path, quality=100, subsampling=0)

        output_seg_image_path = os.path.join(output_sub_dir_path, f'{file_name}_seg.jpg')
        Image.fromarray(segmentation_canvas).save(output_seg_image_path, quality=100, subsampling=0)


def main(output_dir_path, train_sample_num, valid_sample_num, image_max_size, image_min_size, char_max_size,
         char_min_size, char_max_num, char_min_num):
    os.makedirs(output_dir_path, exist_ok=True)

    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    classes_txt_path = os.path.join(os.path.dirname(__file__), 'classes.txt')
    classes = []
    with open(classes_txt_path) as f:
        for line in f:
            classes.append(line.strip())
    colors = get_classes_color(classes)

    output_train_dir_path = os.path.join(output_dir_path, 'train')
    write(output_train_dir_path, train_sample_num, image_max_size, image_min_size, char_max_size, char_min_size,
          char_max_num, char_min_num, x_train, y_train, colors)

    output_valid_dir_path = os.path.join(output_dir_path, 'valid')
    write(output_valid_dir_path, valid_sample_num, image_max_size, image_min_size, char_max_size, char_min_size,
          char_max_num, char_min_num, x_test, y_test, colors)

    shutil.copy(classes_txt_path, os.path.join(output_dir_path, os.path.basename(classes_txt_path)))

    json_dict = {'classes': classes, 'colors': colors}
    with open(os.path.join(output_dir_path, 'classes.json'), 'w') as f:
        json.dump(json_dict, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--output_dir_path', type=str, default='~/.vaik-mnist-segmentation-dataset')
    parser.add_argument('--train_sample_num', type=int, default=100)
    parser.add_argument('--valid_sample_num', type=int, default=100)
    parser.add_argument('--image_max_size', type=int, default=768)
    parser.add_argument('--image_min_size', type=int, default=320)
    parser.add_argument('--char_max_size', type=int, default=192)
    parser.add_argument('--char_min_size', type=int, default=96)
    parser.add_argument('--char_max_num', type=int, default=6)
    parser.add_argument('--char_min_num', type=int, default=2)
    args = parser.parse_args()

    args.output_dir_path = os.path.expanduser(args.output_dir_path)

    main(**args.__dict__)
