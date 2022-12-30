export ASCEND_GLOBAL_LOG_LEVEL=1
export ASCEND_SLOG_PRINT_TO_STDOUT=1
#atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW --input_shape="input:1,3,1088,1920;size:2" --output=./model --output_type=FP32 --soc_version=Ascend310
#atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW  --input_shape_range="input:[1,3,1~1088,1~1920];size:[2]" --output=./model --output_type=FP32 --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310
#atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW  --input_shape="input:1,3,1088,1920" --output=./model --output_type=FP32 --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310
#atc --mode=0 --model=./power3.onnx --framework=5 --input_format=NCHW  --input_shape_range="input:[1,3,1~1088,1~1920]" --output=./model --output_type=FP32 --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310P3
atc --mode=0 --model=./add.onnx --framework=5 --input_format=NCHW  --input_shape_range="input:[1,3,1~2560,1~2560]" --output=./model --output_type=FP32 --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310
#atc --mode=0 --model=./power3.onnx --framework=5 --input_format=NCHW  --output=./model --output_type=FP32 --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310
#atc --mode=0 --model=./power3.onnx --framework=5 --input_format=NCHW  --input_shape_range="input:[1,3,1~1088,1~1920]" --output=./model --output_type=FP32  --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310
#atc --mode=1 --om=./model.om --json=./resize2.json 
#atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW  --input_shape="input:1,3,1088,1920" --output=./model --output_type=FP32 --insert_op_conf=./dynamic_op.cfg --soc_version=Ascend310
#atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW  --input_shape="input:1,3,1088,1920;size:2" --output=./model --output_type=FP32 --soc_version=Ascend310
#atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW  --input_shape_range="input:[1,3,1~1088,1~1920]" --output=./model --output_type=FP32  --soc_version=Ascend310
#atc --mode=0 --model=./Conv.onnx --framework=5 --input_format=NCHW  --input_shape="X:1,2,4,4;W:2,2,3,3;B:2"  --output=./model --output_type=FP32 --soc_version=Ascend310
