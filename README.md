# vaik-mnist-segmentation-dataset

Create MNIST segmentation dataset

## Example

![Screenshot from 2023-03-02 10-24-54](https://user-images.githubusercontent.com/116471878/222306913-b40cec5f-c061-48e0-aaac-ed227b298f68.png)

![train_000000005_seg](https://user-images.githubusercontent.com/116471878/222306870-9a48d3b0-c211-470f-9a99-29a78321a17d.jpg)

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

![Screenshot from 2023-03-02 10-24-54](https://user-images.githubusercontent.com/116471878/222306913-b40cec5f-c061-48e0-aaac-ed227b298f68.png)
![Screenshot from 2023-03-02 10-30-56](https://user-images.githubusercontent.com/116471878/222307625-0284e290-1f0f-40f4-83cc-49bdc1693338.png)
