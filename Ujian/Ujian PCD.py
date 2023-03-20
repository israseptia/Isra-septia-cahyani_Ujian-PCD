import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.original_image = None
        self.modified_image_1 = None
        self.modified_image_2 = None
        # Buat tombol untuk memilih gambar
        self.select_image_button = tk.Button(root, text="Gambar", command=self.select_image)
        self.select_image_button.pack(pady=10)

        # Buat tampilan untuk gambar asli
        self.original_image_label = tk.Label(root)
        self.original_image_label.pack(pady=10)

        # Buat tombol untuk metode perbaikan 1
        self.method_1_button = tk.Button(root, text="Metode Perbaikan 1", command=self.apply_method_1)
        self.method_1_button.pack(pady=10)

        # Buat tampilan untuk gambar hasil metode perbaikan 1
        self.modified_image_1_label = tk.Label(root)
        self.modified_image_1_label.pack(pady=10)

        # Buat tombol untuk metode perbaikan 2
        self.method_2_button = tk.Button(root, text="Metode Perbaikan 2", command=self.apply_method_2)
        self.method_2_button.pack(pady=10)

        # Buat tampilan untuk gambar hasil metode perbaikan 2
        self.modified_image_2_label = tk.Label(root)
        self.modified_image_2_label.pack(pady=10)

    def select_image(self):
        # Membuka jendela dialog untuk memilih gambar
        file_path = filedialog.askopenfilename()
        if file_path:
            # Baca gambar dan tampilkan di tampilan gambar asli
            self.original_image = Image.open(file_path)
            self.original_image = self.original_image.convert("RGB")
            photo = ImageTk.PhotoImage(self.original_image)
            self.original_image_label.configure(image=photo)
            self.original_image_label.image = photo

    def apply_method_1(self):
        if self.original_image:
            # Lakukan metode perbaikan 1 dan tampilkan di tampilan gambar hasil metode perbaikan 1
            self.modified_image_1 = self.original_image.filter(ImageFilter.GaussianBlur(radius=2))
            photo = ImageTk.PhotoImage(self.modified_image_1)
            self.modified_image_1_label.configure(image=photo)
            self.modified_image_1_label.image = photo

    def apply_method_2(self):
        if self.original_image:
            # Lakukan metode perbaikan 2 dan tampilkan di tampilan gambar hasil metode perbaikan 2
            enhancer = ImageEnhance.Contrast(self.original_image)
            self.modified_image_2 = enhancer.enhance(2.0)
            photo = ImageTk.PhotoImage(self.modified_image_2)
            self.modified_image_2_label.configure(image=photo)
            self.modified_image_2_label.image = photo

root = tk.Tk()
editor = ImageEditor(root)
root.mainloop()
