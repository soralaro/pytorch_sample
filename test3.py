import torch
import Net3 as models
 
torch_model = torch.load("net1.pth", map_location= 'cpu') 
#model = models.Net1(mode='val')
#model = models.Net1(size=(400,400))
model = models.Net1()
#model.load_state_dict(torch_model)
 
batch_size = 1
c=3
h=1080
w=1920
input_shape = (3, 1080,1920)   
 
# #set the model to inference mode
model.eval()
 
x = torch.randn(batch_size, *input_shape)  
size = torch.ones(2)  
size[0]=input_shape[1]
size[1]=input_shape[2]
dynamic_hw ={'input':{2:'H',3:'W'},
             'output':{2:'H',3:'W'},
        }
#size_t=(size_h,)
#size=torch.randint(size_w,size_t,dtype=torch.int32)
args=(x,size)
#args=(x)
export_onnx_file = "net3.onnx"
torch.onnx.export(model,
                    args,
                    export_onnx_file,
                    opset_version=11,
                    do_constant_folding=True, 
#                    input_names=["input","size"],
                   input_names=["input"],
                    output_names=["output"],
#                    dynamic_axes=dynamic_hw
                    ) 
#                   dynamic_axes={"input":{0:"batch_size"},  # 批处理变量
#                                  "output":{0:"batch_size"}}
