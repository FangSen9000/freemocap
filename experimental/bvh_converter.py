import numpy as np


class BVHConverter:
    def __init__(self, skeleton_data: np.ndarray, marker_names: list, connections: list):
        self.skeleton_data = skeleton_data
        self.marker_names = marker_names
        self.connections = connections

    def _write_hierarchy(self) -> str:
        hierarchy = "HIERARCHY\nROOT Hips\n{\n\tOFFSET 0.0 0.0 0.0\n\tCHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation\n"

        # Add joint hierarchy based on connections
        for connection in self.connections:
            parent_name, child_name = connection
            parent_id = self.marker_names.index(parent_name)
            child_id = self.marker_names.index(child_name)
            offset = self.skeleton_data[0, child_id] - self.skeleton_data[0, parent_id]
            hierarchy += f"\tJOINT {child_name}\n\t{{\n\t\tOFFSET {offset[0]} {offset[1]} {offset[2]}\n\t\tCHANNELS 3 Zrotation Xrotation Yrotation\n\t}}"

        hierarchy += "\n}\n"
        return hierarchy

    def _write_motion(self) -> str:
        motion = f"MOTION\nFrames: {self.skeleton_data.shape[0]}\nFrame Time: 0.033333\n"

        for frame in self.skeleton_data:
            frame_data = " ".join([str(value) for marker in frame for value in marker])
            motion += frame_data + "\n"

        return motion

    def generate_bvh(self) -> str:
        return self._write_hierarchy() + self._write_motion()


if __name__ == "__main__":
    skeleton_frame_marker_dimension = np.load(r"C:\Users\jonma\freemocap_data\recording_sessions\freemocap_sample_data\freemocap_sample_data_frame_name_xyz.npy")
    marker_names = ["left_elbow", "left_wrist"]  # Define the marker names as needed
    connections = [("left_elbow", "left_wrist")]  # Define the connections as needed

    converter = BVHConverter(skeleton_frame_marker_dimension, marker_names, connections)
    bvh_content = converter.generate_bvh()

    with open("output.bvh", "w") as file:
        file.write(bvh_content)
