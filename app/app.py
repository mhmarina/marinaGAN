import gradio as gr
from model import Generator, Discriminator, nz
import torch
import torchvision.transforms.functional as tf

ngpu = 1
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")

netG = Generator(ngpu).to(device)
netD = Discriminator(ngpu).to(device)

# load model:
checkpoint = torch.load(f'../pickle/checkpoint.pth')
netG.load_state_dict(checkpoint['netG_state_dict'])
netD.load_state_dict(checkpoint['netD_state_dict'])

def generate():
    rand_noise = torch.randn(1, nz, 1, 1, device=device)

    with torch.no_grad():
        fake = netG(rand_noise).detach().cpu()
        fake = tf.to_pil_image(fake.squeeze()).resize((256,256))
        return gr.Image(fake)

demo = gr.Interface(
    fn= generate,
    inputs=None,
    outputs=["image"],
    api_name="generate_img"
)

demo.launch()