# Product Requirements Document (PRD)

## Project: Companion Animal Welfare, Nutrition & Cognitive Enrichment (Canines, Felines & Lagomorphs) — Interactive Technical Masterclass

### Academic Project Information
- **Course**: Generative AI, LLMs & Agents
- **Faculty / Institution**: Bar-Ilan University (BIU)
- **Instructor**: Dr. Yoram Segal
- **Authors**:
  - **Inbal Ehre** (ענבל אהרה)
  - **Noy Shalev** (נוי שלו)
- **Topic**: Companion Animal Welfare, Nutrition & Cognitive Enrichment (Canines, Felines & Lagomorphs)
- **Repository Artifacts**: `enrichment_calculator.py`, `generate_presentation.py`, `presentation.html`, `capture_screenshots.py`, `PRD.md`, `README.md`, `prompts/`, `screenshots/`

---

### 1. Executive Summary & Vision

#### 1.1 Executive Summary
Human guardianship of companion animals has advanced dramatically over the past two decades, transitioning from basic disease management and physical containment toward an evidence-based, compassionate behavioral and nutritional science. Millions of dogs (*Canis lupus familiaris*), cats (*Felis catus*), and rabbits (*Oryctolagus cuniculus*) live in domestic environments that frequently fail to satisfy their evolutionary ethology, resulting in chronic stress, destructive stereotypies, obesity, and premature mortality.

This project delivers a **10-slide, interactive, standalone technical presentation** titled *"Companion Animal Welfare, Nutrition & Cognitive Enrichment (Canines, Felines & Lagomorphs)"*, accompanied by a **functional Python calculation engine** (`enrichment_calculator.py`). Designed for veterinary professionals, companion animal behaviorists, rescue directors, and devoted guardians, this masterclass provides an exhaustive, scientifically rigorous examination of species-appropriate biological care, cognitive stimulation, and modern welfare philosophy.

The entire masterclass is built and exported deterministically by `generate_presentation.py`, which integrates the real-time mathematical outputs of `enrichment_calculator.py` into a zero-dependency, self-contained `presentation.html` document with an interactive 3D WebGL organic point-cloud background powered by Three.js, embedded animated SVG illustrations, and responsive warm glassmorphic layout cards.

#### 1.2 Target User Personas
- **The Veterinary Professional & Clinic Educator**: Seeking evidence-based visual materials and mathematical models to communicate the Five Domains model, multimodal osteoarthritis analgesia, RER/MER metabolic budgeting, and lagomorph GI stasis pathophysiology to clients.
- **The Companion Animal Behaviorist / Trainer**: Requiring structured quantitative frameworks for canine contra-freeloading, feline 3D vertical territory planning, and interspecies desensitization protocols.
- **The Dedicated Companion Guardian**: Passionate about optimizing the biological and emotional flourishing of multi-pet households, seeking actionable habitat proofing, joint preservation, and enrichment blueprints.

---

### 2. Technology Stack & Architectural Specifications

| Component | Technology | Rationale & Specification |
| :--- | :--- | :--- |
| **Functional Tool** | Python 3.10+ Standard Library (`math`, `json`, `argparse`) | `enrichment_calculator.py`: models RER/MER metabolic energetics, contra-freeloading caloric splits, 3-tier puzzle scheduling, and senior joint load scoring. |
| **Generator Script** | Python 3.10+ Standard Library (`pathlib`, `sys`) | Zero external pip dependencies; deterministic file generation; cross-platform execution; imports and evaluates calculator logic. |
| **Presentation Engine** | Vanilla ES6+ JavaScript & HTML5 DOM | High performance, instant hydration, zero framework overhead (no React/Vue runtime). |
| **3D WebGL Graphics** | Three.js (r128 via CDN) | Hardware-accelerated botanical point-cloud, glowing radial sprites, delicate organic filaments, and damped camera lerp. |
| **Vector Illustrations** | Custom Embedded SVG + CSS Keyframes | Lightweight vector line-art with smooth floating breathing motion (`float-gentle`), cardiac pulses, and scent diffusion waves. |
| **Typography & Styling** | CSS3 Modern Specifications | Warm glassmorphism (`backdrop-filter: blur(28px)`), CSS Grid/Flexbox layouts, warm earth-toned palette (`#121110`, `#fdfbf7`, `#e0a96d`, `#d97736`, `#87a987`), and Google Fonts (`Fraunces`, `Plus Jakarta Sans`, `JetBrains Mono`). |
| **Automated Capture** | Python + Headless Chromium (Microsoft Edge) | Headless 1080p slide screenshot capture via isolated temporary profiles. |

---

### 3. Functional Python Capability: `enrichment_calculator.py`

To satisfy the rubric requirement of Python as a functional tool ("a tool that does things"), `enrichment_calculator.py` was developed as a standalone veterinary science analytics engine:

#### 3.1 Mathematical & Physiological Models
1. **Resting Energy Requirement (RER)**:
   Calculated using Kleiber's allometric scaling law endorsed by the World Small Animal Veterinary Association (WSAVA):
   $$\text{RER (kcal/day)} = 70 \times (\text{Mass}_{\text{kg}})^{0.75}$$
2. **Maintenance Energy Requirement (MER)**:
   Species and life-stage multipliers applied to RER:
   - *Canines*: Puppies ($2.5\times$), Adult intact ($1.8\times$), Adult neutered ($1.6\times$), Senior ($1.2\times$–$1.4\times$).
   - *Felines*: Kittens ($2.2\times$), Adult ($1.2\times$), Senior ($1.1\times$).
   - *Lagomorphs*: Juvenile ($2.0\times$), Adult maintenance ($1.5\times$), with mandatory $\ge 85\%$ long-stem indigestible fiber baseline.
3. **Contra-Freeloading & Foraging Calorie Split**:
   Allocates 25% to 35% of daily MER to cognitive puzzles, snuffle mats, and scatter feeds, dividing the remaining calories into base satiety meals.
4. **Three-Tier Cognitive Puzzle Scheduling**:
   Progresses animals from Level 1 (licking, snuffling mats) through Level 2 (sliding tiles, rotary wobblers) to Level 3 (multi-step locks and scent discrimination).
5. **Geriatric Joint Stress & "Sniffari" Biomechanical Protocol**:
   Calculates an articular load index (0–100) based on pet age, weight, and orthopedic severity (e.g. osteoarthritis), computing the optimal duration for low-impact olfactory "sniffaris" where 15–20 minutes of sniffing delivers cognitive exhaustion equivalent to 45–60 minutes of high-impact running without articular damage.

#### 3.2 Presentation Integration
`generate_presentation.py` directly imports `CompanionEnrichmentCalculator` and generates dynamic, glassmorphic UI telemetry cards:
- **Slide 4 (Senior Dog Care & Mobility)**: Displays live RER, Senior MER, Joint Load Index, Sniffari duration, and orthopedic bedding/ramp prescriptions.
- **Slide 8 (Cognitive Puzzle & Foraging Architecture)**: Displays total MER, Contra-freeloading caloric allocation, cognitive tier schedule, and prescribed apparatus.

---

### 4. Detailed Slide-by-Slide Syllabus (10 Slides)

#### Slide 1: Holistic Companion Animal Care & Welfare
- **Theme**: Welfare Science & Paradigm Evolution.
- **Learning Objectives**: Understand the shift from traditional "Five Freedoms" to the contemporary **Five Domains Model** (Mellor et al.); evaluate the role of positive affective states and agency in long-term health.
- **Content Outline**:
  - The Five Domains Model: Nutrition, Physical Environment, Health, Behavioral Interactions, and Positive Mental State.
  - Cognitive Agency & Stress Reduction: Demonstrating that perceived control over environment reduces chronic cortisol levels by $>80\%$.
  - The Triad of Species-Appropriate Guardianship: Biological integrity $\to$ Environmental sanctuary $\to$ Cognitive agency $\to$ Interspecies trust $\to$ Flourishing longevity.
  - Prominent Academic Project Banner: Inbal Ehre & Noy Shalev, Dr. Yoram Segal, Bar-Ilan University.
- **Visuals**: Animated botanical wreath SVG framing line-art dog, cat, and rabbit with central pulsing welfare heart; 5-step holistic care pipeline; welfare metric telemetry badges.

#### Slide 2: Species-Specific Needs: Dogs vs. Cats vs. Rabbits
- **Theme**: Comparative Biology & Evolutionary Ecology.
- **Learning Objectives**: Master divergent digestive, nutritional, social, and sensory adaptations across canines, felines, and lagomorphs.
- **Content Outline**:
  - **Canines (*Canis lupus familiaris*)**: Facultative carnivores / opportunistic omnivores; flexible macronutrient assimilation; cooperative group sociality; mutual gaze oxytocin feedback loop.
  - **Felines (*Felis catus*)**: Strict obligate carnivores requiring mandatory dietary taurine, arachidonic acid, and preformed vitamin A; solitary territorial hunters; vertical space orientation.
  - **Lagomorphs (*Oryctolagus cuniculus*)**: Crepuscular colonial prey animals; hindgut fermenters requiring continuous indigestible long-stem roughage; non-vocal communication and acute illness masking.
- **Visuals**: Tripartite species medallion SVG banner; comprehensive comparative taxonomy table across Diet, Nutrients, Social Model, and Sensory Priorities.

#### Slide 3: Canine Cognitive Enrichment & Puzzle Work
- **Theme**: Canine Cognition & Olfactory Enrichment.
- **Learning Objectives**: Apply the contra-freeloading phenomenon and olfactory neuro-processing to structure progressive canine mental workouts.
- **Content Outline**:
  - Contra-freeloading: Domestic dogs actively prefer working for food rewards over free-feeding from stationary bowls.
  - Olfactory Processing: 220–300 million olfactory receptors; 15 minutes of scent search induces neurochemical fatigue equivalent to 45 minutes of aerobic running.
  - Tiered Puzzle Progression:
    - *Level 1*: Licking and snuffling mats releasing calming endorphins.
    - *Level 2*: Mechanical sliders, wobblers, and rolling dispensers.
    - *Level 3*: Multi-step sequential locks requiring spatial memory and impulse restraint.
- **Visuals**: Animated canine snout tracking moving scent-waves to a multi-tiered rotating puzzle board; 3-stage puzzle progression funnel.

#### Slide 4: Senior Dog Care: Mobility, Joint Support & Mental Stimulation
- **Theme**: Geriatric Medicine, Neuro-Preservation & Biometrics.
- **Learning Objectives**: Formulate multimodal osteoarthritis management protocols, identify early Cognitive Dysfunction Syndrome (CDS), and evaluate mathematical joint load profiles.
- **Content Outline**:
  - Multimodal Osteoarthritis (OA) Management: Anti-NGF monoclonal antibodies (bedinvetmab / Librela), marine omega-3 fatty acids (EPA/DHA $>100\text{ mg/kg}$), joint chondroprotectants (UC-II), non-slip environmental floor modifications.
  - Cognitive Dysfunction Syndrome (CDS / "Canine Alzheimer's"): Diagnostic evaluation via the **DISHA** framework (Disorientation, Interactions altered, Sleep-wake cycles, House soiling & Activity).
  - Low-impact geriatric cognitive exercise: "Sniffaris" (slow scent walks) and stationary lick-mats.
  - **Live Python Engine Telemetry**: Real-time integration of `enrichment_calculator.py` outputs for senior canine profiles (RER, MER, Joint Load Index, Sniffari pacing, and foam depth).
- **Visuals**: Senior dog resting on an orthopedic bolster bed with joint warmth rings and ECG pulse wave; DISHA diagnostic grid; live Python calculation telemetry card.

#### Slide 5: Feline Environmental Enrichment & Territory Dynamics
- **Theme**: Feline Ethology & Spatial Engineering.
- **Learning Objectives**: Architect 3D vertical territory, satisfy predatory motor patterns, and prevent feline inter-cat resource friction.
- **Content Outline**:
  - 3D Vertical Territory: Cats experience living spaces in cubic volume rather than square footage. Cat superhighways, floating catwalks, and elevated vantage points mitigate inter-cat territorial conflicts.
  - The Full Predatory Motor Pattern:
    $$\text{Stare} \to \text{Stalk} \to \text{Chase} \to \text{Pounce} \to \text{Kill-Bite} \to \text{Eat/Groom}$$
  - Laser Pointer Syndrome: Neurochemical frustration caused by non-catchable light beams; mandatory transition to physical feathered/plush prey.
  - The $N+1$ Resource Rule: Dispersing litter boxes, water fountains, and scratching posts across separate rooms.
- **Visuals**: Arched stretching cat climbing staggered floating catwalks toward a feather wand toy; 6-step predatory sequence diagram.

#### Slide 6: Lagomorph Welfare: Delicate Digestive Systems & Hay Diet
- **Theme**: Lagomorph Nutrition & Emergency Pathology.
- **Learning Objectives**: Master hindgut fermentation mechanics, cecotrophy, continuous dental wear, and life-threatening Gastrointestinal (GI) Stasis.
- **Content Outline**:
  - The Dietary Golden Ratio:
    - **85%+ Unprocessed Long-Stem Grass Hay** (Timothy, Orchard, Meadow): Indigestible fiber driving gut motility and wearing continuously growing elodont teeth (2–3 mm/week).
    - **10% Fresh Leafy Greens** & **5% Plain Timothy Pellets**.
  - Cecotrophy: Specialized ingestion of nutrient-rich fermented cecal capsules ("night feces") supplying B-vitamins, volatile fatty acids, and microbial proteins.
  - Gastrointestinal (GI) Stasis Emergency Cascade: Pain/Stress $\to$ Hypomotility $\to$ Gas buildup $\to$ Microbial dysbiosis $\to$ Stomach/cecal impaction $\to$ Hypothermic endotoxic shock.
- **Visuals**: Detailed rabbit reaching to nibble timothy hay from a wooden rack with `85%+ FIBER` badge; 3-step GI stasis emergency cascade.

#### Slide 7: Safe Enclosure Architecture & Timber Habitat Design
- **Theme**: Habitat Engineering & Non-Toxic Wood Chemistry.
- **Learning Objectives**: Design modern free-roam rabbit living quarters and evaluate timber safety matrices for natural chewing.
- **Content Outline**:
  - The Inadequacy of Commercial Hutches: Caging causes spinal deformities, ulcerative pododermatitis (sore hocks), and depression. Minimum 12 sq ft exercise pen + daily free-roam access.
  - Dual-Exit Castles: Prey flight instincts require multiple exit points in every wooden hideout.
  - Wood Toxicity & Chewing Safety Matrix:
    - *100% Safe*: Apple, Pear, Hazelnut, Willow, Aspen, Birch, Kiln-Dried Pine (phenols heat-neutralized).
    - *Toxic Phenols*: Fresh Cedar, Green Pine (respiratory and hepatic destruction).
    - *Cyanogenic Glycosides*: Fresh twigs of Cherry, Peach, Plum (hydrocyanic acid release).
    - *Hardwood Toxins*: Oak, Black Walnut (tannins and juglone inducing colic).
- **Visuals**: Kiln-dried timber castle with crenellations, dual flight arches, and bundled applewood chew twigs; timber safety table.

#### Slide 8: Behavioral Enrichment: Foraging, Chewing & Scent Work
- **Theme**: Ethological Drive Fulfillment & Stereotypy Prevention.
- **Learning Objectives**: Implement species-tailored foraging systems to replace rapid bowl-feeding and extinguish stereotypic behaviors.
- **Content Outline**:
  - Ethological Deprivation: The psychological consequences of passive feeding: bar-biting in rabbits, psychogenic alopecia in cats, compulsive pacing in dogs.
  - Wild Foraging Comparison: Wild ancestors spend up to 70% of waking hours searching for food vs. $<15$ minutes in domestic bowl-fed animals.
  - Species-Specific Foraging Blueprints:
    - *Canines*: Olfactory scatter feeding, frozen stratified KONGs, destructible cardboard nested boxes.
    - *Felines*: Multiple elevated puzzle mice hidden throughout home.
    - *Lagomorphs*: Dig boxes (sterile soil/hay/dandelion), hay-stuffed tubes, foraging seagrass mats.
  - **Live Python Engine Telemetry**: Embedded contra-freeloading caloric breakdown, cognitive tiering, and apparatus prescriptions from `enrichment_calculator.py`.
- **Visuals**: Multi-layered fleece snuffle mat with treat pockets, drifting scent trails, and herbal dig tray; foraging blueprint cards; live Python calculation telemetry card.

#### Slide 9: Multi-Pet Household Management & Safe Coexistence
- **Theme**: Interspecies Dynamics & Predator-Prey Safety.
- **Learning Objectives**: Safely manage predator-prey dynamics between dogs, cats, and rabbits through desensitization and fortified sanctuary architecture.
- **Content Outline**:
  - The Sudden Flight Trigger: Instinctive predatory motor patterns firing reflexively on sudden rabbit hops, even in gentle family dogs.
  - Sanctuary Zone Architecture: Fortified, dog/cat-proof rooms ensuring prey animals never experience visual or olfactory entrapment.
  - 4-Stage Systematic Introduction Protocol:
    1. *Stage 1: Blind Scent Swapping*: Exchanging bedding and scent cloths with positive reward pairing.
    2. *Stage 2: Distanced Barrier Visual Interaction*: Double baby gates; rewarding instant disengagement.
    3. *Stage 3: Controlled Shared Airspace*: Leashed down-stays with rabbit inside fortified habitat.
    4. *Stage 4: Supervised Free-Range*: Only with bomb-proof, low-prey-drive animals.
- **Visuals**: Double-grid protective barrier with calm lying dog on one side and rabbit sanctuary zone on the other; 4-stage protocol funnel.

#### Slide 10: Lifetime Commitment: Preventative Health & Quality of Life
- **Theme**: Geriatric Stewardship & Ethical End-of-Life Transitions.
- **Learning Objectives**: Execute proactive preventative health frameworks, monitor Body Condition Scoring (BCS), and apply the HHHHHMM Quality of Life scale.
- **Content Outline**:
  - Proactive Wellness Protocol: Annual dental examinations, biannual senior blood chemistry/urinalysis, core vaccinations (including RHDV2 for lagomorphs), monthly BCS tracking (target 4.5/9).
  - The Silent Threat of Periodontal Disease: Chronic oral inflammation as a primary driver of renal, hepatic, and cardiovascular deterioration.
  - The **HHHHHMM Quality of Life Scale** (Dr. Alice Villalobos): Hurt, Hunger, Hydration, Hygiene, Happiness, Mobility, More Good Days.
  - The Ethical Covenant: Euthanasia as the ultimate selfless act of compassionate guardianship.
  - Final Academic Project Footer: Inbal Ehre & Noy Shalev, Bar-Ilan University, Dr. Yoram Segal.
- **Visuals**: Caring cupped hands cradling a covenant heart with multi-species paw prints and laurel sprigs; HHHHHMM scoring triad; project attribution card.

---

### 5. 3D WebGL Technical Implementation Specifications

#### 5.1 Scene Graph & Organic Particle Architecture
- **Engine**: Three.js (r128 via CDN).
- **Particle System**: Single `THREE.Points` object with `THREE.BufferGeometry` containing 850 point particles.
- **Attributes**:
  - `position`: `Float32Array(850 * 3)` coordinates procedurally distributed across 5 biological cluster centroids.
  - `color`: `Float32Array(850 * 3)` storing normalized RGB colors mapped to species and welfare themes:
    - Cluster 0: Warm Amber / Terracotta (`#d97736`)
    - Cluster 1: Soft Honey (`#e0a96d`)
    - Cluster 2: Muted Sage / Olive (`#87a987`)
    - Cluster 3: Warm Sand / Clay (`#c9ada7`)
    - Cluster 4: Creamy Off-White (`#fdfbf7`)
- **Material & Texture**: High-performance canvas-generated circular soft radial glow sprite rendered with `THREE.AdditiveBlending` and `depthWrite: false`.

#### 5.2 Connecting Ecosystem Graph Edges
- **Geometry**: `THREE.LineSegments` utilizing a dynamic buffer geometry connecting nearby particles within clusters (distance threshold $< 16\text{ units}$, maximum 2 connections per particle), with an intentional $1.2\%$ cross-cluster bridge probability simulating interspecies ecological connectivity.
- **Material**: `THREE.LineBasicMaterial` with vertex colors enabled and 14% additive opacity to maintain readability without obscuring slide foreground text.

#### 5.3 Mouse Parallax & Dynamic Orbit Lerp
- Cursor movement maps normalized window coordinates $(x, y) \in [-1, 1]$ to target rotation angles:
  $$\Delta \theta_y = \text{mouseX} \cdot 0.38, \quad \Delta \theta_x = \text{mouseY} \cdot 0.28$$
- Smooth damping is achieved via linear interpolation (lerp) per frame:
  $$\text{rotation}_t = \text{rotation}_{t-1} + (\text{target} - \text{rotation}_{t-1}) \cdot 0.025$$
- **Sinusoidal Breathing Undulation**: Continuous vertical floating perturbation (`Math.sin(elapsedTime * 0.5) * 1.5`) simulating natural organic life.
- **Slide-Reactive Camera Transitions**: Transitioning between slides updates the camera's spatial coordinate vector $(X, Y, Z)$, smoothly gliding and orbiting to spotlight different sectors of the organic constellation corresponding to the slide topic.

---

### 6. Verification and Acceptance Criteria

| Criteria ID | Category | Requirement Description | Verification Method | Status |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | **Deterministic Build** | Running `python generate_presentation.py` exits with code 0 and creates `presentation.html` in the root workspace. | Automated command execution. | **PASSED** |
| **AC-02** | **Slide Completeness** | Exactly 10 slides rendered with semantic IDs `slide-1` through `slide-10`, complete badges, titles, subtitles, and structured bodies. | DOM query and regex count. | **PASSED** |
| **AC-03** | **Subject Mastery** | Comprehensive coverage of Five Domains, Species Differences, Canine Puzzles, Senior Care, Feline Territory, Lagomorph Hay/GI Stasis, Safe Timber Architecture, Foraging, Multi-Pet Dynamics, and HHHHHMM Scale. | Manual and automated text inspection. | **PASSED** |
| **AC-04** | **3D WebGL Canvas** | Three.js point-cloud with 5 organic clusters, glowing circular sprites, delicate filament lines, and breathing animation (no tech grid). | JavaScript VM parsing and browser execution. | **PASSED** |
| **AC-05** | **Animated Vector Art** | Embedded inline SVG illustrations on all slides with keyframe animations (`float-gentle`, `pulse-subtle`, `scent-wave`, `breathe-glow`). | CSS & SVG DOM inspection. | **PASSED** |
| **AC-06** | **Deep-Linking** | URL parameter `?slide=N` and hash `#slide-N` jump immediately to the requested slide on load. | Unit test in headless browser. | **PASSED** |
| **AC-07** | **Automated Screenshots** | `capture_screenshots.py` captures 1080p screenshots (`screenshots/overview.png` and `screenshots/slide_detail.png`) via headless Edge without profile collisions. | Python script execution and file size verification. | **PASSED** |
| **AC-08** | **Engineering Logs** | Dedicated `prompts/` folder with `prompt_history.md` and `iteration_log.md` detailing the entire project evolution. | File inspection. | **PASSED** |
| **AC-09** | **Zero Pip Dependencies** | Presentation generator runs on standard library Python without requiring pip package installations. | Clean Python execution. | **PASSED** |
| **AC-10** | **Functional Tool Integration** | `enrichment_calculator.py` models metabolic RER/MER, contra-freeloading, and joint stress; outputs embedded live into Slide 4 and Slide 8. | CLI testing & HTML telemetry verification. | **PASSED** |
