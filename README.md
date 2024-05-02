The PNG-to-MP4 code is python based code snippit that takea all images in a folder, sorts them, then makes an MP4 video file with them.

Original use case is for making MP4 of sprite work from asprite (such as video files of animation or for time laps).

Use the create_video() function with these paramiters:
image_folder: String for local location of the folder with all the PNG images
video_name: String for output name of the MP4 file
frame_duration: Double for how long each PNG frame should be displaied for in seconds
scale_factor: Int for changing the resolution size of the PNG images
lasting_end: Bool for if you want the video the linger on the final PNG image
linger_duration: Int for how many seconds should the last frame be lingered on (ignored if lasting_end is false)
cycles: Int for how many times the video should reapet before ending
