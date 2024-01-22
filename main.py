from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Global variable for the image
new_image = None


# Functions
def upload_image():
    file = file_path_entry.get()
    print(file)
    image_display(file)


def image_display(filepath):
    pil_image = Image.open(filepath)
    # Calculate the scaling factor to fit the image within the canvas
    scale_factor = min(canvas.winfo_width() / pil_image.width, canvas.winfo_height() / pil_image.height)
    # Resize the image
    resized_image = pil_image.resize((int(pil_image.width * scale_factor), int(pil_image.height * scale_factor)))
    # Convert the resized PIL image to Tkinter-compatible PhotoImage
    new_image = ImageTk.PhotoImage(resized_image)
    # Update the canvas with the new image
    canvas.itemconfig(ph_image_id, image=new_image)
    # Keep a reference to the new image to prevent it from being garbage collected
    canvas.image = new_image


def add_watermark():
    global new_image
    watermark_text = watermark_entry.get()
    print(watermark_text)

    # Draw the watermark text on the image
    pil_image = Image.open(file_path_entry.get().strip())
    # Convert the image to "RGB" mode
    pil_image = pil_image.convert("RGB")

    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.load_default()

    text_color = (255, 255, 255)  # White color

    # Calculate the position for the watermark (50 pixels up and 50 pixels to the left from the bottom-right corner)
    x = pil_image.width - 50
    y = pil_image.height - 50

    # Draw the text on the image
    draw.text((x, y), watermark_text, font=font, fill=text_color)

    # Save the image with the watermark
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        pil_image.save(save_path)
        print(f"Image saved at: {save_path}")
        new_image = ImageTk.PhotoImage(pil_image)
        canvas.itemconfig(ph_image_id, image=new_image)
        # display in canvas
        image_display(save_path)


# Create a tkinter window to upload a image
window = Tk()
window.title("water mark")
window.config(padx=50, pady=50)

# Create a canvas for image
canvas = Canvas(height=400, width=400)
# initial_image="/Users/yamuna/documents/Images/healthy_food.png"
initial_image = "upload_png.png"
ph_image = PhotoImage(file=initial_image)
ph_image_id = canvas.create_image(200, 200, image=ph_image)
canvas.grid(row=0, column=1)

# labels for the tkinter
image_file_path = Label(text="Image File path")
image_file_path.grid(row=1, column=0)
water_mark_text_label = Label(text="Water Mark Text")
water_mark_text_label.grid(row=3, column=0)

# entries
file_path_entry = Entry(width=35)
file_path_entry.grid(row=1, column=1, columnspan=2)
file_path = file_path_entry.get()
file_path_entry.focus()
watermark_entry = Entry(width=35)
watermark_entry.grid(row=3, column=1)

# buttons
upload_imgae_button = Button(text="Upload image", width=33, command=upload_image)
upload_imgae_button.grid(row=2, column=1, columnspan=2)
add_watermark_button = Button(text="Add Watermark", width=33, command=add_watermark)
add_watermark_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
