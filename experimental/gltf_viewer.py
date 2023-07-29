from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QVector3D
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.Qt3DExtras import Qt3DWindow, QFirstPersonCameraController
from PyQt6.Qt3DRender import QMesh
from PyQt6.Qt3DCore import QEntity, QTransform
from PyQt6.Qt3DAnimation import QClipAnimator, QAnimationClipLoader
from pygltflib import GLTF2, Buffer, BufferView, Accessor, Animation, AnimationChannel, AnimationSampler, Scene, Node
import numpy as np


class GLTFViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        gltf_path = self.create_gltf()

        # Qt3D Window
        self.view = Qt3DWindow()
        self.container = QWidget.createWindowContainer(self.view)
        self.setCentralWidget(self.container)

        # Scene
        self.root_entity = QEntity()
        self.view.setRootEntity(self.root_entity)

        # Camera
        camera = self.view.camera()
        camera.setPosition(QVector3D(0, 0, 5))
        camera.setViewCenter(QVector3D(0, 0, 0))
        cam_controller = QFirstPersonCameraController(self.root_entity)
        cam_controller.setCamera(camera)

        # Mesh
        mesh = QMesh()
        mesh.setSource(QUrl.fromLocalFile(gltf_path))
        mesh_entity = QEntity(self.root_entity)
        mesh_entity.addComponent(mesh)

        # Transform
        transform = QTransform()
        mesh_entity.addComponent(transform)

        # Animation
        clip_loader = QAnimationClipLoader()
        clip_loader.setSource(QUrl.fromLocalFile(gltf_path))
        animator = QClipAnimator()
        animator.setClip(clip_loader)
        animator.setRunning(True)
        mesh_entity.addComponent(animator)

        # Show
        self.show()

    def create_gltf(self) -> str:
        gltf = GLTF2()

        # Buffer for positions
        positions = np.array([-1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1],
                             dtype=np.float32)
        buffer_data = positions.tobytes()
        buffer_positions = Buffer(byteLength=len(buffer_data))
        gltf.buffers.append(buffer_positions)

        # BufferView for positions
        buffer_view_positions = BufferView(buffer=0, byteOffset=0, byteLength=len(buffer_data))
        gltf.bufferViews.append(buffer_view_positions)

        # Accessor for positions
        accessor_positions = Accessor(bufferView=0, byteOffset=0, componentType=5126, count=8, type="VEC3")
        gltf.accessors.append(accessor_positions)

        # Animation
        # (Your animation code here)

        # Node with mesh and rotation
        node = Node(rotation=[0.0, 0.0, 0.0, 1.0], mesh=0)
        gltf.nodes.append(node)

        # Mesh with a single position attribute
        gltf.meshes.append({"primitives": [{"attributes": {"POSITION": 0}}]})

        # Scene
        scene = Scene(nodes=[0])
        gltf.scenes.append(scene)
        gltf.scene = 0

        # Save
        gltf_path = "rotating_cube.gltf"
        gltf.save(gltf_path)

        return gltf_path


if __name__ == "__main__":
    app = QApplication([])
    viewer = GLTFViewer()
    app.exec()
