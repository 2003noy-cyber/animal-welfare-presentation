# Documentation: 3D Rabbit Feature in `presentation (1).html`

## Overview

This document records the prompt given to the AI coding agent (Antigravity) and the agent's summary of the changes it made to the file `presentation (1).html`.

---

## 1. The Prompt

```
In the file presentation (1).html there is a 3D rabbit that runs along the bottom
of the screen and appears on every slide. I want to change its behavior as follows:

1. Free movement: The rabbit should roam freely across the entire screen (not just
   the bottom), in all directions. The motion should look natural and smooth: it
   changes direction every so often, turns to face the direction it is running
   (rotating the 3D model accordingly), and never leaves the screen bounds.

2. Persistence: The rabbit must keep appearing on all slides, including during
   slide transitions, and must not disappear, reset, or reload when the slide
   changes. Keep a single rabbit instance and render it in a fixed overlay layer
   above the slides.

3. Jump on click: When the user clicks (or taps) the rabbit, it performs a jump
   animation (up and back down, with a natural arc) and then continues running as
   before. Use raycasting or the existing click handling to detect clicks on the
   3D model itself, not on its bounding box or the whole canvas.

4. No interference with the presentation: Clicking the rabbit must not trigger
   slide navigation, and the rabbit's canvas/overlay must not block clicks on the
   slide content. For example, use pointer-events: none on the overlay and handle
   rabbit hit-testing separately, or enable pointer events only when the pointer
   is over the rabbit.

Keep the existing presentation code intact and change only what is required for
the rabbit. If the rabbit uses an existing animation (run cycle), reuse it for
the movement and add the jump as a separate animation or a programmatic motion.
At the end, briefly explain what you changed.
```

---

## 2. The Agent's Response: Summary of Changes

### 1. Fixed Overlay Layer (`#rabbit-overlay-canvas`)

- Replaced the previous 2D emoji script with a dedicated WebGL canvas layer styled with `position: fixed`, `z-index: 1000`, and `pointer-events: none`.
- The canvas renders a single persistent 3D rabbit mascot that stays above all slides, remains active during slide transitions, and never reloads or resets between slides.

### 2. Full-Screen Free Movement and Boundary Clamping

- The rabbit roams freely across the entire screen in all directions (360°).
- A steering system periodically chooses new screen targets and anticipates screen boundaries (140px buffer) to smoothly turn away toward the interior.
- Smooth angular damping ensures natural turns while the 3D model continuously rotates (`yawGroup.rotation.z`) to face its forward travel direction.
- Strict screen margin clamping (65px) ensures the model never leaves the viewport, adapting dynamically to window resizing.

### 3. 3D Model and Procedural Run Cycle

- Created a stylized 3D rabbit using Three.js standard geometries (ellipsoid torso, chest, head, snout, nose, glossy eyes with catchlights, articulated ears, front paws, hind haunches, and a fluffy tail) with warm earth-toned materials matching the presentation palette.
- Implemented a continuous run cycle with body bobbing, alternating leg pivots, ear inertia bounce, and tail movement.

### 4. Mesh-Level Raycasting and Jump Animation

- Implemented `checkRabbitModelHit()` using `THREE.Raycaster` against the rabbit's actual 3D mesh components rather than a bounding box or canvas.
- On click or tap, the rabbit executes a natural parabolic arc jump with a mid-air "binky" twist, ear flutter, stretched leg postures, and a landing squash before seamlessly resuming its run.
- Hovering over the rabbit updates the cursor to `pointer` for visual feedback.

### 5. No Interference with the Presentation

- The overlay canvas has `pointer-events: none`, allowing clicks, text selection, and slide controls beneath it to operate unimpeded.
- Rabbit clicks are captured in the event capture phase (`capture: true`) with `stopPropagation()`, `stopImmediatePropagation()`, and `preventDefault()`, ensuring that clicking the rabbit triggers its jump without triggering slide navigation or activating underlying slide elements.
