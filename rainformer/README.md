ENGLISH | [简体中文](README_CN.md)

# Rainformer: Features Extraction Balanced Network for Radar-Based Precipitation Nowcasting

## Overview

Rainformer is a novel precipitation nowcasting framework, in which, two practical components are proposed: the global features extraction unit and the gate fusion unit (GFU). The former provides robust global features learning ability depending on the window-based multi-head self-attention (W-MSA) mechanism, while the latter provides a balanced fusion of local and global features. Rainformer has a simple yet efficient architecture and significantly improves the accuracy of rainfall prediction, especially on high-intensity rainfall. It offers a potential solution for real-world applications. 

![rainformer](images/architecture.JPG)

This tutorial introduces the research background and technical path of Rainformer, and shows how to train and fast infer the model through MindEarth.

More details can be found in the [original paper](https://ieeexplore.ieee.org/abstract/document/9743916)

## QuickStart

The dataset consists of precipitation maps in 5-minute intervals from 2016-2019 resulting in about 420,000 images.

The dataset is based on radar precipitation maps from [The Royal Netherlands Meteorological Institute (KNMI)](https://www.knmi.nl/over-het-knmi/about).

To download the dataset, please write an e-mail to [k.trebing@alumni.maastrichtuniversity.nl](k.trebing@alumni.maastrichtuniversity.nl) and [s.mehrkanoon@uu.nl](s.mehrkanoon@uu.nl) to get the link.

Please download the data to `./dataset`, and use `./dataset/create_dataset.py` to create the dataset.

### Run Option 1: Call main.py from command line

### Run Option 2: Run Jupyter Notebook

## Result

## Contributor

gitee id: bingzhi.li
email: bingzhi.li@zhejianglab.com
