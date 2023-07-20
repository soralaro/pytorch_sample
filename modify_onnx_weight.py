import onnx
import numpy as np
import struct
import re
import sys
# read onnx model.
onnx_model = onnx.load(sys.argv[1])
graph = onnx_model.graph
eplison = 0.000009

def check_string(re_exp, str):
    res = re.search(re_exp, str)
    if res:
        print(str)
        return True
    else:
        return False

for node in graph.node:
    if node.name in ['BatchNormalization_181']:
        eplison = node.attribute[0].f

for node in graph.initializer:
    #if check_string('*.*.bn.weight', node.name):
    if check_string('\.bn\.weight', node.name):
        f=''
        for i in range(node.dims[0]):
            f = f + 'f'
        value = np.array(struct.unpack(f, node.raw_data), dtype=np.float32)
        value = np.where(abs(value) > 0.00000001, value, eplison)
        value = struct.pack(f,*value)
        node.raw_data = value

onnx.checker.check_model(onnx_model)
onnx.save(onnx_model, sys.argv[2])

