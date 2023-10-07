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

### Integrating Demo Deployment into our PyTorch Lightning Template (Basically Using Gradio with Hydra Template)
- You'll have to first add gradio in requirements.txt file 
- Add demo.py file in src 
- Add demo.yaml file in configs 
- there should be a checkpoint with .ckpt extension in configs/logs/trainer ... but if there isn't then train the model and stop the evaluation early like after 2-3 epochs by doing : python3 src/train.py experiment=example 
- then u can finally run demo.py by doing : python3 src/demo.py ckpt_path=(provideThePath) experiment=example 