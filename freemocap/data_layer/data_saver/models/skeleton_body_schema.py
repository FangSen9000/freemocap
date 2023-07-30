from freemocap.data_layer.data_saver.models.skeleton_models import SkeletonBody, HierarchySegment, \
    VirtualMarkerDefinition, \
    SegmentLength

skeleton_body_schema = SkeletonBody(Root=HierarchySegment(
    name="Spine",
    point_names=["hips_center", "chest_center"],
    virtual_marker_definitions={
        "hips_center": VirtualMarkerDefinition(marker_names=["left_hip", "right_hip"], marker_weights=[0.5, 0.5]),
        "chest_center": VirtualMarkerDefinition(marker_names=["left_shoulder", "right_shoulder"],
                                                marker_weights=[0.5, 0.5])},
    connections=[("hips_center", "chest_center")],
    length=SegmentLength(body_height=0.288,
                         measured_length=None),
    parent=None,
    origin="hips_center",
    center=VirtualMarkerDefinition(marker_names=["hips_center", "chest_center"], marker_weights=[0.5, 0.5]),
    pole="chest_center",
    children={
        "Neck": HierarchySegment(name="Neck",
                                 point_names=["chest_center", "head_center"],
                                 virtual_marker_definitions={
                                     "chest_center": VirtualMarkerDefinition(
                                         marker_names=["left_shoulder", "right_shoulder"], marker_weights=[0.5, 0.5]),
                                     "head_center": VirtualMarkerDefinition(
                                         marker_names=["nose", "left_ear", "right_ear"],
                                         marker_weights=[0.34, 0.33, 0.33])
                                 },
                                 connections=[("chest_center", "head_center")],
                                 length=SegmentLength(body_height=.066,
                                                      measured_length=None),
                                 origin="chest_center",
                                 center=VirtualMarkerDefinition(marker_names=["chest_center", "head_center"],
                                                                marker_weights=[0.5, 0.5]),
                                 pole="head_center",
                                 parent="Spine",
                                 children={
                                     "Head": HierarchySegment(name="Head",
                                                              point_names=["head_center", "nose", "left_ear",
                                                                           "right_ear", "left_eye_center",
                                                                           "right_eye_center"],
                                                              virtual_marker_definitions={
                                                                  "head_center": VirtualMarkerDefinition(
                                                                      marker_names=["nose", "left_ear", "right_ear"],
                                                                      marker_weights=[0.34, 0.33, 0.33])},
                                                              connections=[("head_center", "nose"),
                                                                           ("head_center", "left_ear"),
                                                                           ("head_center", "right_ear"),
                                                                           ("head_center", "left_eye_center"),
                                                                           ("head_center", "right_eye_center")],
                                                              length=SegmentLength(body_height=.05,
                                                                                   measured_length=None),
                                                              origin="head_center",
                                                              center="head_center",
                                                              pole="nose",
                                                              parent="Neck",
                                                              children={})}),
        "LeftHip": HierarchySegment(name="LeftHip",
                                    point_names=["hips_center", "left_hip"],
                                    virtual_marker_definitions={
                                        "hips_center": VirtualMarkerDefinition(
                                            marker_names=["left_hip", "right_hip"],
                                            marker_weights=[0.5, 0.5])},
                                    connections=[("hips_center", "left_hip")],
                                    length=SegmentLength(body_height=.095,
                                                         measured_length=None),
                                    origin="hips_center",
                                    center=VirtualMarkerDefinition(
                                        marker_names=["hips_center", "left_hip"],
                                        marker_weights=[0.5, 0.5]),
                                    pole="left_hip",
                                    parent="Spine",
                                    children={
                                        "LeftThigh": HierarchySegment(name="LeftThigh",
                                                                      point_names=[
                                                                          "left_hip",
                                                                          "left_knee"],
                                                                      virtual_marker_definitions={},
                                                                      connections=[(
                                                                          "left_hip",
                                                                          "left_knee")],
                                                                      length=SegmentLength(
                                                                          body_height=.245,
                                                                          measured_length=None),
                                                                      origin="left_hip",
                                                                      center=VirtualMarkerDefinition(
                                                                          marker_names=[
                                                                              "left_hip",
                                                                              "left_knee"],
                                                                          marker_weights=[
                                                                              0.5, 0.5]),
                                                                      pole="left_knee",
                                                                      parent="LeftHip",
                                                                      children={
                                                                          "LeftShin": HierarchySegment(
                                                                              name="LeftShin",
                                                                              point_names=[
                                                                                  "left_knee",
                                                                                  "left_ankle"],
                                                                              virtual_marker_definitions={},
                                                                              connections=[
                                                                                  (
                                                                                      "left_knee",
                                                                                      "left_ankle")],
                                                                              length=SegmentLength(
                                                                                  body_height=.246,
                                                                                  measured_length=None),
                                                                              origin="left_knee",
                                                                              center=VirtualMarkerDefinition(
                                                                                  marker_names=[
                                                                                      "left_knee",
                                                                                      "left_ankle"],
                                                                                  marker_weights=[
                                                                                      0.5,
                                                                                      0.5]),
                                                                              pole="left_ankle",
                                                                              parent="LeftThigh",
                                                                              children={
                                                                                  "LeftHeel": HierarchySegment(
                                                                                      name="LeftHeel",
                                                                                      point_names=[
                                                                                          "left_ankle",
                                                                                          "left_heel"],
                                                                                      virtual_marker_definitions={},
                                                                                      connections=[
                                                                                          (
                                                                                              "left_ankle",
                                                                                              "left_heel")],
                                                                                      length=SegmentLength(
                                                                                          body_height=.04,
                                                                                          measured_length=None),
                                                                                      origin="left_ankle",
                                                                                      center=VirtualMarkerDefinition(
                                                                                          marker_names=[
                                                                                              "left_ankle",
                                                                                              "left_heel"],
                                                                                          marker_weights=[
                                                                                              0.5,
                                                                                              0.5]),
                                                                                      pole="left_heel",
                                                                                      parent="LeftShin",
                                                                                      children={
                                                                                          "LeftFoot": HierarchySegment(
                                                                                              name="LeftFoot",
                                                                                              point_names=[
                                                                                                  "left_heel",
                                                                                                  "left_foot_index"],
                                                                                              virtual_marker_definitions={},
                                                                                              connections=[
                                                                                                  (
                                                                                                      "left_heel",
                                                                                                      "left_foot_index")],
                                                                                              length=SegmentLength(
                                                                                                  body_height=.152,
                                                                                                  measured_length=None),
                                                                                              origin="left_heel",
                                                                                              center=VirtualMarkerDefinition(
                                                                                                  marker_names=[
                                                                                                      "left_heel",
                                                                                                      "left_foot_index"],
                                                                                                  marker_weights=[
                                                                                                      0.5,
                                                                                                      0.5]),
                                                                                              pole="left_foot_index",
                                                                                              parent="LeftHeel", )
                                                                                      })})})}),
        "RightHip": HierarchySegment(name="RightHip",
                                     point_names=["hips_center", "right_hip"],
                                     virtual_marker_definitions={
                                         "hips_center": VirtualMarkerDefinition(
                                             marker_names=["left_hip", "right_hip"],
                                             marker_weights=[0.5, 0.5])},
                                     connections=[("hips_center", "right_hip")],
                                     length=SegmentLength(body_height=.095,
                                                          measured_length=None),
                                     origin="hips_center",
                                     center=VirtualMarkerDefinition(
                                         marker_names=["hips_center", "right_hip"],
                                         marker_weights=[0.5, 0.5]),
                                     pole="right_hip",
                                     parent="Spine",
                                     children={
                                         "RightThigh": HierarchySegment(name="RightThigh",
                                                                        point_names=[
                                                                            "right_hip",
                                                                            "right_knee"],
                                                                        virtual_marker_definitions={},
                                                                        connections=[(
                                                                            "right_hip",
                                                                            "right_knee")],
                                                                        length=SegmentLength(
                                                                            body_height=.245,
                                                                            measured_length=None),
                                                                        origin="right_hip",
                                                                        center=VirtualMarkerDefinition(
                                                                            marker_names=[
                                                                                "right_hip",
                                                                                "right_knee"],
                                                                            marker_weights=[
                                                                                0.5, 0.5]),
                                                                        pole="right_knee",
                                                                        parent="RightHip",

                                                                        children={
                                                                            "RightShin": HierarchySegment(
                                                                                name="RightShin",
                                                                                point_names=[
                                                                                    "right_knee",
                                                                                    "right_ankle"],
                                                                                virtual_marker_definitions={},
                                                                                connections=[
                                                                                    (
                                                                                        "right_knee",
                                                                                        "right_ankle")],
                                                                                length=SegmentLength(
                                                                                    body_height=.246,
                                                                                    measured_length=None),
                                                                                origin="right_knee",
                                                                                center=VirtualMarkerDefinition(
                                                                                    marker_names=[
                                                                                        "right_knee",
                                                                                        "right_ankle"],
                                                                                    marker_weights=[
                                                                                        0.5,
                                                                                        0.5]),
                                                                                pole="right_ankle",
                                                                                parent="RightThigh",
                                                                                children={
                                                                                    "RightHeel": HierarchySegment(
                                                                                        name="RightHeel",
                                                                                        point_names=[
                                                                                            "right_ankle",
                                                                                            "right_heel"],
                                                                                        virtual_marker_definitions={},
                                                                                        connections=[
                                                                                            (
                                                                                                "right_ankle",
                                                                                                "right_heel")],
                                                                                        length=SegmentLength(
                                                                                            body_height=.04,
                                                                                            measured_length=None),
                                                                                        origin="right_ankle",
                                                                                        center=VirtualMarkerDefinition(
                                                                                            marker_names=[
                                                                                                "right_ankle",
                                                                                                "right_heel"],
                                                                                            marker_weights=[
                                                                                                0.5,
                                                                                                0.5]),
                                                                                        pole="right_heel",
                                                                                        parent="RightShin",
                                                                                        children={
                                                                                            "RightFoot": HierarchySegment(
                                                                                                name="RightFoot",
                                                                                                point_names=[
                                                                                                    "right_heel",
                                                                                                    "right_foot_index"],
                                                                                                virtual_marker_definitions={},
                                                                                                connections=[
                                                                                                    (
                                                                                                        "right_heel",
                                                                                                        "right_foot_index")],
                                                                                                length=SegmentLength(
                                                                                                    body_height=.152,
                                                                                                    measured_length=None),
                                                                                                origin="right_heel",
                                                                                                center=VirtualMarkerDefinition(
                                                                                                    marker_names=[
                                                                                                        "right_heel",
                                                                                                        "right_foot_index"],
                                                                                                    marker_weights=[
                                                                                                        0.5,
                                                                                                        0.5]),
                                                                                                pole="right_foot_index",
                                                                                                parent="RightHeel",
                                                                                            )
                                                                                        })})})}),
        "LeftShoulder": HierarchySegment(name="LeftShoulder",
                                         point_names=["chest_center", "left_shoulder"],
                                         virtual_marker_definitions={
                                             "chest_center": VirtualMarkerDefinition(
                                                 marker_names=["left_shoulder",
                                                               "right_shoulder"],
                                                 marker_weights=[0.5, 0.5])},
                                         connections=[("chest_center", "left_shoulder")],
                                         length=SegmentLength(body_height=.129,
                                                              measured_length=None),
                                         origin="chest_center",
                                         center=VirtualMarkerDefinition(
                                             marker_names=["chest_center",
                                                           "left_shoulder"],
                                             marker_weights=[0.5, 0.5]),
                                         pole="left_shoulder",
                                         parent="Spine",
                                         children={
                                             "LeftUpperArm": HierarchySegment(
                                                 name="LeftUpperArm",
                                                 point_names=[
                                                     "left_shoulder",
                                                     "left_elbow"],
                                                 virtual_marker_definitions={},
                                                 connections=[
                                                     (
                                                         "left_shoulder",
                                                         "left_elbow")],
                                                 length=SegmentLength(
                                                     body_height=.186,
                                                     measured_length=None),
                                                 origin="left_shoulder",
                                                 center=VirtualMarkerDefinition(
                                                     marker_names=[
                                                         "left_shoulder",
                                                         "left_elbow"],
                                                     marker_weights=[
                                                         0.5, 0.5]),
                                                 pole="left_elbow",
                                                 parent="LeftShoulder",
                                                 children={
                                                     "LeftForeArm": HierarchySegment(
                                                         name="LeftForeArm",
                                                         point_names=[
                                                             "left_elbow",
                                                             "left_wrist"],
                                                         virtual_marker_definitions={},
                                                         connections=[
                                                             (
                                                                 "left_elbow",
                                                                 "left_wrist")],
                                                         length=SegmentLength(
                                                             body_height=.146,
                                                             measured_length=None),
                                                         origin="left_elbow",
                                                         center=VirtualMarkerDefinition(
                                                             marker_names=[
                                                                 "left_elbow",
                                                                 "left_wrist"],
                                                             marker_weights=[
                                                                 0.5, 0.5]),
                                                         pole="left_wrist",
                                                         parent="LeftUpperArm",
                                                         children={
                                                             "LeftHand": HierarchySegment(
                                                                 name="LeftHand",
                                                                 point_names=[
                                                                     "left_wrist",
                                                                     "left_thumb",
                                                                     "left_index",
                                                                     "left_pinky"],
                                                                 virtual_marker_definitions={},
                                                                 connections=[
                                                                     (
                                                                         "left_wrist",
                                                                         "left_thumb"),
                                                                     (
                                                                         "left_wrist",
                                                                         "left_index"),
                                                                     (
                                                                         "left_wrist",
                                                                         "left_pinky"),
                                                                     ("left_index",
                                                                      "left_pinky")],
                                                                 length=SegmentLength(
                                                                     body_height=.108,
                                                                     measured_length=None),
                                                                 origin="left_wrist",
                                                                 center=VirtualMarkerDefinition(
                                                                     marker_names=[
                                                                         "left_wrist",
                                                                         "left_index",
                                                                         "left_pinky"],
                                                                     marker_weights=[
                                                                         0.34, 0.33,
                                                                         0.33]),
                                                                 pole="left_index",
                                                                 parent="LeftForeArm",
                                                                 children={}
                                                             )})})}),
        "RightShoulder": HierarchySegment(name="RightShoulder",
                                          point_names=["chest_center", "right_shoulder"],
                                          virtual_marker_definitions={
                                              "chest_center": VirtualMarkerDefinition(
                                                  marker_names=["left_shoulder",
                                                                "right_shoulder"],
                                                  marker_weights=[0.5, 0.5])},
                                          connections=[("chest_center", "right_shoulder")],
                                          length=SegmentLength(body_height=.129,
                                                               measured_length=None),
                                          origin="chest_center",
                                          center=VirtualMarkerDefinition(
                                              marker_names=["chest_center",
                                                            "right_shoulder"],
                                              marker_weights=[0.5, 0.5]),
                                          pole="right_shoulder",
                                          parent="Spine",

                                          children={
                                              "RightUpperArm": HierarchySegment(
                                                  name="RightUpperArm",
                                                  point_names=[
                                                      "right_shoulder",
                                                      "right_elbow"],
                                                  virtual_marker_definitions={},
                                                  connections=[
                                                      (
                                                          "right_shoulder",
                                                          "right_elbow")],
                                                  length=SegmentLength(
                                                      body_height=.186,
                                                      measured_length=None),
                                                  origin="right_shoulder",
                                                  center=VirtualMarkerDefinition(
                                                      marker_names=[
                                                          "right_shoulder",
                                                          "right_elbow"],
                                                      marker_weights=[
                                                          0.5, 0.5]),
                                                  pole="right_elbow",
                                                  parent="RightShoulder",
                                                  children={
                                                      "RightForeArm": HierarchySegment(
                                                          name="RightForeArm",
                                                          point_names=[
                                                              "right_elbow",
                                                              "right_wrist"],
                                                          virtual_marker_definitions={},
                                                          connections=[
                                                              (
                                                                  "right_elbow",
                                                                  "right_wrist")],
                                                          length=SegmentLength(
                                                              body_height=.146,
                                                              measured_length=None),
                                                          origin="right_elbow",
                                                          center=VirtualMarkerDefinition(
                                                              marker_names=[
                                                                  "right_elbow",
                                                                  "right_wrist"],
                                                              marker_weights=[
                                                                  0.5, 0.5]),
                                                          pole="right_wrist",
                                                          parent="RightUpperArm",
                                                          children={
                                                              "RightHand": HierarchySegment(
                                                                  name="RightHand",
                                                                  point_names=[
                                                                      "right_wrist",
                                                                      "right_thumb",
                                                                      "right_index",
                                                                      "right_pinky"],
                                                                  virtual_marker_definitions={},
                                                                  connections=[
                                                                      (
                                                                          "right_wrist",
                                                                          "right_thumb"),
                                                                      (
                                                                          "right_wrist",
                                                                          "right_index"),
                                                                      (
                                                                          "right_wrist",
                                                                          "right_pinky"),
                                                                      ("right_index",
                                                                       "right_pinky")],
                                                                  length=SegmentLength(
                                                                      body_height=.108,
                                                                      measured_length=None),
                                                                  origin="right_wrist",
                                                                  center=VirtualMarkerDefinition(
                                                                      marker_names=[
                                                                          "right_wrist",
                                                                          "right_index",
                                                                          "right_pinky"],
                                                                      marker_weights=[
                                                                          0.34, 0.33,
                                                                          0.33]),
                                                                  pole="right_index",
                                                                  parent="RightForeArm",

                                                                  children={}
                                                              )})})}),
    }))

if __name__ == "__main__":
    print(skeleton_body_schema.json(indent=2))
