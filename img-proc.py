from PIL import Image
import os

input_dir = "data-raw/"
output_dir = "data-preproc/"
os.makedirs(output_dir, exist_ok=True)

for i, filename in enumerate(os.listdir(input_dir)):
    img = Image.open(os.path.join(input_dir, filename))
    name = f"{i}.jpg"
    img = img.convert("L")          
    img = img.resize((64, 64), Image.LANCZOS)  
    img.save(os.path.join(output_dir, name))

print("Done!")