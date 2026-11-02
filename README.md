# 🐾 Companion Animal Welfare, Nutrition & Cognitive Enrichment
### Canines, Felines & Lagomorphs — Interactive 3D Technical Masterclass

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-r128-black?logo=three.js&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Modern%20DOM-orange?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Glassmorphism-emerald?logo=css3&logoColor=white)
![Welfare Science](https://img.shields.io/badge/Welfare%20Science-Five%20Domains-green)

A scientifically grounded, standalone 10-slide interactive presentation examining the behavioral science, nutritional physiology, cognitive enrichment, habitat architecture, and lifetime ethical care of **dogs (*Canis lupus familiaris*)**, **cats (*Felis catus*)**, and **rabbits (*Oryctolagus cuniculus*)**.

The presentation features an interactive **3D WebGL organic ecosystem** rendered with **Three.js**, responding to mouse movements and smooth camera transitions across slide topics.

---

## 📸 Presentation Visual Previews

### Slide 01: Holistic Companion Animal Care & The Five Domains
![Slide 1: Holistic Animal Care & Five Domains](https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=1200&q=80)
*The modern Five Domains model of animal welfare: prioritizing positive affective mental states over mere absence of suffering.*

### Slide 03: Canine Cognitive Enrichment & Puzzle Work
![Slide 3: Canine Cognitive Enrichment](https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=1200&q=80)
*Contra-freeloading, olfactory processing (300M receptors), and tiered puzzle progression from lick mats to multi-step locks.*

### Slide 06: Lagomorph Welfare: Delicate Digestive Systems & Hay Diet
![Slide 6: Lagomorph Nutrition & Hay Diet](https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?auto=format&fit=crop&w=1200&q=80)
*Hindgut fermentation, cecotrophy, continuous open-rooted dental wear, and life-saving GI Stasis emergency triage.*

### Slide 09: Multi-Pet Household Management & Safe Coexistence
![Slide 9: Multi-Pet Safe Coexistence](https://images.unsplash.com/photo-1535268647677-300dbf3d78d1?auto=format&fit=crop&w=1200&q=80)
*Managing predator-prey flight triggers between dogs, cats, and rabbits through desensitization and fortified sanctuary zones.*

---

## 🚀 Quickstart Guide

### 1. Requirements
- **Python 3.10+** (uses only standard library modules; **no pip install required**).
- Any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).

### 2. Generate the Presentation
Run the generation script from the project directory:

```bash
# Using standard Python
python generate_presentation.py

# Or using the Python launcher
py generate_presentation.py
```

Expected output:
```text
[*] Building companion animal welfare technical presentation...
[+] Successfully generated standalone presentation: C:\biu01\presentation.html
[+] Total file size: 88,875 bytes
[*] Open 'presentation.html' in any modern browser to view.
```

### 3. View the Presentation
Open `presentation.html` in your browser:

- **Windows**:
  ```powershell
  Start-Process msedge.exe "C:\biu01\presentation.html"
  # Or open in default browser:
  Start-Process presentation.html
  ```
- **macOS**:
  ```bash
  open presentation.html
  ```
- **Linux**:
  ```bash
  xdg-open presentation.html
  ```
- **Optional Local HTTP Server**:
  ```bash
  python -m http.server 8000
  # Then navigate to http://localhost:8000/presentation.html
  ```

---

## 🎮 Navigation & Keyboard Controls

| Input Control | Action |
| :--- | :--- |
| <kbd>→</kbd> / <kbd>↓</kbd> / <kbd>Space</kbd> / <kbd>PageDown</kbd> | Navigate to the **Next Slide** |
| <kbd>←</kbd> / <kbd>↑</kbd> / <kbd>PageUp</kbd> | Navigate to the **Previous Slide** |
| <kbd>Home</kbd> | Jump to **Slide 01** |
| <kbd>End</kbd> | Jump to **Slide 10** |
| **Top Navigation Buttons** | Click **←** or **→** buttons on the top right bar |
| **Bottom Navigation Dots** | Click any dot to jump directly to that slide |
| **Mouse Cursor** | Subtle 3D organic constellation rotation via mouse parallax |
| **Touch / Mobile** | Swipe left or right to switch slides |

---

## 📚 Complete Slide Syllabus

```
├── Slide 01: Holistic Companion Animal Care & Welfare
│   ├── Beyond the Five Freedoms: The Five Domains Model (Mellor et al.)
│   ├── Cognitive agency and 80%+ cortisol reduction
│   └── The Triad of Species-Appropriate Guardianship
│
├── Slide 02: Species-Specific Needs: Dogs vs. Cats vs. Rabbits
│   ├── Facultative omnivore vs. Obligate carnivore vs. Hindgut fermenter
│   ├── Essential nutrients (taurine, preformed Vit A, long-stem silica fiber)
│   └── Divergent evolutionary drivers and illness masking
│
├── Slide 03: Canine Cognitive Enrichment & Puzzle Work
│   ├── Contra-freeloading: why animals prefer working for rewards
│   ├── Olfactory superpower: 220–300M receptors, 15 min sniff = 45 min run
│   └── 3-tier puzzle progression (lick mats → sliders → sequential locks)
│
├── Slide 04: Senior Dog Care: Mobility, Joint Support & Mental Stimulation
│   ├── Multimodal osteoarthritis: anti-NGF monoclonal antibodies (Librela), EPA/DHA
│   ├── Cognitive Dysfunction Syndrome (CDS): DISHA diagnostic framework
│   └── Low-impact geriatric workouts: sniffaris and stationary lick-mats
│
├── Slide 05: Feline Environmental Enrichment & Territory Dynamics
│   ├── 3D vertical territory: cat superhighways, catwalks, and aerial escape perches
│   ├── Predatory sequence: Stare → Stalk → Chase → Pounce → Kill-Bite → Eat
│   ├── Laser pointer syndrome and neurochemical frustration
│   └── The N+1 resource distribution rule for multi-cat homes
│
├── Slide 06: Lagomorph Welfare: Delicate Digestive Systems & Hay Diet
│   ├── Cecotrophy: ingestion of nutrient-rich fermented cecal capsules
│   ├── The 85%+ unprocessed grass hay imperative for continuous dental wear
│   └── GI Stasis emergency pathology: hypomotility, dysbiosis, and 12-hr triage
│
├── Slide 07: Safe Enclosure Architecture & Timber Habitat Design
│   ├── The death of the hutch: minimum 12 sq ft pen + daily free-roam exercise
│   ├── Dual-exit prey hides: preventing panic and spatial entrapment
│   └── Wood toxicity matrix: safe timbers (apple, willow) vs. toxic (cedar, cherry, oak)
│
├── Slide 08: Behavioral Enrichment: Foraging, Chewing & Scent Work
│   ├── Ethological deprivation and stereotypic displacement behaviors
│   ├── Natural time budgets: 70% daily wild foraging vs. <15 min bowl feeding
│   └── Cross-species foraging: KONGs, puzzle mice, and lagomorph dig boxes
│
├── Slide 09: Multi-Pet Household Management & Safe Coexistence
│   ├── The predatory flight trigger: why "gentle" pets react to rabbit hops
│   ├── Sanctuary zone architecture: fortified, dog/cat-proof safe rooms
│   └── 4-stage systematic desensitization protocol (scent → barrier → leash → space)
│
└── Slide 10: Lifetime Commitment: Preventative Health & Quality of Life
    ├── Proactive geriatric wellness: dental prophylaxis and annual blood panels
    ├── Body Condition Scoring (BCS target 4.5/9)
    ├── The HHHHHMM Quality of Life scale (Dr. Alice Villalobos)
    └── Ethical covenant: guardianship as compassionate lifetime stewardship
```

---

## 🎨 3D WebGL Technical Design

The background animation is built natively in Three.js and features:
- **900 Point Particles** procedurally clustered around 5 biological centroids.
- **5 Semantic Color Schemes**:
  - Warm Amber / Gold (`#f59e0b`): Canine Vitality & Scentwork
  - Emerald Green (`#10b981`): Feline Grace & Agility
  - Sage / Olive (`#84cc16`): Lagomorph Earth & Nutrition
  - Cyan / Turquoise (`#06b6d4`): Cognitive Spark & Puzzles
  - Rose / Coral (`#f43f5e`): Welfare Science & Compassion
- **Dynamic Ecosystem Graph Edges**: Connecting nearby nodes within clusters with inter-species connecting lines.
- **Damped Parallax Lerp**: Camera smoothly tracks cursor movements with linear interpolation (`camera.position += target * 0.04`).
- **Slide-Reactive Viewpoint Shifts**: Navigating between slides glides the camera through different sectors of the organic constellation.

---

## 📂 Project Structure

```
C:\biu01\
├── generate_presentation.py   # Standalone Python generator script
├── presentation.html          # Generated standalone interactive presentation
├── PRD.md                     # Comprehensive Product Requirements Document
└── README.md                  # Detailed repository documentation
```

---

## 🛠️ Verification & Acceptance Testing

```powershell
# 1. Run the Python generator
python generate_presentation.py

# 2. Check generated file size
Get-Item presentation.html | Select-Object Name, Length, LastWriteTime

# 3. Launch presentation in your Chromium browser
Start-Process msedge.exe "C:\biu01\presentation.html"
```

---

## 📄 License
This project is licensed under the MIT License — open for academic, educational, and non-profit animal rescue use.
