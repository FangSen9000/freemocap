from PyQt6.QtWebEngineWidgets import QWebEngineView
from fastapi import FastAPI
from fastapi.responses import FileResponse
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
import uvicorn
import threading




# FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse('html/webgl_geometry_spline_editor.html')

# Function to run FastAPI server
def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Function to run PyQt6 app
def run_qt_app():
    app = QApplication([])

    view = QWebEngineView()
    view.load(QUrl("http://127.0.0.1:8000")) # URL of the FastAPI server
    view.show()

    app.exec()

if __name__ == "__main__":
    # Create index.html file


    # Start FastAPI server in a separate thread
    threading.Thread(target=run_server).start()

    # Run PyQt6 application
    run_qt_app()
