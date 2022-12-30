import torch
import add as models
 
torch_model = torch.load("add.pth", map_location= 'cpu') 
#model = models.Net1(mode='val')
#model = models.Net1(size=(400,400))
model = models.Net1()
#model.load_state_dict(torch_model)
 
batch_size = 1
input_shape = (3, 1088,1920)   
 
# #set the model to inference mode
model.eval()
 
x = torch.randn(batch_size, *input_shape)  
dynamic_hw ={'input':{2:'H',3:'W'},
             'output':{2:'H',3:'W'},
        }
#args=(x)
export_onnx_file = "add.onnx"
torch.onnx.export(model,
                    x,
                    export_onnx_file,
                    opset_version=11,
                    do_constant_folding=True, 
                   input_names=["input"],
                    output_names=["output"],
                    #dynamic_axes=dynamic_hw
                    ) 
#                   dynamic_axes={"input":{0:"batch_size"},  # 批处理变量
#                                  "output":{0:"batch_size"}}
