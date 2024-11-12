import os
import sys
import streamlit as st
from streamlit_webrtc import VideoHTMLAttributes, webrtc_streamer
from aiortc.contrib.media import MediaRecorder
import av

# Set base directory and append to system path for conditional imports later
BASE_DIR = os.path.abspath(os.path.join(__file__, '../../'))
sys.path.append(BASE_DIR)

# Main title of the application
st.title('FITVOYAGE AI FITNESS TRAINER')

# Dropdown menu for exercise selection
exercise_choice = st.selectbox("Choose Exercise", ("Select", "Bicep Curls", "Squats"))

# Initialize variables for processing and threshold setup
live_process_frame = None
thresholds = None
pose = None

# Only import and set up modules after user selects an exercise
if exercise_choice == "Bicep Curls":
    # Import necessary functions and classes for Bicep Curls
    from utils import get_mediapipe_pose
    from process_frame import ProcessFrame
    from thresholds import get_bicep_curl_thresholds
    
    # Initialize threshold and processing objects
    thresholds = get_bicep_curl_thresholds()
    live_process_frame = ProcessFrame(thresholds=thresholds, flip_frame=True)
    pose = get_mediapipe_pose()
    
    st.subheader("Bicep Curl Analysis")

elif exercise_choice == "Squats":
    # Import necessary functions and classes for Squats
    from utils import get_mediapipe_pose
    from process_frame2 import ProcessFrame2
    from thresholds import get_thresholds
    
    # Initialize threshold and processing objects
    thresholds = get_thresholds()
    live_process_frame = ProcessFrame2(thresholds=thresholds, flip_frame=True)
    pose = get_mediapipe_pose()
    
    st.subheader("Squats Analysis")

# Output video file name based on exercise choice
output_video_file = f'output_{exercise_choice.lower()}.flv' if exercise_choice != "Select" else None

# Function to process each video frame
def video_frame_callback(frame: av.VideoFrame):
    if live_process_frame and pose:
        frame = frame.to_ndarray(format="rgb24")  # Decode and get RGB frame
        frame, _ = live_process_frame.process(frame, pose)  # Process frame
        return av.VideoFrame.from_ndarray(frame, format="rgb24")  # Encode and return RGB frame
    return frame

# Function to set up video recording output
def out_recorder_factory() -> MediaRecorder:
    return MediaRecorder(output_video_file)

# Only display the webrtc streamer if a valid exercise is selected
if exercise_choice != "Select":
    webrtc_streamer(
        key=f"{exercise_choice}-pose-analysis",
        video_frame_callback=video_frame_callback,
        rtc_configuration={"iceServers": []},
        media_stream_constraints={"video": {"width": {'min': 480, 'ideal': 720}}, "audio": False},
        video_html_attrs=VideoHTMLAttributes(autoPlay=True, controls=False, muted=False),
        out_recorder_factory=out_recorder_factory
    )