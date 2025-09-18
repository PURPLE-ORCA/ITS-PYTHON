from rembg import remove
from PIL import Image
import io

def remove_bg(input_path, output_path):
    with open(input_path, 'rb') as i:
        input_data = i.read()

    output_data = remove(input_data)

    with open(output_path, 'wb') as o:
        o.write(output_data)

    print(f"✅ Background removed and saved to: {output_path}")

remove_bg('input.png', 'output.png')