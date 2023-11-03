# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
'''
rainformer train and test
'''

import argparse
import time

def get_args():
    """Get user specified parameters."""
    parser = argparse.ArgumentParser(description='Rainformer')
    parser.add_argument('--config_file_path', type=str, default='./Rainformer.yaml')
    parser.add_argument('--device_target', '-d', type=str, choices=["Ascend", "GPU"], default="Ascend")
    parser.add_argument('--device_id', type=int, default=0)
    parser.add_argument('--distribute', type=bool, default=False)
    parser.add_argument('--rank_size', type=int, default=1)
    parser.add_argument('--amp_level', type=str, default='O2')
    parser.add_argument('--run_mode', type=str, choices=["train", "test"], default='train')
    parser.add_argument('--load_ckpt', type=bool, default=False)

    parser.add_argument('--num_workers', type=int, default=1)

    parser.add_argument('--eval_interval', type=int, default=10)
    parser.add_argument('--keep_checkpoint_max', type=int, default=1)
    parser.add_argument('--output_dir', type=str, default='./summary')
    parser.add_argument('--ckpt_path', type=str, default='')

    params = parser.parse_args()
    return params

