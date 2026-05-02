import json, base64, os, glob
from PIL import Image
import io
import shutil

progress_path = "progress"
os.makedirs(progress_path, exist_ok=True)

# extract images from notebook
with open('../GAN.ipynb', 'r') as f:
    nb = json.load(f)

img_count = 0
for cell in nb['cells']:
    for output in cell.get('outputs', []):
        if output.get('output_type') == 'display_data':
            if 'image/png' in output.get('data', {}):
                # skip the first img
                if img_count != 0:
                    img_data = base64.b64decode(output['data']['image/png'])
                    img = Image.open(io.BytesIO(img_data))
                    img.save(f'{progress_path}/epoch_{img_count:03d}.png')
                img_count += 1

print(f"Extracted {img_count} images")

# stitch into gif
frames = [Image.open(f) for f in sorted(glob.glob('progress/*.png'))]
frames[0].save(
    'training_progress.gif',
    save_all=True,
    append_images=frames[1:],
    duration=200,  # ms per frame
    loop=0
)

print("GIF saved to training_progress.gif")
shutil.rmtree(progress_path)
