import os

from freemocap.data_layer.data_saver.models.skeleton_body_schema import skeleton_body_schema


def write_bvh_file(skeleton, filename):
    def write_segment(segment, indent=0, root=False):
        lines = []
        indent_str = '\t' * indent
        lines.append(f"{indent_str}JOINT {segment.name}")
        lines.append(f"{indent_str}{{")
        lines.append(f"{indent_str}\tOFFSET 0.0 {segment.length.body_height} 0.0")
        if root:
            lines.append(f"{indent_str}\tCHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation")
        else:
            lines.append(f"{indent_str}\tCHANNELS 3 Zrotation Xrotation Yrotation")
        for child in segment.children.values():
            lines.extend(write_segment(child, indent + 1))
        lines.append(f"{indent_str}}}")
        return lines

    lines = ["HIERARCHY"]
    lines.extend(write_segment(skeleton.Root, root=True))
    lines.append("MOTION")
    lines.append("Frames: 2")
    lines.append("Frame Time: 0.033333")
    lines.append("0.0 " * 6 * len(lines) + "0.0")
    lines.append("0.0 " * 6 * len(lines) + "0.0")

    with open(filename, 'w') as f:
        f.write('\n'.join(lines))

if __name__ == "__main__":
    write_bvh_file(skeleton_body_schema, "output.bvh")