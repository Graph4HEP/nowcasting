# Copyright 2023 Huawei Technologies Co., Ltd
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
"""loss functions for rainformer"""

import mindspore
from mindspore import nn
import mindspore.ops as ops

class BMAEloss(nn.Cell):
    r"""
    Rainformer loss cell
    """
    def __init__(self):
        super(BMAEloss, self).__init__()
        self.where = ops.Where()
        self.greater_equal = ops.GreaterEqual()
        self.less = ops.Less()
        self.abs = ops.Abs()
        self.sum = ops.ReduceSum()

    def fundFlag(self, a, n, m):
        flag_1 = self.greater_equal(a, n)
        flag_2 = self.less(a, m)
        flag_3 = self.where(self.where(flag_1, 1, 0), flag_2, 1)
        return flag_3 == 2

    def forward(self, pred, y):
        mask = mindspore.Tensor(mindspore.Tensor(y.shape), mindspore.float32)
        mask.fill_(0)
        mask = self.where(self.less(y, 2), mask, 1)
        mask = self.where(self.fundFlag(y, 2, 5), mask, 2)
        mask = self.where(self.fundFlag(y, 5, 10), mask, 5)
        mask = self.where(self.fundFlag(y, 10, 30), mask, 10)
        mask = self.where(self.greater_equal(y, 30), mask, 30)
        diff = self.abs(y - pred) * mask
        loss = self.sum(diff) / mindspore.Tensor(diff.shape).prod()
        return loss
