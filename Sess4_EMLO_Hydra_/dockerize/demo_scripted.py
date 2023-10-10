# import pyrootutils

# root = pyrootutils.setup_root(
#     search_from=__file__,
#     indicator=[".git", "pyproject.toml"],
#     pythonpath=True,
#     dotenv=True,
# )
import rootutils
rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

from typing import List, Tuple

import torch
import hydra
import gradio as gr
from omegaconf import DictConfig

from src import utils

import torch.nn.functional as F 
from torchvision import transforms as T

# log = utils.get_pylogger(__name__)
from src.utils import (
    RankedLogger,
    extras,
    get_metric_value,
    instantiate_callbacks,
    instantiate_loggers,
    log_hyperparameters,
    task_wrapper,
)

log = RankedLogger(__name__, rank_zero_only=True)

def demo(cfg: DictConfig) -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    assert cfg.ckpt_path

    log.info("Running Demo")

    log.info(f"Instantiating scripted model <{cfg.ckpt_path}>")
    model = torch.jit.load(cfg.ckpt_path)

    log.info(f"Loaded Model: {model}")

    def recognize_digit(image):
        if image is None:
            return None
        # image = torch.tensor(image[None, None, ...], dtype=torch.float32)
        image = T.ToTensor()(image).unsqueeze(0) #adding this for RGB
        preds = model.forward_jit(image)
        preds = preds[0].tolist()
        label = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
        return {label[i]: preds[i] for i in range(10)}
        # return {str(i): preds[i] for i in range(10)}

    # im = gr.Image(shape=(28, 28), image_mode="L", invert_colors=True, source="canvas")
    im = gr.Image(shape=(28, 28), image_mode="RGB", invert_colors=True)

    demo = gr.Interface(
        fn=recognize_digit,
        inputs=[im],
        outputs=[gr.Label(num_top_classes=10)],
        live=True,
    )

    demo.launch(share = True,
                server_port=8080) #added shrae=True to create an extra link 

@hydra.main(
    version_base="1.2", config_path="../configs", config_name="demo_scripted.yaml"
)
def main(cfg: DictConfig) -> None:
    demo(cfg)

if __name__ == "__main__":
    main()
