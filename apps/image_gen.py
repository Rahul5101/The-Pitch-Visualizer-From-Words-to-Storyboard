from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_images(prompts):
    images = []
    for prompt in prompts:
        image = pipe(prompt, num_inference_steps=30).images[0]

        filename = f"static/generated_{abs(hash(prompt)) % (10 ** 8)}.png"
        image.save(f"app/{filename}")
        images.append(filename)
    return images
