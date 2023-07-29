from pathlib import Path

import pandas as pd

from freemocap.core_processes.post_process_skeleton_data.estimate_skeleton_segment_lengths import \
    mediapipe_skeleton_segment_definitions, estimate_skeleton_segment_lengths


def write_bvh_file(segment_lengths: dict, file_path: str) -> None:
    with open(file_path, 'w') as bvh_file:
        bvh_file.write("HIERARCHY\n")
        bvh_file.write("ROOT Hips\n{\n")
        bvh_file.write("\tOFFSET 0.0 0.0 0.0\n")
        bvh_file.write("\tCHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation\n")

        def write_joint(joint_name: str):
            length = segment_lengths[joint_name]['median']
            bvh_file.write(f"\tJOINT {joint_name}\n\t{{\n")
            bvh_file.write(f"\t\tOFFSET 0.0 {length} 0.0\n")
            bvh_file.write("\t\tCHANNELS 3 Zrotation Xrotation Yrotation\n")

        write_joint("lower_spine")
        write_joint("upper_spine")
        write_joint("head")
        write_joint("left_clavicle")
        write_joint("left_upper_arm")
        write_joint("left_forearm")
        write_joint("left_hand")
        write_joint("right_clavicle")
        write_joint("right_upper_arm")
        write_joint("right_forearm")
        write_joint("right_hand")
        write_joint("left_pelvis")
        write_joint("left_thigh")
        write_joint("left_calf")
        write_joint("left_foot")
        write_joint("right_pelvis")
        write_joint("right_thigh")
        write_joint("right_calf")
        write_joint("right_foot")

        bvh_file.write("\t}\n" * (len(segment_lengths) + 1))
        bvh_file.write("MOTION\n")
        # ...


if __name__ == "__main__":
    path_to_skeleton_body_csv = Path(
        "D:/Dropbox/FreeMoCapProject/teddy_animation/FreeMocap_Data/sesh_2022-10-09_13_55_45_calib_and_take_1_alpha/output_data/mediapipe_body_3d_xyz.csv"
    )
    skeleton_dataframe = pd.read_csv(path_to_skeleton_body_csv)

    skeleton_segment_lengths = estimate_skeleton_segment_lengths(
        skeleton_dataframe, mediapipe_skeleton_segment_definitions
    )

    output_bvh_file_path = '../output.bvh'
    write_bvh_file(skeleton_segment_lengths, output_bvh_file_path)