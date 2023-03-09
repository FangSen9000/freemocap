from pathlib import Path
import logging

import numpy as np

from freemocap.core_processes.capture_volume_calibration.triangulate_3d_data import save_mediapipe_3d_data_to_npy
from freemocap.utilities.flatten_3d_data import project_3d_data_to_z_plane

logger = logging.getLogger(__name__)


def process_single_camera_3d_data(input_skel3d_frame_marker_xyz: np.ndarray, raw_data_folder_path: Path) \
        -> [np.ndarray, np.ndarray]:

    logger.info("Processing Single Camera 3d data...")

    skeleton_reprojection_error_fr_mar = np.zeros(input_skel3d_frame_marker_xyz.shape[0:2])

    raw_skel3d_frame_marker_xyz = project_3d_data_to_z_plane(
        skel3d_frame_marker_xyz=input_skel3d_frame_marker_xyz)

    save_mediapipe_3d_data_to_npy(
        data3d_numFrames_numTrackedPoints_XYZ=raw_skel3d_frame_marker_xyz,
        data3d_numFrames_numTrackedPoints_reprojectionError=skeleton_reprojection_error_fr_mar,
        path_to_folder_where_data_will_be_saved=raw_data_folder_path,
    )

    return raw_skel3d_frame_marker_xyz, skeleton_reprojection_error_fr_mar