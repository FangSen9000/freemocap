# Definition of mediapipe_skeleton_schema
from typing import Dict, Any

mediapipe_skeleton_schema = {
    'body': {
        'point_names': ['nose', 'left_eye_inner', 'left_eye', 'left_eye_outer', 'right_eye_inner', 'right_eye', 'right_eye_outer', 'left_ear', 'right_ear', 'mouth_left', 'mouth_right', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist', 'left_pinky', 'right_pinky', 'left_index', 'right_index', 'left_thumb', 'right_thumb', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle', 'left_heel', 'right_heel', 'left_foot_index', 'right_foot_index'],
        'connections': [(15, 21), (16, 20), (18, 20), (3, 7), (14, 16), (23, 25), (28, 30), (11, 23), (27, 31), (6, 8), (15, 17), (24, 26), (16, 22), (4, 5), (5, 6), (29, 31), (12, 24), (23, 24), (0, 1), (9, 10), (1, 2), (0, 4), (11, 13), (30, 32), (28, 32), (15, 19), (16, 18), (25, 27), (26, 28), (12, 14), (17, 19), (2, 3), (11, 12), (27, 29), (13, 15)],
        'virtual_marker_definitions': {'head_center': {'marker_names': ['left_ear', 'right_ear'], 'marker_weights': [0.5, 0.5]}, 'neck_center': {'marker_names': ['left_shoulder', 'right_shoulder'], 'marker_weights': [0.5, 0.5]}, 'trunk_center': {'marker_names': ['left_shoulder', 'right_shoulder', 'left_hip', 'right_hip'], 'marker_weights': [0.25, 0.25, 0.25, 0.25]}, 'hips_center': {'marker_names': ['left_hip', 'right_hip'], 'marker_weights': [0.5, 0.5]}},
        'parent': 'hips_center'
    },
    'hands': {},
    'face': {}
}

# Function to build the BVH hierarchy
def build_bvh_hierarchy_from_schema(schema: Dict[str, Any]) -> str:
    body_schema = schema["body"]
    point_names = body_schema["point_names"]
    connections = body_schema["connections"]

    hierarchy = "HIERARCHY\n"
    hierarchy += "ROOT " + body_schema["parent"] + "\n{\n"
    hierarchy += "    OFFSET 0.0 0.0 0.0\n"
    hierarchy += "    CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation\n"

    # Function to build joints recursively
    def build_joint(name: str, depth: int) -> str:
        children = [point_names[b] for a, b in connections if point_names[a] == name]
        result = "    " * depth + f"JOINT {name}\n"
        result += "    " * depth + "{\n"
        result += "    " * depth + "    OFFSET 0.0 0.0 0.0\n"  # Placeholder for OFFSET
        result += "    " * depth + "    CHANNELS 3 Zrotation Xrotation Yrotation\n"
        for child in children:
            result += build_joint(child, depth + 1)
        result += "    " * depth + "}\n"
        return result

    # Build the hierarchy from the root joint
    for child in body_schema["virtual_marker_definitions"]["hips_center"]["marker_names"]:
        hierarchy += build_joint(child, 1)

    hierarchy += "}\n"

    return hierarchy

if __name__ == "__main__":
    # Example usage: print the BVH hierarchy
    humanoid_hierarchy_from_schema = build_bvh_hierarchy_from_schema(mediapipe_skeleton_schema)
    print(humanoid_hierarchy_from_schema)
    #save to file
    with open("../humanoid_hierarchy_from_schema.bvh", "w") as f:
        f.write(humanoid_hierarchy_from_schema)
