import cv2
import os
import re

##by Buoysharkdog
##PNG-to-MP4
def upscale_image(image, scale_factor):
    return cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

def create_video(image_folder, video_name, frame_duration, scale_factor, lasting_end, linger_duration, cycles):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key=extract_number)  # Sort images based on the frame number, all images must have the same name

    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    frame = upscale_image(frame, scale_factor)
    height, width, layers = frame.shape

    # Modify here to save the video in the image folder
    video_path = os.path.join(image_folder, video_name)
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 1/frame_duration, (width, height))

    # Add images to video per cycle
    i = 0
    while i < cycles:
        for image in images:
            img = cv2.imread(os.path.join(image_folder, image))
            img = upscale_image(img, scale_factor)
            video.write(img)
        i = i + 1

    if (lasting_end == True):
        # Linger on the last frame for
        last_frame = img
        linger_duration = 0  # seconds
        linger_frames = int(1 / frame_duration * linger_duration)

        for _ in range(linger_frames):
            video.write(last_frame)

    video.release()

# Usage
create_video('C:\\Users\\testuser\\pngfolder', 'png_video.mp4', 0.1, 1, False, 0, 1)
