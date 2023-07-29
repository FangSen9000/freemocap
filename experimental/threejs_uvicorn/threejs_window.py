import sys
import argparse
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

# Sample HTML content for Three.js animation
HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Three.js Basic Animation</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Function to set up the scene, camera, and renderer
        function init() {
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 5;
            const renderer = new THREE.WebGLRenderer();
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);
            const geometry = new THREE.BoxGeometry();
            const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
            const cube = new THREE.Mesh(geometry, material);
            scene.add(cube);

            function render() {
                requestAnimationFrame(render);
                cube.rotation.x += 0.01;
                cube.rotation.y += 0.01;
                renderer.render(scene, camera);
            }

            render();
        }

        window.onload = init;
    </script>
</body>
</html>
"""

class ThreeJSWindow(QMainWindow):
    def __init__(self, html_path=None):
        super().__init__()
        self.setWindowTitle("Three.js Animation")
        self.setGeometry(100, 100, 800, 600)

        # Create a QWebEngineView to display the web content
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        if html_path is None:
            # Use the sample HTML content if no path is specified
            self.web_view.setHtml(HTML_CONTENT)
        else:
            # Load the HTML content from the specified file
            url = QUrl.fromLocalFile(html_path)
            self.web_view.setUrl(url)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = ThreeJSWindow()
    window.show()
    sys.exit(app.exec())
