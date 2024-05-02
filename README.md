
The PNG-to-MP4 code is a Python-based snippet that takes all images in a folder, sorts them, and then creates an MP4 video file with them.

The original use case is for making MP4 videos of sprite work from Aseprite (such as animation files or time lapses).

Use the `create_video()` function with these parameters:

1.  `image_folder`: String specifying the local location of the folder containing all the PNG images.
2.  `video_name`: String for the output name of the MP4 file.
3.  `frame_duration`: Double indicating how long each PNG frame should be displayed in seconds.
4.  `scale_factor`: Int for changing the resolution size of the PNG images.
5.  `lasting_end`: Bool to determine if the video should linger on the final PNG image.
6.  `linger_duration`: Int for how many seconds the last frame should linger (ignored if `lasting_end` is false).
7.  `cycles`: Int for how many times the video should repeat before ending.
