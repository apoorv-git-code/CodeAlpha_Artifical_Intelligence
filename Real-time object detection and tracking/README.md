# ⏳ Real-Time Object Detection and Tracking Dashboard 👀

A real-time Computer Vision pipeline built with Python, OpenCV, and YOLOv8. This application processes a live video feed (webcam or video file), detects objects, and tracks them continuously across frames using the ByteTrack algorithm. It features a live telemetry dashboard overlay displaying real-time tracking analytics.

## ⚙️ Features
* **Real-Time Inference:** High-speed object detection powered by a pre-trained YOLOv8 Nano model.
* **Persistent Object Tracking:** Uses ByteTrack to assign unique, consistent IDs to individual objects across frames.
* **Live Analytics Dashboard:** An on-screen overlay display showing:
  * **Live On-Screen Count:** Number of tracked objects currently in the frame.
  * **Total Unique Seen:** Cumulative count of unique object IDs observed throughout the session (safeguarded against duplicate counting).
* **Automated Recording:** Automatically encodes and saves the processed tracking feed to an output `.mp4` file.

---

## 🚀 Repository Structure 🚀

```text
├── yolo_tracker.py    # Main application script with analytics dashboard
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── yolo_tracker.mp4   # Auto-generated recorded output (created after running)
```

## 💻 Setup & Installation

Follow these steps to configure your local environment and run the application.

1. Clone the Repository
``` 
git clone https://github.com/apoorv-git-code/CodeAlpha_Artifical_Intelligence.git
cd CodeAlpha_Artifical_Intelligence/Real-time\ object\ detection\ and\ tracking
```
2. Set Up a Virtual Environment (Mostly preferred)
```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
3.  Install Dependencies

Install all required packages at once using the requirements.txt file:
```
pip install -r requirements.txt
```

 ## 🚦 How to Run

 Execute the main script to initialize your webcam stream and start the tracking pipeline:
```
python yolo_tracker.py
```
## ⚙️ Configuration Options

To change the video source from your live webcam to a pre-recorded local file, update line 10 in final_pipeline.py:
```
Python
# Change this:
cap = cv2.VideoCapture(0)

# To this:
cap = cv2.VideoCapture("path/to/your/video.mp4")
```
## 🎮 Controls
- Press q: Safely stops the video stream, updates the terminal summary, finalizes the video encoding, and exits the application.

## 📊 Core Architecture & Logic

Tracking Pipeline Flow
The data flow shifts away from independent, frame-by-frame image recognition, moving instead toward a unified, continuous object-management cycle:
- Frame Capture: OpenCV reads individual frames from the video hardware loop.
- AI Inference: The frame is passed into YOLOv8 to predict boundary coordinates.
- Bytetrack Processing: The bounding boxes are passed to the tracker, which correlates overlapping paths between Frame $T$ and Frame $T+1$ to lock persistent object IDs.
- Dashboard Render: Analytics are rendered directly into the frame before displaying and saving.

## Duplicate Prevention Logic
The application utilizes a Python set() data structure to manage cumulative object metrics. Because a set mathematically enforces uniqueness, appending an active ID repeatedly does not alter its structural length:
<p align="center">
     $$\text{Total Unique Seen} = |\{\text{ID}_1, \text{ID}_2, \dots, \text{ID}_n\}|$$
</p>
Even if an object stays in the camera's view for thousands of frames, it is strictly counted as one unique object over time, providing highly accurate data tracking.

## 📝 Dependencies
This project relies on the following open-source frameworks:
- Ultralytics (YOLOv8) - Model architecture and tracker.
- OpenCV-Python - Video capture, processing, GUI framework, and array-to-video compilation.
- NumPy - Array manipulation.
<p align="center">
       <img width="300" height="300" alt="GroupgreetingGroupgreeting-stickersGIF" src="https://github.com/user-attachments/assets/57d13fac-6623-41f8-975a-454ff13558c0" />
</p>
