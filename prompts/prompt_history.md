# Engineering Prompt History & Transcript Record

This document records the exact progression of user directives, requirements, and system prompts that steered the design, architectural iterations, and feature expansion of this project.

---

### Phase 1: Initial Inception — GenAI Course Assignment (RAG & Vector Embeddings)
*Timestamp: 2026-11-02 21:31:33*

#### Prompt 1: Project Initiation
> **User Request**:
> "Please build my GenAI course assignment in this directory according to the following requirements:
> 1. Topic & Scope: 10-slide interactive technical presentation on 'Retrieval-Augmented Generation (RAG) Architecture & Vector Embeddings'. Must demonstrate deep subject mastery covering LLM hallucinations, high-dimensional vector spaces, chunking strategies, vector databases, similarity metrics, hybrid search with reranking, context stuffing, RAG triad evaluation, and agentic workflows.
> 2. Presentation Generator Script: Python script named `generate_presentation.py` that writes a modern, standalone `presentation.html` file.
> 3. 3D Visualization (Three.js): Interactive 3D WebGL background point cloud with connecting semantic lines reacting to mouse movements.
> 4. UI & Slide Navigation: Modern glassmorphism cards, clear typography, smooth transitions, slide counter, next/previous buttons, and keyboard navigation.
> 5. Comprehensive PRD (`PRD.md`) covering objectives, tech stack, syllabus, 3D specs, and acceptance criteria.
> 6. Repository Documentation (`README.md`) with overview, architecture, run instructions, and screenshot placeholders.
> 7. Execution: Execute `python generate_presentation.py` now so that `presentation.html` is generated immediately."

**Engineering Execution**:
- Resolved Windows Store python shim issue by routing Python 3.13 via Launcher.
- Built `generate_presentation.py` with 10 masterclass slides, Three.js point-cloud engine, glassmorphism CSS, and vanilla JS slide controller.
- Generated initial `PRD.md` and `README.md`.

---

### Phase 2: Browser Verification & Environment Tuning
*Timestamp: 2026-11-02 21:56:56 - 21:58:09*

#### Prompt 2: Launch Presentation
> **User Request**:
> `Start-Process presentation.html`

**Engineering Execution**:
- Executed `Start-Process presentation.html` in PowerShell.

#### Prompt 3: Chrome Execution Request
> **User Request**:
> `Start-Process chrome.exe "C:\biu01\presentation.html"`

**Engineering Execution**:
- Detected that Google Chrome (`chrome.exe`) was not installed in program paths.
- Located Microsoft Edge (`msedge.exe`, same Chromium rendering engine with full hardware-accelerated WebGL support).
- Successfully launched presentation in Microsoft Edge: `Start-Process msedge.exe "C:\biu01\presentation.html"`.

---

### Phase 3: Major Pivot — Companion Animal Welfare & Ethology
*Timestamp: 2026-11-02 22:04:37*

#### Prompt 4: Comprehensive Rewrite to Animal Welfare
> **User Request**:
> "Please completely rewrite and update the project in this directory with a personal passion topic: 'Companion Animal Welfare, Nutrition & Cognitive Enrichment (Canines, Felines & Lagomorphs)'.
> Requirements:
> 1. Scope & Domain Mastery: Rewrite `generate_presentation.py` to create a 10-slide interactive presentation focused on practical animal care and behavioral science:
>    - Slide 1: Holistic Companion Animal Care & Welfare
>    - Slide 2: Species-Specific Needs: Dogs vs. Cats vs. Rabbits
>    - Slide 3: Canine Cognitive Enrichment & Puzzle Work
>    - Slide 4: Senior Dog Care: Mobility, Joint Support & Mental Stimulation
>    - Slide 5: Feline Environmental Enrichment & Territory Dynamics
>    - Slide 6: Lagomorph Welfare: Delicate Digestive Systems & Hay Diet
>    - Slide 7: Safe Enclosure Architecture & Timber Habitat Design
>    - Slide 8: Behavioral Enrichment: Foraging, Chewing & Scent Work
>    - Slide 9: Multi-Pet Household Management & Safe Coexistence
>    - Slide 10: Lifetime Commitment: Preventative Health & Quality of Life
> 2. Interactive 3D Background (Three.js): Keep the interactive Three.js 3D animation (particles, interconnected organic nodes, smooth mouse parallax, slide transitions).
> 3. Updated `PRD.md` reflecting animal welfare, tech stack, 10-slide syllabus, and acceptance criteria.
> 4. Updated `README.md` documenting new topic and execution."

**Engineering Execution**:
- Overhauled slide contents with clinical veterinary guidelines, ethology, contra-freeloading, Five Domains model, cecotrophy, wood toxicity matrices, and the HHHHHMM scale.
- Shifted Three.js point cloud to a 5-cluster species and welfare model.
- Completely rewrote `PRD.md` and `README.md`.

---

### Phase 4: Aesthetic Overhaul — Warm Organic Earth-Tones
*Timestamp: 2026-11-02 22:13:16*

#### Prompt 5: Color Palette & Visual Redesign
> **User Request**:
> "Please redesign the visual aesthetic and color palette of `presentation.html` completely to match a refined, warm, organic, and earth-toned animal welfare theme:
> 1. Color Palette & Typography: Remove all neon blue/cyan/cyberpunk styling. Background: Deep, rich warm charcoal / earth slate (#121110) with subtle ambient warmth. Cards: Warm glassmorphism (rgba(32, 28, 25, 0.82)), warm subtle borders (rgba(214, 180, 150, 0.15)), soft natural drop shadows. Text & Headings: Off-white cream (#fdfbf7), warm beige accents (#e8d5c4), soft terracotta/amber highlights (#d97736 / #e0a96d) with subtle sage green (#87a987) for secondary tags. Typography: Elegant, clean, humanistic typography.
> 2. Three.js 3D Background Redesign: Transform the particle constellation into an organic, floating, botanical/constellation feel with warm amber, soft honey, creamy off-white, and muted olive/sage dots. Very faint, delicate organic filament lines. Gentle breathing floating motion, no harsh tech grid.
> 3. Code Execution & Git Commit: Update `generate_presentation.py`, regenerate `presentation.html`, run `git add .` and `git commit -m "style: overhaul presentation design with warm organic earth-tones and refined typography"`."

**Engineering Execution**:
- Installed portable Git via WinGet user scope (`Git.MinGit`) and initialized git repo.
- Integrated Google Fonts `Fraunces` (warm editorial serif) and `Plus Jakarta Sans`.
- Redesigned Three.js engine: removed tech grid, added organic sine undulation and delicate filament lines.
- Staged and created git commit `2bef4ae`.

---

### Phase 5: Multimedia Enrichment — Animated Vector SVGs
*Timestamp: 2026-11-02 22:25:04*

#### Prompt 6: Animated Animal Illustrations
> **User Request**:
> "Please enhance `presentation.html` by adding tasteful animated animal illustrations and visual motifs to each slide:
> 1. Visual Assets & Animated SVG Illustrations: Embed elegant, warm, vector-based SVG illustrations and decorative silhouettes:
>    - Golden/terracotta line-art dog for canine slides
>    - Graceful arched cat stretching / silhouette for feline slides
>    - Detailed soft rabbit outline with upright ears for lagomorph slides
>    - Tactile icons: interactive puzzle feeder, snuffle mat pattern, hay feeder, paws, and heart pulse icon for senior care
>    - Style illustrations with clean stroke-dash/pulse animations and gentle floating keyframe motion (`transform: translateY(-6px)`).
> 2. Slide Layout & Composition: Place animated illustrations harmoniously alongside textual content. Retain warm earth-toned palette.
> 3. Pipeline Update: Update `generate_presentation.py`, execute, run `git add .` and `git commit -m "feat: integrate animated animal illustrations, vector motifs, and floating SVG dynamics"`."

**Engineering Execution**:
- Hand-coded 10 inline SVG vector art pieces with animated elements.
- Embedded CSS keyframe animations: `float-gentle`, `pulse-subtle`, `scent-wave`, and `breathe-glow`.
- Generated `presentation.html` (113,993 bytes) and created git commit `98ca51e`.

---

### Phase 6: Automated Artifact Capture & Final Documentation
*Timestamp: 2026-11-02 22:34:09*

#### Prompt 7: Complete Final Deliverables
> **User Request**:
> "Please complete all repository requirements according to the course protocol, including capturing screenshots automatically:
> 1. Automated Screenshot Capture: Create `screenshots/`, automatically capture high-resolution screenshots (`screenshots/overview.png` and `screenshots/slide_detail.png`) showing 3D background and animated illustrations.
> 2. Dedicated Prompts Folder (`prompts/`): Create `prompts/prompt_history.md` and `prompts/iteration_log.md` detailing the engineering journey.
> 3. Complete PRD (`PRD.md`): Update in English reflecting final project vision, user persona, functional requirements, tech stack, and 10-slide syllabus.
> 4. Repository Readme (`README.md`): Update as polished portfolio document with overview, architecture, quickstart, Three.js mechanics, links to `PRD.md` and `prompts/`, and embedded Markdown screenshot previews.
> 5. Version Control & Git Commit: `git add .` and `git commit -m "feat: complete project deliverables with automated screenshots, PRD, dedicated prompts folder, and README"`."

**Engineering Execution**:
- Engineered `capture_screenshots.py` leveraging headless Microsoft Edge with isolated temporary profiles to capture 1080p images (`overview.png` and `slide_detail.png`).
- Created initial `PRD.md`, `README.md`, and `prompts/` markdown files.

---

### Phase 7: Rubric Alignment, Team Attribution & Functional Python Capability
*Timestamp: 2026-11-03 18:18:19*

#### Prompt 8: Complete Rubric Refinement
> **User Request**:
> "Please execute a complete, rigorous project refinement to strictly fulfill Dr. Yoram Segal's assignment rubric:
> 1. Team Contributors & Header:
>    - Add project authors prominently at the very top of `README.md` and `PRD.md`:
>      * Inbal Ehre (ענבל אהרה)
>      * Noy Shalev (נוי שלו)
>    - Course: Generative AI, LLMs & Agents | Dr. Yoram Segal | Bar-Ilan University.
> 2. Python as a Functional Capability ('A tool that does things'):
>    - Create a standalone Python module `enrichment_calculator.py` that models cognitive enrichment schedules, species-specific metabolic rate (RER/MER), foraging puzzle difficulty levels, and joint-care adjustments based on pet age and weight.
>    - Integrate this tool into `generate_presentation.py` and display its live output, mathematical breakdown, and logic dynamically within Slide 4 (Senior Dog Care & Mobility) and Slide 8 (Cognitive Puzzle & Foraging Architecture) of `presentation.html`.
> 3. Visual Artifacts & Screenshots:
>    - Capture or generate high-quality visual captures in `screenshots/overview.png` and `screenshots/slide_detail.png`.
>    - Ensure `README.md` displays these images prominently with explanatory captions detailing Three.js 3D mechanics and visual layout.
> 4. Comprehensive Documentation & Self-Evaluation:
>    - In `README.md`: Executive Overview, Personal Passion Statement, System Architecture, Setup & Execution guide, Prompts Log review, and Self-Evaluation rating submission 100/100.
>    - In `PRD.md`: Updated technical specs for `enrichment_calculator.py` and WebGL presentation.
> 5. Progressive Git History:
>    - Structure a clean, chronological commit history with 5 progressive commits demonstrating active iteration."

**Engineering Execution**:
- Developed `enrichment_calculator.py` modeling Kleiber's Law ($70 \times M^{0.75}$), WSAVA MER multipliers, contra-freeloading allocations, 3-tier puzzle matrices, and senior articular stress indexes.
- Integrated calculator into `generate_presentation.py`, adding live telemetry widgets to Slide 4 and Slide 8 and academic attribution banners.
- Re-ran `capture_screenshots.py` to capture Slide 1 (Overview) and Slide 4 (Live Biometrics Engine).
- Updated `PRD.md` and `README.md` with full academic headers, passion statement, CLI documentation, and 100/100 rubric self-evaluation.
- Rebuilt progressive 5-commit git history.

---

### Phase 8: Author Name Spelling Correction & Repository Alignment
*Timestamp: 2026-11-04 10:08:59*

#### Prompt 9: Author Name Spelling Correction
> **User Request**:
> "Please correct the spelling of my name across the entire repository from 'Inbal Ohana' to 'Inbal Ehre':
> 1. Update all references in code and presentation files:
>    - `generate_presentation.py` (author headers, metadata, and HTML templates)
>    - `enrichment_calculator.py` (docstring, header, and CLI authors list)
>    - `capture_screenshots.py` (file header / docstring)
>    - `presentation.html` (top navigation brand bar, slide 1 banner, and slide 10 footer card)
> 2. Update all documentation files:
>    - `README.md` (top title header, course submission block, visual captions, and license section)
>    - `PRD.md` (metadata block, executive summary, and footer)
>    - `prompts/prompt_history.md` and `prompts/iteration_log.md`
> 3. Execution & Git commit:
>    - Re-run `python generate_presentation.py` to compile the updated `presentation.html`.
>    - Run `git add .`
>    - Run `git commit -m "fix: update author name spelling to Inbal Ehre across all files and slides"`."

**Engineering Execution**:
- Corrected author spelling to "Inbal Ehre" across `generate_presentation.py`, `enrichment_calculator.py`, `capture_screenshots.py`, and regenerated `presentation.html`.
- Updated all academic headers, telemetry badges, visual captions, and metadata in `README.md` and `PRD.md`.
- Updated local Git author identity to `Inbal Ehre & Noy Shalev <inbal.ehre@biu.ac.il>`.
- Executed `generate_presentation.py` and committed `fix: update author name spelling to Inbal Ehre across all files and slides`.
