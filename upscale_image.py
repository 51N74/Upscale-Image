from PIL import ImageEnhance, Image

def enhance_images(image_paths, enhancement_factor):
    for image_path in image_paths:
        # Open the image using Pillow
        image = Image.open(image_path)

        # Convert the image to RGB mode
        image = image.convert("RGB")

        # Create an instance of the ImageEnhance class
        enhancer = ImageEnhance.Sharpness(image)

        # Enhance the image sharpness using the specified factor
        enhanced_image = enhancer.enhance(enhancement_factor)

        # Save the enhanced image with a modified file name
        file_name = image_path.split("/")[-1]
        enhanced_image.save(f"enhanced_{file_name}")

    print("Image enhancement completed")

# Provide a list of image file paths
image_paths = ["./image/Noga/image1.jpg","./image/Noga/image2.jpg"]
enhancement_factor = 10  # Change this value to adjust the enhancement

# Call the enhance_images function
enhance_images(image_paths, enhancement_factor)
