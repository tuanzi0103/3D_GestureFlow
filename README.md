# GestureFlow 3D

> A real-time hand gesture controlled 3D particle interaction system built with Three.js and MediaPipe.

GestureFlow 3D combines particle simulation, computer vision, and immersive interaction into a browser-based experience. Users can manipulate a dynamic particle universe, browse photo cards, and control visual effects entirely through hand gestures captured by a webcam.

---

## Demo

### Particle Universe

![Particle Universe](assets/demo-particles.gif)

### Gesture Interaction

![Gesture Interaction](assets/demo-gesture.gif)

### Photo Card Carousel

![Photo Card Carousel](assets/demo-cards.gif)

---

## Features

### Interactive Particle System

* Heart-shaped 3D particle cloud
* Bloom glow post-processing
* Dynamic particle scaling
* Custom particle emission colors
* GPU-accelerated rendering with InstancedMesh

### Gesture Recognition

* Real-time hand tracking using MediaPipe Hands
* Webcam-based interaction
* Smooth gesture state detection
* Fully hands-free control

### Photo Card Experience

* Particle-based photo generation
* Swipeable photo carousel
* Card selection and highlighting
* Dynamic image loading

### Multimedia Support

* Background music playback
* MP3 / M4A / MP4 support
* Automatic media discovery in local server mode

---

## 🖐 Gesture Controls

| Gesture                        | Action                  |
| ------------------------------ | ----------------------- |
| Five fingers open / close      | Scale particle universe |
| Index finger drag              | Rotate camera view      |
| Two-finger swipe               | Browse photo cards      |
| Three-finger pinch             | Select center card      |
| Five fingers fully open (hold) | Enter card display mode |

---

## Project Structure

```text
GestureFlow 3D
│
├── photos/          # Photo card images
├── music/           # Background music
├── backgraph/       # Card back images
│
├── index.html
├── server.py
└── assets/
    ├── demo-particles.gif
    ├── demo-gesture.gif
    └── demo-cards.gif
```

---

## Tech Stack

### Frontend

* Three.js
* JavaScript (ES6+)
* Tailwind CSS

### Computer Vision

* MediaPipe Hands

### Graphics

* WebGL
* InstancedMesh
* UnrealBloomPass

---

## Getting Started

### Option 1 — Local Server (Recommended)

Requires Python 3.

```bash
git clone https://github.com/tuanzi0103/3D_GestureFlow.git

cd 3D_GestureFlow

python3 server.py
```

Open:

```text
http://localhost:8080
```

---

## 📂 Asset Loading

Place assets into the following folders:

| Folder     | Content                 |
| ---------- | ----------------------- |
| photos/    | JPG / PNG / WEBP images |
| music/     | MP3 / M4A / MP4 audio   |
| backgraph/ | Card background images  |

Assets are automatically loaded when the local server starts.

Before using card browsing features:

1. Add images to the `photos/` folder when running the local server.
2. Or upload images manually through the interface after launch.

If no images are provided, the photo card system will remain unavailable.

---

## 🌐 Option 2 — Open Directly

Open `index.html` directly in your browser.

In this mode:

* Photos must be uploaded manually
* Music files must be uploaded manually
* Automatic folder scanning is unavailable

---

## 💻 Browser Requirements

Recommended browsers:

* Google Chrome (Latest)
* Microsoft Edge (Latest)

Requirements:

* Webcam permission enabled
* WebGL supported

---
