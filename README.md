# 3D_GestureFlow

A 3D particle gesture interaction system built with Three.js + MediaPipe. Features immersive particle effects, photo card browsing, and music playback — all controlled by hand gestures via webcam.

## Demo
<img width="648" height="550" alt="image" src="https://github.com/user-attachments/assets/d3eaa561-ec8d-415e-a9f1-ff635b832392" />
<img width="1490" height="830" alt="image" src="https://github.com/user-attachments/assets/3b34fd85-5572-40c6-a263-73ccdbe7a0d2" />
<img width="1498" height="908" alt="image" src="https://github.com/user-attachments/assets/5f962be7-252e-4d0c-ab70-a2a8f16caeb6" />

## Features

- Outer layer: heart-shaped 3D particle cloud with bloom glow
- Inner layer: wind-blown photo particles
- Photo card carousel: swipe with two fingers, grab to highlight
- Full gesture control — no mouse or keyboard needed
- Custom particle emission color
- Background music player (mp3 / m4a / mp4)

## Gesture Controls

| Gesture | Action |
|---------|--------|
| Five fingers open/close | Particle scale |
| Index finger drag | Rotate view |
| Two fingers swipe | Browse photo cards |
| Three fingers pinch | Grab center card |
| Five fingers fully open (hold) | Show card display |

## Getting Started

### Option 1: Local Server (recommended)

Requires Python 3.

```bash
git clone https://github.com/tuanzi0103/3D_GestureFlow.git
cd 3D_GestureFlow
python3 server.py
```

Open `http://localhost:8080` in your browser.

Place files in the corresponding folders and they load automatically:

| Folder | Content |
|--------|---------|
| `photos/` | Photo cards (jpg / png / webp) |
| `music/` | Background music (mp3 / m4a / mp4) |
| `backgraph/` | Card back images (portrait or landscape) |

### Option 2: Open directly

Open `index.html` directly in your browser and use the buttons at the bottom to upload files manually.

> Note: auto-loading from local folders requires the local server.
> Note: If no images are provided, the photo card system will remain unavailable.

## Tech Stack

- [Three.js](https://threejs.org/) — 3D rendering, particle system, InstancedMesh
- [MediaPipe Hands](https://mediapipe.dev/) — real-time hand gesture recognition
- [Tailwind CSS](https://tailwindcss.com/) — UI styling
- UnrealBloomPass — bloom post-processing

## Requirements

Chrome or Edge (latest) — webcam permission required for gesture recognition.
