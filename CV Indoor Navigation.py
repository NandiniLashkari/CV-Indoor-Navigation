import cv2
import cv2.aruco as aruco
import pyttsx3
import heapq

#ClassRoom ID
room_positions = {
    "115": (0, 0), "114": (2, 0), "113": (4, 0), "112": (6, 0), "111": (8, 0),
    "110": (10, 0), "109": (12, 0), "108": (14, 0), "107": (16, 0), "106": (18, 0),
    "105": (20, 0), "104": (22, 0), "103": (24, 0), "102": (26, 0), "101": (28, 0),
    "MA155": (14, 5), "MA150": (28, 5)
}

# Graph
graph = {
    "115": {"114": 4.27, "MA155": 26.05},
    "114": {"115": 4.27, "113": 16.91},
    "113": {"114": 16.91, "112": 5.98},
    "112": {"113": 5.98, "111": 6.11},
    "111": {"112": 6.11, "110": 4.42},
    "110": {"111": 4.42, "109": 10.10},
    "109": {"110": 10.10, "108": 15.95},
    "108": {"109": 15.95, "107": 4.22, "MA155": 30.39},
    "107": {"108": 4.22, "106": 16.00},
    "106": {"107": 16.00, "105": 6.14},
    "105": {"106": 6.14, "104": 4.42},
    "104": {"105": 4.42, "103": 6.72},
    "103": {"104": 6.72, "102": 16.80},
    "102": {"103": 16.80, "101": 5.17},
    "101": {"102": 5.17, "MA150": 26.36},
    "MA155": {"108": 30.39, "115": 26.05, "MA150": 30.0},
    "MA150": {"MA155": 30.0, "101": 26.36}
}


def dijkstra(graph, start, end):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

 
    path = []
    node = end
    while node:
        path.insert(0, node)
        node = previous[node]

    return path, distances[end]


engine = pyttsx3.init()
def speak(text):
    print("[SPEAK]", text)
    engine.say(text)
    engine.runAndWait()


def total_distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += graph[path[i]].get(path[i + 1], 0)
    return dist


print("Available rooms:", ', '.join(room_positions.keys()))
start_room = input("Enter starting room: ").strip().upper()
end_room = input("Enter destination room: ").strip().upper()

if start_room not in room_positions or end_room not in room_positions:
    print("Invalid room entered. Please check room names.")
    exit()

path, full_distance = dijkstra(graph, start_room, end_room)
total_time = full_distance / 1.0  # 1 m/s walking speed

print(f"Shortest path: {' -> '.join(path)}")
print(f"Total distance: {full_distance:.2f} meters")
print(f"Estimated time: {total_time:.1f} seconds")
speak(f"Path from {start_room} to {end_room}. Distance: {int(full_distance)} meters. Time: {int(total_time)} seconds.")

#ArUco Setup
dict_type = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()
cap = cv2.VideoCapture(0)

#Mapping marker ID to room name
marker_id_to_room = {
    0: "115", 1: "114", 2: "113", 3: "112", 4: "111",
    5: "110", 6: "109", 7: "108", 8: "107", 9: "106",
    10: "105", 11: "104", 12: "103", 13: "102", 14: "101",
    15: "MA155", 16: "MA150"
}

#Main Loop
current_index = 0
visited = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    corners, ids, _ = aruco.detectMarkers(frame, dict_type, parameters=parameters)

    if ids is not None:
        for i, marker_id in enumerate(ids.flatten()):
            if marker_id in marker_id_to_room:
                room = marker_id_to_room[marker_id]

                if room == path[current_index] and room not in visited:
                    print(f"Reached {room}")
                    speak(f"You are at {room}")
                    visited.add(room)

                    if current_index < len(path) - 1:
                        current_index += 1
                        next_room = path[current_index]

                        x1, _ = room_positions[room]
                        x2, _ = room_positions[next_room]
                        direction = "right" if x2 > x1 else "left"

                        remaining_path = path[current_index:]
                        remaining_distance = total_distance(remaining_path)
                        remaining_time = remaining_distance / 1.0

                        speak(f"Turn {direction} towards {next_room}. Remaining distance is {int(remaining_distance)} meters. Time left is {int(remaining_time)} seconds.")
                    else:
                        speak("You have reached your final destination.")

    aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow("AR Navigation", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
