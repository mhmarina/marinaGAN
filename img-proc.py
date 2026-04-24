from PIL import Image
import os

input_dir = "data-raw/"
output_dir = "data-preproc/"
raw_dir = "data-renamed"
os.makedirs(output_dir, exist_ok=True)

for i, filename in enumerate(os.listdir(input_dir)):
    print(filename, i)
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        img = Image.open(os.path.join(input_dir, filename))
        name = f"{i}.jpg"
        img.save(os.path.join(raw_dir, name))
        img = img.convert("L")          
        img = img.resize((64, 64), Image.LANCZOS)  
        img.save(os.path.join(output_dir, name))

print("Done!")