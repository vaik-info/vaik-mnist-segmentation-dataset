# vaik-mnist-segmentation-dataset

Create MNIST segmentation dataset

## Example

![Screenshot from 2023-03-02 11-04-34](https://user-images.githubusercontent.com/116471878/222312171-00fbcad5-a5a0-48d7-82e5-aae7059314d6.png)

![train_000000000_seg](https://user-images.githubusercontent.com/116471878/222312254-aa393fc7-f5c5-4c2f-953e-ba1cf15b757d.png)

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
background
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
        "background",
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
            0,
            0,
            0
        ],
        [
            1,
            1,
            1
        ],
        [
            2,
            2,
            2
        ],
        [
            3,
            3,
            3
        ],
        [
            4,
            4,
            4
        ],
        [
            5,
            5,
            5
        ],
        [
            6,
            6,
            6
        ],
        [
            7,
            7,
            7
        ],
        [
            8,
            8,
            8
        ],
        [
            9,
            9,
            9
        ],
        [
            10,
            10,
            10
        ]
    ]
}
```

- raw image and segmentation image for train and validation

![Screenshot from 2023-03-02 11-04-34](https://user-images.githubusercontent.com/116471878/222312171-00fbcad5-a5a0-48d7-82e5-aae7059314d6.png)
![Screenshot from 2023-03-02 11-05-02](https://user-images.githubusercontent.com/116471878/222312213-fe8ae23f-1da7-4b9a-957d-c807be4fa620.png)
