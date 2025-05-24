# CV Navigation Project

This project implements an indoor navigation system using ArUco markers, Dijkstra's algorithm, and socket communication for integration with Unity for mixed reality headsets.

## Features
- Detects ArUco markers using OpenCV.
- Computes shortest paths using Dijkstra's algorithm.
- Sends navigation data to Unity via TCP socket.
- Provides text-to-speech navigation instructions.

## Setup
1. Install Python dependencies: `pip install opencv-python pyttsx3`
2. Run the Python script: `python navigation.py`
3. For Unity, open the `UnityProject` folder in Unity 2022.3+ and configure for MR headsets.

## Requirements
- Python 3.8+
- OpenCV, pyttsx3
- Unity 2022.3+ with XR Interaction Toolkit
- External webcam for ArUco detection

## Usage
1. Place ArUco markers (DICT_6X6_250, IDs 0-16) at room locations.
2. Run the Python script and input start/end rooms.
3. Deploy the Unity project to an MR headset (e.g., Meta Quest).

## License
MIT License
