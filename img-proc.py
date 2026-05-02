from PIL import Image, ImageOps
import os

input_dir = "data-raw/"
output_dir = "data-preproc/portraits/"
# rename_dir = "data-rename/"
os.makedirs(output_dir, exist_ok=True)

for i, filename in enumerate(os.listdir(input_dir)):
    img = Image.open(os.path.join(input_dir, filename))
    name = f"{i}.jpg"
    # if(filename.endswith("png")):
    #     name = f"{i}.png"
    # img.save(os.path.join(rename_dir, name))
    img = img.convert("L")          
    img = img.resize((64, 64), Image.LANCZOS)  
    img.save(os.path.join(output_dir, name))
    # augment with horizontal flip
    flipped = ImageOps.mirror(img)
    flipped.save(os.path.join(output_dir, f"{i}_flip.jpg"))

print("Done!")