export ASCEND_GLOBAL_LOG_LEVEL=0
export ASCEND_SLOG_PRINT_TO_STDOUT=1
atc --mode=0 --model=./net3.onnx --framework=5 --input_format=NCHW --input_shape="input:1,3,1088,1920" --insert_op_conf=./insert_op_lk.cfg --output=./model --output_type=FP32 --soc_version=Ascend310
#atc --mode=0 --model=./Conv.onnx --framework=5 --input_format=NCHW  --input_shape="X:1,2,4,4;W:2,2,3,3;B:2"  --output=./model --output_type=FP32 --soc_version=Ascend310
