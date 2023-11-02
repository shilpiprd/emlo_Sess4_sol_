# Task
- Use the hyperparameters obtained in prevoius assignment optuna sweep (lr, batch_rate & optimizer) and train the cifar10 dataset. 
- convert ur model into Torch scripted module. 
- use gradio, take input from user and give top 10 outputs. 
- Update README and write instructions on how to use the demo. 
- dockerize the demo. 
- docker run -t -p 8080:8080 <image>:<tag> should start the webapp !
- push everythign to dockerHub and get the link. 

## Comments: 
- Removed all the optuna sweep parts. 
- Had to change configs/trainer/default.yaml accelator value from gpu to cpu. 
- Also, updated all files in the utils folder.
- Modified train.py file for logger. 
- Also modified mnist_module.py file inside src/models/ folder.
- Inside train.yaml, changed defaults to mnist for data and model.

### Integrating Demo Deployment into our PyTorch Lightning Template (Basically Using Gradio with Hydra Template)
- You'll have to first add gradio in requirements.txt file 
- Add demo.py file in src 
- Add demo.yaml file in configs 
- there should be a checkpoint with .ckpt extension in configs/logs/trainer ... but if there isn't then train the model and stop the evaluation early like after 2-3 epochs by doing : python3 src/train.py experiment=example 
- Then add the path of checkpoint in demo.yaml file so u wouldn't have to provide it manually.
- then u can finally run demo.py by doing : python3 src/demo.py experiment=example 


### Additions Made for Scripting with MNIST (in-video exercise)
- Modified mnist_module.py , imported libraries import torch.nn.functional as F  & from torchvision import transforms as T. Also added @torch.jit.export function. 
- Obtained a separate demo file and it's corresponding yaml file. demo_scripted.
- Also, forward_jit function defined in mnist_module.py isn't predefined. It can be given any name. Just make sure to use the following changes in demo_scripted.py as well. 
- Added lines 91-97 in train.py , not given in the required changes section in session4 Document.

### Additions done specifically for Session4 assignment (scripting & training on cifar10)
- I didn't have best parameters from optuna, so I'm still using random parameters. 
- Train the model fully using : python3 src/train.py experiment=cifar 
- Note: train.py has been changed here because of previous in-video run in scripting. (lines 91-97) 
- For scripted training, demo_scripted.py needs to be used by doing: ``python3 src/demo_scripted.py``. 
- Set defaults of model and data to cifar in train.yaml file. 
- Added lines 56-66 in src/model/cifar10_timm_module.py for scripting. 
- Had to modify the recognize_digit function in demo_scripted.py to accegt RGB and to not give canvas as source (since we needed to upload images rather than draw them). 

### Points to keep in mind
- Scripting is in general more bendable as compared to tracing. After tracing pytorch code, it's faster, but it might give you more errors in some situations. 
- if creation of docker image isn't working out, then make sure to modify the reuqirements.txt file. In this case i reduced torch packages to their cpu version, which considerably reduced the size. 
- Also, to get a link after running docker image, u gotta specify this line in the .py file : demo.launch(server_name="0.0.0.0", server_port=8080) 
- Further image size can be reduced if we remove some of the packages in the .txt file such as timm 
- To push the image, I tagged the image by doing: ``docker tag test_image:latest shilpi06/dockerizedandscripted:latest`` 
- And finally pushed it with the command: ``docker push shilpi06/dockerizedandscripted:latest`` 

### To run the image 
- To run the docker image and get output predictions, simply pull the image from dockerhub and run it . 
- On typing localhost:8080 on the webpage, you should be able to open gradio. 