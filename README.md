# vaik-mnist-segmentation-dataset

Create MNIST segmentation dataset

## Example

![vaik-mnist-segmentation-dataset](https://user-images.githubusercontent.com/116471878/221352632-56c1c7b7-adf9-476b-a4a1-c7569d6797fd.png)

## Usage

```shell
pip install -r requirements.txt
python main.py --output_dir_path ~/.vaik-mnist-segmentation-dataset \
                --train_sample_num 10000 \
                --valid_sample_num 100 \
                --image_max_size 768 \
                --image_min_size 256 \
                --char_max_size 128 \
                --char_min_size 64 \
                --char_max_num 6 \
                --char_min_num 2
```

## Output
- classes.txt

```text
zero
one
two
three
four
five
six
seven
eight
nine
```

- classes.json

```text
{
    "classes": [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ],
    "colors": [
        [
            255,
            0,
            0
        ],
        [
            255,
            153,
            0
        ],
        [
            203,
            255,
            0
        ],
        [
            51,
            255,
            0
        ],
        [
            0,
            255,
            102
        ],
        [
            0,
            255,
            255
        ],
        [
            0,
            102,
            255
        ],
        [
            50,
            0,
            255
        ],
        [
            204,
            0,
            255
        ],
        [
            255,
            0,
            152
        ]
    ]
}
```

- raw image and segmentation image for train and validation
  ![vaik-mnist-segmentation-dataset](https://user-images.githubusercontent.com/116471878/221352907-7551e3b2-9de8-4c10-a39c-f7d3237fbd88.png)
- ![vaik-mnist-segmentation-dataset](https://user-images.githubusercontent.com/116471878/221352632-56c1c7b7-adf9-476b-a4a1-c7569d6797fd.png)