from flask import Flask, request, render_template, send_file, session
from PIL import Image
import numpy as np
import os
import random

app = Flask(__name__)
app.secret_key = 'secret_key_to_use_sessions'  

UPLOAD_FOLDER = 'uploads'
ENCRYPTED_FOLDER = 'encrypted'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)

KEY = 12345

def swap_pixels(pixels, key):
    flat = pixels.reshape(-1, 3)
    random.seed(key)
    idx = list(range(len(flat)))
    random.shuffle(idx)
    return flat[idx].reshape(pixels.shape)

def reverse_swap_pixels(pixels, key):
    flat = pixels.reshape(-1, 3)
    random.seed(key)
    idx = list(range(len(flat)))
    shuffled = idx[:]
    random.shuffle(shuffled)
    reverse_idx = np.argsort(shuffled)
    return flat[reverse_idx].reshape(pixels.shape)

def encrypt_image(img):
    pixels = np.array(img)
    swapped = swap_pixels(pixels, KEY)
    encrypted = np.bitwise_xor(swapped, 127).astype('uint8')
    return Image.fromarray(encrypted)

def decrypt_image(img):
    pixels = np.array(img)
    xor_reversed = np.bitwise_xor(pixels, 127).astype('uint8')
    original = reverse_swap_pixels(xor_reversed, KEY)
    return Image.fromarray(original)


@app.route('/', methods=['GET', 'POST'])
def index():

    encrypted_history = get_file_list(ENCRYPTED_FOLDER)
    decrypted_history = get_file_list(ENCRYPTED_FOLDER)

    encrypted_filename = decrypted_filename = None

    if request.method == 'POST':
        action = request.form['action']
        file = request.files['image']

        if file:
            img = Image.open(file).convert('RGB')
            filename = file.filename
            original_path = os.path.join(UPLOAD_FOLDER, filename)
            img.save(original_path)

            if action == 'Encrypt':
                result_img = encrypt_image(img)
                encrypted_filename = f'encrypted_{filename}'
                result_img.save(os.path.join(ENCRYPTED_FOLDER, encrypted_filename))
                encrypted_history.append(encrypted_filename)

            elif action == 'Decrypt':
                result_img = decrypt_image(img)
                decrypted_filename = f'decrypted_{filename}'
                result_img.save(os.path.join(ENCRYPTED_FOLDER, decrypted_filename))
                decrypted_history.append(decrypted_filename)

    # Render templates with history
    return render_template('index.html',
                           encrypted_filename=encrypted_filename,
                           decrypted_filename=decrypted_filename,
                           encrypted_history=encrypted_history,
                           decrypted_history=decrypted_history)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(ENCRYPTED_FOLDER, filename), as_attachment=True)

def get_file_list(folder):
    """Utility to get all file names in the folder."""
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

if __name__ == '__main__':
    app.run(debug=True)
