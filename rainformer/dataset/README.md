# 数据预处理

原始数据集包含了2016年至2019年间5分钟间隔的雷达图。

为了预测短临降雨，首先需要将其中包含降雨事例的雷达图找出来。

使用`create_dataset.py`脚本对原始数据集进行预处理。

# 数据处理方法

脚本将找出降雨量大于阈值的雷达图。

阈值被定义为降雨总量的百分比。

如果一幅雷达图的降雨量超过阈值，则这张雷达图前面的（input_lenth+image_ahead）张雷达图将被保存为一个序列，作为最终的数据集用于训练和测试。

# 运行脚本

运行以下命令：

`python create_dataset.py --input_length 12 --image_ahead 6 --rain_amount_thresh 0.5`

- input_length        : 输入雷达图长度
- image_ahead         : 当前雷达图之前的雷达图长度
- rain_amount_thresh  : 阈值

# Why need to preprocess the dataset

The original dataset contains the radar maps in 5 mins from 2016 to 2019.

To predict the rain, we need first select the radar maps that contains the rain event.

To create such a dataset, we use the script `create_dataset.py` to preprocess the original dataset.

# How the script work

The script will find the radar map which above a threshold.

The threshold is defined as the percentage of the rain amount in a radar map.

If a radar map whose rain amount is larger than the threshold, the script will store (input_lenth+image_ahead) images before this rader map as a sequence for the later training and testing.

# Run the script

To do the preprocessing, just run the command following:

`python create_dataset.py --input_length 12 --image_ahead 6 --rain_amount_thresh 0.5`

- input_length        : lenth of input images
- image_ahead         : number of images ahead of the input images
- rain_amount_thresh  : percent of rain area threshold for the radar maps
