import gradio as gr
from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_pretrained(
    "segmind/SSD-1B",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
)
pipe.to("cuda")


def generate_image(prompt, neg_prompt):
    image = pipe(
        prompt=prompt,
        negative_prompt=neg_prompt
    ).images[0]
    return image


prompt = gr.Text(
    label="Prompt",
    show_label=False,
    max_lines=2,
    placeholder="Enter Your Prompt",
    container=False
)

neg_prompt = gr.Text(
    label="Negative Prompt",
    show_label=False,
    max_lines=2,
    placeholder="Enter Your Negative Prompt",
    container=False
)

iface = gr.Interface(
    fn=generate_image,
    inputs=[prompt, neg_prompt],
    outputs="image",
    title="Text to Image Generator",
    examples=[
        ["A painting of a cute cat sitting on a chair", "ugly, blurry"],
        ["An astronaut riding a horse on mars", "poorly drawn"]
    ],
    allow_flagging=False
)

iface.launch(share=True)
