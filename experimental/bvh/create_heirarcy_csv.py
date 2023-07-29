import pandas as pd
import numpy as np

from freemocap.core_processes.post_process_skeleton_data.estimate_skeleton_segment_lengths import \
    mediapipe_skeleton_segment_definitions, estimate_skeleton_segment_lengths


def create_hierarchy_csv(segment_definitions: dict, skeleton_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Create a CSV file containing hierarchy information from skeleton segment definitions.

    Args:
        segment_definitions (dict): Dictionary containing the definitions of each segment (i.e., the proximal and distal joints).
        skeleton_dataframe (pd.DataFrame): DataFrame containing the skeleton data.

    Returns:
        pd.DataFrame: DataFrame containing the hierarchy information.
    """
    hierarchy_data = []

    # Estimate the lengths of the skeleton segments
    skeleton_segment_lengths = estimate_skeleton_segment_lengths(skeleton_dataframe, segment_definitions)

    for segment_name, segment_definition in segment_definitions.items():
        joint = segment_definition["distal"]
        parent = segment_definition["proximal"]

        # Calculate offsets using the estimated segment lengths
        length = skeleton_segment_lengths[segment_name]["mean"]
        offset_x = 0
        offset_y = length / np.sqrt(3)
        offset_z = 0

        hierarchy_data.append([joint, parent, offset_x, offset_y, offset_z])

    # Create a DataFrame and save to CSV
    hierarchy_df = pd.DataFrame(hierarchy_data, columns=['joint', 'parent', 'offset.x', 'offset.y', 'offset.z'])
    hierarchy_df.to_csv('hierarchy.csv', index=False)

    return hierarchy_df

# Example usage:
segment_definitions = mediapipe_skeleton_segment_definitions
skeleton_dataframe = pd.read_csv(r"C:\Users\jonma\freemocap_data\recording_sessions\freemocap_sample_data\output_data\mediapipe_body_3d_xyz.csv")
create_hierarchy_csv(segment_definitions, skeleton_dataframe)
