from pathlib import Path

import pandas as pd
from collections import OrderedDict

from freemocap.core_processes.post_process_skeleton_data.estimate_skeleton_segment_lengths import \
    estimate_skeleton_segment_lengths, mediapipe_skeleton_segment_definitions


def create_bvh_hierarchy(skeleton_segment_lengths: dict):
    """Create BVH hierarchy from skeleton segment lengths.

    Args:
        skeleton_segment_lengths (dict): Dictionary containing the estimated length of each skeleton segment.

    Returns:
        Bvh: A Bvh object representing the skeleton hierarchy.
    """
    hierarchy_template = """
    HIERARCHY
    ROOT lower_spine
    {{
        OFFSET 0 0 0
        CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation
        {content}
    }}
    """

    # Define the hierarchy of the skeleton.
    segments_hierarchy = OrderedDict(
        lower_spine=["upper_spine"],
        upper_spine=["head", "left_clavicle", "right_clavicle"],
        head=[],
        left_clavicle=["left_upper_arm"],
        left_upper_arm=["left_forearm"],
        left_forearm=["left_hand"],
        left_hand=[],
        right_clavicle=["right_upper_arm"],
        right_upper_arm=["right_forearm"],
        right_forearm=["right_hand"],
        right_hand=[],
        left_pelvis=["left_thigh"],
        left_thigh=["left_calf"],
        left_calf=["left_foot"],
        left_foot=[],
        right_pelvis=["right_thigh"],
        right_thigh=["right_calf"],
        right_calf=["right_foot"],
        right_foot=[]
    )

    def create_bvh_node(segment_name):
        children_segments = segments_hierarchy[segment_name]
        segment_length = skeleton_segment_lengths[segment_name]["median"]

        children_content = "\n".join(create_bvh_node(child_segment) for child_segment in children_segments)
        content = f"""
        JOINT {segment_name}
        {{
            OFFSET 0 0 {segment_length}
            CHANNELS 3 Zrotation Xrotation Yrotation
            {children_content}
        }}
        """
        return content

    # Build the hierarchy starting from the root.
    content = create_bvh_node("lower_spine")
    hierarchy_str = hierarchy_template.format(content=content)

    return hierarchy_str

if __name__ == "__main__":

    path_to_skeleton_body_csv = Path(
            r"D:\Dropbox\FreeMoCapProject\teddy_animation\FreeMocap_Data\sesh_2022-10-09_13_55_45_calib_and_take_1_alpha\output_data\mediapipe_body_3d_xyz.csv"
        )
    skeleton_dataframe = pd.read_csv(path_to_skeleton_body_csv)

    skeleton_segment_lengths = estimate_skeleton_segment_lengths(skeleton_dataframe, mediapipe_skeleton_segment_definitions)
    bvh_hierarchy = create_bvh_hierarchy(skeleton_segment_lengths)

    with open('../output.bvh', 'w') as file:
        file.write(str(bvh_hierarchy))
