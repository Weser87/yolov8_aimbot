# Your screen resolution
original_screen_width = 1920
original_screen_height = 1080

# Object Search window resolution
screen_width = 640
screen_height = 480

# dxcam Capture method
Dxcam_capture = True
dxcam_capture_fps = 144
dxcam_monitor_id = 0
dxcam_gpu_id = 0
dxcam_max_buffer_len = 64

# Obs capture method
Obs_capture = False
Obs_camera_id = 1

# Windows capture method
Windows_capture = False

# Aim settings
head_correction = False
y_offset = 0.35

# Mouse settings (More, less mouse shaking)
mouse_sensitivity = 3

# Cv2 debug window settings
show_window = True
show_speed = False
show_fps = False
debug_window_scale_percent = 100
debug_window_name = 'RT'

# AI settings
model_path='models/all_1.pt'

#TEMP#
aim_x = 0
aim_y = 0
aim_x_left = 0
aim_x_right = 0
aim_y_up = 0
aim_y_down = 0

def Calculate_screen_offset():
    left = original_screen_width / 2 - screen_width / 2
    top = original_screen_height / 2 - screen_height / 2
    width = left + screen_width
    height = top + screen_height
    return (int(left), int(top), int(width), int(height))