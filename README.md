CV Navigation Project
This project implements an indoor navigation system using ArUco markers for real-world positioning, Dijkstra's algorithm for shortest path calculation, and socket communication to integrate with Unity for mixed reality (MR) headsets like Meta Quest or HoloLens. The system detects ArUco markers via an external webcam, computes the optimal path between user-specified rooms, provides text-to-speech (TTS) navigation instructions, and sends real-time navigation data to a Unity application for visualization in an MR environment.
Features

ArUco Marker Detection: Uses OpenCV to detect DICT_6X6_250 ArUco markers mapped to room locations.
Dynamic Pathfinding: Implements Dijkstra's algorithm to compute the shortest path between start and destination rooms.
Text-to-Speech Feedback: Provides audio navigation instructions using pyttsx3.
Socket Communication: Sends real-time navigation data (current room, next room, direction) to Unity via TCP socket.
Mixed Reality Integration: Displays navigation cues (text, arrows) in Unity for MR headsets, leveraging passthrough or holographic rendering.
User Input: Allows users to specify start and destination rooms interactively.

Requirements
Python

Python 3.8+
Libraries:
opencv-python (for ArUco marker detection)
pyttsx3 (for text-to-speech)


External USB webcam or Raspberry Pi camera module (MR headsets restrict direct camera access).

Unity

Unity 2022.3 or later
Packages:
XR Interaction Toolkit
TextMeshPro
OpenXR (for Meta Quest) or Windows Mixed Reality (for HoloLens)


MR headset (e.g., Meta Quest, HoloLens) or development environment with Quest Link/Holographic Remoting.

Hardware

Computer to run the Python script (e.g., laptop or Raspberry Pi).
MR headset for Unity deployment.
Printed ArUco markers (DICT_6X6_250, IDs 0–16, ~100mm size).

Installation

Clone the Repository:
git clone https://github.com/your-username/ARNavigationProject.git
cd ARNavigationProject


Python Setup:

Install dependencies:pip install opencv-python pyttsx3


Ensure a webcam is connected and accessible via OpenCV.


Unity Setup:

Open the UnityProject folder in Unity 2022.3+.
Install required packages via Package Manager:
XR Interaction Toolkit
TextMeshPro
OpenXR or Windows Mixed Reality


Configure build settings:
Platform: Android (Meta Quest) or UWP (HoloLens).
Enable XR Plug-in Management and Passthrough (for Quest).


Update the IP address in Assets/Scripts/NavigationClient.cs to match the Python server’s IP.


ArUco Markers:

Print ArUco markers (IDs 0–16, DICT_6X6_250) using OpenCV’s marker generator or pre-generated images.
Place markers at room locations corresponding to the room_positions dictionary in navigation.py.



Usage

Prepare the Environment:

Place ArUco markers at designated room locations (e.g., 115, MA155) as per the room_positions coordinates.
Ensure the webcam has a clear view of the markers.


Run the Python Script:

Execute the script:python navigation.py


Enter the start and destination rooms when prompted (e.g., 115, MA150).
The script detects markers, computes the shortest path, and sends navigation data to Unity.


Run the Unity Application:

Build and deploy the Unity project to the MR headset or test via Quest Link/Holographic Remoting.
The Unity app displays navigation instructions (e.g., “At 115, turn right to MA155”) and a directional arrow in the MR environment.


Navigate:

Follow the TTS instructions from the Python script and visual cues in the MR headset.
Move to each marker until reaching the final destination.



File Structure
ARNavigationProject/
├── navigation.py           # Python script for ArUco detection and pathfinding
├── UnityProject/           # Unity project folder
│   ├── Assets/
│   │   ├── Scripts/
│   │   │   └── NavigationClient.cs  # Unity script for socket communication
│   │   └── [other assets]
│   ├── ProjectSettings/
│   └── Packages/
├── docs/                   # Documentation and screenshots
│   ├── python_output.png   # Screenshot of Python console
│   └── mr_navigation.png   # Screenshot of MR headset output
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
└── LICENSE                 # MIT License

Screenshots

Notes

Camera Limitation: MR headsets restrict direct camera access, so an external webcam or Raspberry Pi camera is used for ArUco detection.
Network: Ensure the Python server and Unity client are on the same network. Update the IP address in NavigationClient.cs if not using localhost.
Calibration: Calibrate the webcam for accurate marker detection using OpenCV’s calibration tools.
Performance: Optimize Unity assets (e.g., low-poly models) to maintain a high frame rate in MR.

Troubleshooting

Socket Connection Issues:
Verify the Python server’s IP address and port (65432) in NavigationClient.cs.
Ensure no firewall is blocking port 65432.


Marker Detection Failures:
Check lighting conditions and marker size (~100mm).
Confirm the correct ArUco dictionary (DICT_6X6_250).


Unity MR Issues:
Enable Passthrough for Meta Quest or set Clear Flags to Black for HoloLens.
Test with Quest Link or Holographic Remoting for debugging.


