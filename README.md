
Pixel Manipulation Image Encryption Tool
========================================

This is a simple yet powerful web application that allows users to encrypt and decrypt images using pixel manipulation techniques. It uses operations like pixel shuffling and bitwise XOR to modify images in a reversible way, ensuring image security and confidentiality.

Features
--------
- Upload and encrypt any image (JPG, PNG)
- Decrypt previously encrypted images
- View encrypted and decrypted image previews
- Download encrypted and decrypted files
- Auto-refresh history showing recent actions
- Stylish dark-themed interface using HTML/CSS

Folder Structure
----------------
PRODIGY_CS_2/
├── app.py
├── uploads/              # Uploaded original images
├── encrypted/            # Encrypted & decrypted images saved here
├── templates/
│   └── index.html        # Frontend interface
├── static/
│   └── style.css         # Dark theme styling
└── README.txt

Installation
------------
1. Clone the Repository
   git clone https://github.com/your-username/image-encryptor.git
   cd image-encryptor

2. Install Dependencies
   Make sure you have Python 3.8+ installed.
   pip install flask pillow numpy

How to Run
----------
python pixel.py
Then, open your browser and go to:  
http://127.0.0.1:5000/

How It Works
------------
1. Encryption:
   - The image pixels are randomly shuffled using a key.
   - Each pixel is bitwise XORed with 127 for obfuscation.
   - The resulting image is saved as an encrypted image.

2. Decryption:
   - XOR operation is reversed.
   - Pixels are reshuffled back to their original positions using the same key.
   - The decrypted image is recovered.

Concepts Used
-------------
- NumPy array manipulation
- Randomized pixel index generation
- Reversible bitwise operations
- Flask for web routing and image handling
- HTML & CSS for frontend UI

Todo / Improvements
-------------------
- Add user-defined key inputs for custom encryption
- Add support for grayscale images
- Add a "Clear All History" button
- Enhance UI responsiveness

Developed By
------------
PRODIGY INFOTECH INTERNSHIP PROJECT
Emmanuel Omopariola
