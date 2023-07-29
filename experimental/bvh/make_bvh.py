from pathlib import Path

import pandas as pd

from freemocap.core_processes.post_process_skeleton_data.estimate_skeleton_segment_lengths import \
    estimate_skeleton_segment_lengths, mediapipe_skeleton_segment_definitions


def create_bvh_hierarchy(skeleton_segment_lengths: dict) -> dict:
    return {
        "ROOT": {
            "name": "Hips",
            "channels": ["Xposition", "Yposition", "Zposition", "Zrotation", "Xrotation", "Yrotation"],
            "offset": [0.0, 0.0, 0.0],
            "children": [
                {
                    "name": "Spine",
                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                    "offset": [0.0, skeleton_segment_lengths['upper_spine']['median'], 0.0],
                    "children": [
                        {
                            "name": "Chest",
                            "channels": ["Zrotation", "Xrotation", "Yrotation"],
                            "offset": [0.0, skeleton_segment_lengths['lower_spine']['median'], 0.0],
                            "children": [
                                {
                                    "name": "Neck",
                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                    "offset": [0.0, skeleton_segment_lengths['head']['median'], 0.0],
                                    "children": [
                                        {
                                            "name": "End Site",
                                            "offset": [0.0, skeleton_segment_lengths['head']['median'], 0.0]
                                        }
                                    ]
                                },
                                {
                                    "name": "Left_Shoulder",
                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                    "offset": [-skeleton_segment_lengths['left_clavicle']['median'], 0.0, 0.0],
                                    "children": [
                                        {
                                            "name": "Left_Elbow",
                                            "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                            "offset": [0.0, -skeleton_segment_lengths['left_upper_arm']['median'], 0.0],
                                            "children": [
                                                {
                                                    "name": "Left_Wrist",
                                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                                    "offset": [0.0, -skeleton_segment_lengths['left_forearm']['median'], 0.0],
                                                    "children": [
                                                        {
                                                            "name": "End Site",
                                                            "offset": [0.0, -skeleton_segment_lengths['left_hand']['median'], 0.0]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": "Right_Shoulder",
                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                    "offset": [skeleton_segment_lengths['right_clavicle']['median'], 0.0, 0.0],
                                    "children": [
                                        {
                                            "name": "Right_Elbow",
                                            "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                            "offset": [0.0, skeleton_segment_lengths['right_upper_arm']['median'], 0.0],
                                            "children": [
                                                {
                                                    "name": "Right_Wrist",
                                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                                    "offset": [0.0, skeleton_segment_lengths['right_forearm']['median'], 0.0],
                                                    "children": [
                                                        {
                                                            "name": "End Site",
                                                            "offset": [0.0, skeleton_segment_lengths['right_hand']['median'], 0.0]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Left_Hip",
                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                    "offset": [-skeleton_segment_lengths['left_pelvis']['median'], 0.0, 0.0],
                    "children": [
                        {
                            "name": "Left_Knee",
                            "channels": ["Zrotation", "Xrotation", "Yrotation"],
                            "offset": [0.0, -skeleton_segment_lengths['left_thigh']['median'], 0.0],
                            "children": [
                                {
                                    "name": "Left_Ankle",
                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                    "offset": [0.0, -skeleton_segment_lengths['left_calf']['median'], 0.0],
                                    "children": [
                                        {
                                            "name": "End Site",
                                            "offset": [0.0, -skeleton_segment_lengths['left_foot']['median'], 0.0]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Right_Hip",
                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                    "offset": [skeleton_segment_lengths['right_pelvis']['median'], 0.0, 0.0],
                    "children": [
                        {
                            "name": "Right_Knee",
                            "channels": ["Zrotation", "Xrotation", "Yrotation"],
                            "offset": [0.0, -skeleton_segment_lengths['right_thigh']['median'], 0.0],
                            "children": [
                                {
                                    "name": "Right_Ankle",
                                    "channels": ["Zrotation", "Xrotation", "Yrotation"],
                                    "offset": [0.0, -skeleton_segment_lengths['right_calf']['median'], 0.0],
                                    "children": [
                                        {
                                            "name": "End Site",
                                            "offset": [0.0, -skeleton_segment_lengths['right_foot']['median'], 0.0]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }


def create_bvh_content(hierarchy: dict, indentation: int = 0) -> str:
    lines = []
    indent = '    ' * indentation

    for key, joint in hierarchy.items():
        lines.append(f"{indent}{key} {joint['name']}")
        lines.append(f"{indent}{{")
        lines.append(f"{indent}    OFFSET {' '.join(map(str, joint['offset']))}")
        lines.append(f"{indent}    CHANNELS {len(joint['channels'])} {' '.join(joint['channels'])}")

        for child in joint.get('children', []):
            lines.append(create_bvh_content(child, indentation + 1))

        lines.append(f"{indent}}}")

    return "\n".join(lines)

if __name__ == "__main__":
    path_to_skeleton_body_csv = Path(
        r"D:\Dropbox\FreeMoCapProject\teddy_animation\FreeMocap_Data\sesh_2022-10-09_13_55_45_calib_and_take_1_alpha\output_data\mediapipe_body_3d_xyz.csv"
    )
    skeleton_dataframe = pd.read_csv(path_to_skeleton_body_csv)

    skeleton_segment_lengths = estimate_skeleton_segment_lengths(
        skeleton_dataframe, mediapipe_skeleton_segment_definitions
    )

    hierarchy = create_bvh_hierarchy(skeleton_segment_lengths)
    bvh_file_content = create_bvh_content(hierarchy)

    with open('test_bvh.bvh', "w") as f:
        f.write(bvh_file_content)
