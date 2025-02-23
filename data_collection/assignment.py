import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        self.image = None
        self.original_image = None
        self.cropped_image = None
        self.rect_start = None
        self.rect_end = None

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Load Image Button
        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Canvas for displaying images
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        # Crop Button
        self.crop_button = tk.Button(self.root, text="Crop Image", command=self.crop_image)
        self.crop_button.pack()

        # Resize Slider
        self.resize_slider = tk.Scale(self.root, from_=1, to=200, orient='horizontal', label="Resize Image")
        self.resize_slider.pack()
        self.resize_slider.bind("<Motion>", self.resize_preview)

        # Save Button
        self.save_button = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack()

    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if filepath:
            self.original_image = cv2.imread(filepath)
            self.image = self.original_image.copy()

            # Convert image to a format suitable for Tkinter
            self.display_image(self.image)

    def display_image(self, image):
        # Convert OpenCV image to Tkinter image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_pil)

        self.canvas.create_image(0, 0, image=image_tk, anchor='nw')
        self.canvas.image = image_tk

    def crop_image(self):
        # Allow user to draw a rectangle on the canvas for cropping
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

    def on_mouse_press(self, event):
        self.rect_start = (event.x, event.y)

    def on_mouse_drag(self, event):
        self.rect_end = (event.x, event.y)
        self.update_crop_rectangle()

    def on_mouse_release(self, event):
        self.rect_end = (event.x, event.y)
        self.crop_and_display()

    def update_crop_rectangle(self):
        # Remove previous rectangle and update the new one
        self.canvas.delete("rect")
        self.canvas.create_rectangle(self.rect_start[0], self.rect_start[1],
                                     self.rect_end[0], self.rect_end[1], outline="red", tags="rect")

    def crop_and_display(self):
        # Crop the image by removing the selected area
        x1, y1 = self.rect_start
        x2, y2 = self.rect_end
        cropped = self.image.copy()
        cropped[y1:y2, x1:x2] = 0  # Black out the selected area

        self.cropped_image = cropped
        self.display_image(cropped)

    def resize_preview(self, event):
        # Resize the cropped image and update the preview
        scale_factor = self.resize_slider.get() / 100
        resized_image = cv2.resize(self.cropped_image, None, fx=scale_factor, fy=scale_factor)
        self.display_image(resized_image)

    def save_image(self):
        if self.cropped_image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                cv2.imwrite(save_path, self.cropped_image)
                messagebox.showinfo("Saved", f"Image saved to {save_path}")
        else:
            messagebox.showerror("Error", "No cropped image to save.")

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
