# CV-Indoor-Navigation
Computer Vision-Based Indoor Navigation Using ArUco Markers
This project provides a classroom navigation system using computer vision (OpenCV) and ArUco markers. It helps users find their way within a building (e.g., an academic block) by recognizing ArUco markers placed outside rooms and providing step-by-step audio instructions based on Dijkstra’s shortest path algorithm.

🎯 Project Highlights
Uses ArUco markers to recognize room positions via webcam

Calculates the shortest path using Dijkstra’s algorithm

Provides real-time guidance through visual and spoken instructions

Tracks user progress as they pass by each marker

Built using Python, OpenCV, and pyttsx3 for text-to-speech

🛠️ Tech Stack
Python 3.x

OpenCV (cv2 & cv2.aruco)

pyttsx3 (Text-to-Speech)

NumPy

Webcam for real-time video input

📦 Requirements
Install the dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt:

opencv-python
numpy
pyttsx3

🚀 How to Run the Project
Clone the repository.

Open the terminal in the project folder.

Run the main script:

bash
Copy
Edit
python ar_navigation.py
When prompted, enter:

Starting room ID (e.g., 115)

Destination room ID (e.g., 101)

The webcam will start. Hold ArUco markers in view or walk past them in order.

Spoken instructions and visual detection will guide you step-by-step.

To stop: press q in the webcam window.

🧠 How It Works
ArUco markers placed outside classrooms are mapped to room IDs.

The system tracks user position using a webcam and detects the marker in view.

Based on the current room and destination, it calculates the shortest path.

For each step, it announces the next direction (left or right) and the remaining distance/time.

🗺️ Navigation Logic
The classroom layout is modeled as a graph with edges representing corridors or distances.

Dijkstra’s algorithm finds the optimal route.

Each room has coordinates and connections for direction estimation.

Directions are estimated based on X-axis movement (left/right).

📂 Project Structure
project-folder/
├── ar_navigation.py # Main script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── assets/ # (Optional) ArUco marker images, demo visuals

🧪 Future Improvements
Add detection confidence stats (e.g., percentage match)

Display a mini GUI or console map

Integrate with external camera or mobile camera stream

Extend to multi-floor navigation
