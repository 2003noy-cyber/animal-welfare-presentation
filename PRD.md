# Product Requirements Document (PRD)

## Project: Companion Animal Welfare, Nutrition & Cognitive Enrichment (Canines, Felines & Lagomorphs) — Interactive Technical Masterclass

---

### 1. Executive Summary & Project Objectives

#### 1.1 Executive Summary
Human guardianship of companion animals has advanced dramatically over the past two decades, transitioning from basic disease management and confinement toward an evidence-based, compassionate behavioral and nutritional science. Millions of dogs (*Canis lupus familiaris*), cats (*Felis catus*), and rabbits (*Oryctolagus cuniculus*) live in domestic environments that frequently fail to satisfy their evolutionary ethology, resulting in chronic stress, destructive stereotypies, obesity, and premature mortality.

This project delivers a **10-slide, interactive, standalone technical presentation** titled *"Companion Animal Welfare, Nutrition & Cognitive Enrichment (Canines, Felines & Lagomorphs)"*. Designed for veterinary professionals, companion animal behaviorists, rescue directors, and devoted guardians, this masterclass provides an exhaustive, scientifically rigorous examination of species-appropriate biological care, cognitive stimulation, and modern welfare philosophy.

The entire masterclass is built and exported deterministically by a single Python script (`generate_presentation.py`), producing a zero-dependency, self-contained `presentation.html` document with an interactive 3D WebGL organic point-cloud background powered by Three.js.

#### 1.2 Core Objectives
- **Ethological & Clinical Depth**: Provide deep subject mastery spanning the **Five Domains Model** of animal welfare, comparative digestive physiology (facultative vs. obligate carnivores vs. hindgut fermenters), canine contra-freeloading and olfactory neuro-processing, feline 3D territory dynamics and predatory sequences, lagomorph cecotrophy and GI stasis emergency management, non-toxic timber habitat architecture, and multi-pet predator-prey dynamics.
- **Organic 3D Spatial Visualization**: Integrate an interactive 3D WebGL canvas that renders a multi-cluster organic point-cloud with interconnected dynamic edges, responding to cursor parallax and slide-specific camera orbit transitions.
- **Zero-Dependency Standalone Ergonomics**: Ensure the presentation runs completely offline in any modern web browser without requiring Node.js, Webpack, local web server daemons, or Python pip dependencies outside standard library modules.
- **Modern Glassmorphism UI**: Deliver a polished dark-mode aesthetic utilizing translucent frosted glass cards, fluid typography (`Inter`, `Space Grotesk`, `JetBrains Mono`), color-coded status badges, and responsive keyboard/touch navigation.

---

### 2. Technology Stack & Architectural Specifications

| Component | Technology | Rationale & Specification |
| :--- | :--- | :--- |
| **Generator Script** | Python 3.10+ Standard Library (`pathlib`, `sys`) | Zero external pip dependencies; deterministic file generation; cross-platform execution. |
| **Presentation Engine** | Vanilla ES6+ JavaScript & HTML5 DOM | High performance, instant hydration, zero framework overhead (no React/Vue runtime). |
| **3D WebGL Graphics** | Three.js (r128 via CDN) | Hardware-accelerated point-cloud generation, particle glow shader simulation, dynamic graph lines, and camera lerp animations. |
| **Typography & Styling** | CSS3 Modern Specifications | Glassmorphism (`backdrop-filter: blur(28px)`), CSS Grid/Flexbox layouts, CSS custom variables, and Google Fonts (`Inter`, `Space Grotesk`, `JetBrains Mono`). |

---

### 3. Detailed Slide-by-Slide Syllabus (10 Slides)

#### Slide 1: Holistic Companion Animal Care & Welfare
- **Theme**: Welfare Science & Paradigm Evolution.
- **Learning Objectives**: Understand the shift from traditional "Five Freedoms" to the contemporary **Five Domains Model** (Mellor et al.); evaluate the role of positive affective states and agency in long-term health.
- **Content Outline**:
  - The Five Domains Model: Nutrition, Physical Environment, Health, Behavioral Interactions, and Positive Mental State.
  - Cognitive Agency & Stress Reduction: Demonstrating that perceived control over environment reduces chronic cortisol levels by $>80\%$.
  - The Triad of Species-Appropriate Guardianship: Biological integrity $\to$ Environmental sanctuary $\to$ Cognitive agency $\to$ Interspecies trust $\to$ Flourishing longevity.
- **Visuals**: 5-step holistic care pipeline; high-contrast welfare metric telemetry badges.

#### Slide 2: Species-Specific Needs: Dogs vs. Cats vs. Rabbits
- **Theme**: Comparative Biology & Evolutionary Ecology.
- **Learning Objectives**: Master divergent digestive, nutritional, social, and sensory adaptations across canines, felines, and lagomorphs.
- **Content Outline**:
  - **Canines (*Canis lupus familiaris*)**: Facultative carnivores / opportunistic omnivores; flexible macronutrient assimilation; cooperative group sociality; mutual gaze oxytocin feedback loop.
  - **Felines (*Felis catus*)**: Strict obligate carnivores requiring mandatory dietary taurine, arachidonic acid, and preformed vitamin A; solitary territorial hunters; vertical space orientation.
  - **Lagomorphs (*Oryctolagus cuniculus*)**: Crepuscular colonial prey animals; hindgut fermenters requiring continuous indigestible long-stem roughage; non-vocal communication and acute illness masking.
- **Visuals**: Comprehensive comparative taxonomy table across Diet, Nutrients, Social Model, and Sensory Priorities.

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
- **Visuals**: 3-stage puzzle progression funnel; golden rules of frustration mitigation.

#### Slide 4: Senior Dog Care: Mobility, Joint Support & Mental Stimulation
- **Theme**: Geriatric Medicine & Neuro-Preservation.
- **Learning Objectives**: Formulate multimodal osteoarthritis management protocols and identify early Cognitive Dysfunction Syndrome (CDS).
- **Content Outline**:
  - Multimodal Osteoarthritis (OA) Management: Anti-NGF monoclonal antibodies (bedinvetmab / Librela), marine omega-3 fatty acids (EPA/DHA $>100\text{ mg/kg}$), joint chondroprotectants (UC-II), non-slip environmental floor modifications.
  - Cognitive Dysfunction Syndrome (CDS / "Canine Alzheimer's"): Diagnostic evaluation via the **DISHA** framework:
    - **D**: Disorientation in familiar spaces.
    - **I**: Interactions altered with humans and pets.
    - **S**: Sleep-wake cycle disturbances (nocturnal pacing).
    - **H/A**: House soiling loss and purposeless activity.
  - Low-impact geriatric cognitive exercise: "Sniffaris" (slow scent walks) and stationary lick-mats.
- **Visuals**: DISHA diagnostic grid cards; multimodal joint therapy protocol.

#### Slide 5: Feline Environmental Enrichment & Territory Dynamics
- **Theme**: Feline Ethology & Spatial Engineering.
- **Learning Objectives**: Architect 3D vertical territory, satisfy predatory motor patterns, and prevent feline inter-cat resource friction.
- **Content Outline**:
  - 3D Vertical Territory: Cats experience living spaces in cubic volume rather than square footage. Cat superhighways, floating catwalks, and elevated vantage points mitigate inter-cat territorial conflicts.
  - The Full Predatory Motor Pattern:
    $$\text{Stare} \to \text{Stalk} \to \text{Chase} \to \text{Pounce} \to \text{Kill-Bite} \to \text{Eat/Groom}$$
  - Laser Pointer Syndrome: Neurochemical frustration caused by non-catchable light beams; mandatory transition to physical feathered/plush prey.
  - The $N+1$ Resource Rule: Dispersing litter boxes, water fountains, and scratching posts across separate rooms.
- **Visuals**: 6-step predatory motor sequence flowchart; Laser pointer pathology alert box.

#### Slide 6: Lagomorph Welfare: Delicate Digestive Systems & Hay Diet
- **Theme**: Lagomorph Nutrition & Emergency Pathology.
- **Learning Objectives**: Master hindgut fermentation mechanics, cecotrophy, continuous dental wear, and life-threatening Gastrointestinal (GI) Stasis.
- **Content Outline**:
  - The Dietary Golden Ratio:
    - **85%+ Unprocessed Long-Stem Grass Hay** (Timothy, Orchard, Meadow): Indigestible fiber driving gut motility and wearing continuously growing elodont teeth (2–3 mm/week).
    - **10% Fresh Leafy Greens** & **5% Plain Timothy Pellets**.
  - Cecotrophy: Specialized ingestion of nutrient-rich fermented cecal capsules ("night feces") supplying B-vitamins, volatile fatty acids, and microbial proteins.
  - Gastrointestinal (GI) Stasis Emergency Cascade: Pain/Stress $\to$ Hypomotility $\to$ Gas buildup $\to$ Microbial dysbiosis $\to$ Stomach/cecal impaction $\to$ Hypothermic endotoxic shock.
- **Visuals**: 3-step GI stasis emergency cascade; 12-hour intervention threshold callout.

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
- **Visuals**: Comprehensive Timber Safety Table; pododermatitis prevention guide.

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
- **Visuals**: Cross-species foraging blueprint cards; ethological time-budget metrics.

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
- **Visuals**: 3-stage protocol funnel; predatory flight trigger warning card.

#### Slide 10: Lifetime Commitment: Preventative Health & Quality of Life
- **Theme**: Geriatric Stewardship & Ethical End-of-Life Transitions.
- **Learning Objectives**: Execute proactive preventative health frameworks, monitor Body Condition Scoring (BCS), and apply the HHHHHMM Quality of Life scale.
- **Content Outline**:
  - Proactive Wellness Protocol: Annual dental examinations, biannual senior blood chemistry/urinalysis, core vaccinations (including RHDV2 for lagomorphs), monthly BCS tracking (target 4.5/9).
  - The Silent Threat of Periodontal Disease: Chronic oral inflammation as a primary driver of renal, hepatic, and cardiovascular deterioration.
  - The **HHHHHMM Quality of Life Scale** (Dr. Alice Villalobos):
    - **H**urt (effective pain management)
    - **H**unger (voluntary nutritional intake)
    - **H**ydration (fluid balance maintenance)
    - **H**ygiene (ability to stay clean and self-groom)
    - **H**appiness (expression of joy, curiosity, tail wags, purrs, binkies)
    - **M**obility (ability to stand, walk, explore without distress)
    - **M**ore Good Days than Bad Days
  - The Ethical Covenant: Euthanasia as the ultimate selfless act of compassionate guardianship.
- **Visuals**: Proactive healthcare timeline; HHHHHMM triad scoring cards.

---

### 4. 3D WebGL Technical Implementation Specifications

#### 4.1 Scene Graph & Organic Particle Architecture
- **Engine**: Three.js (r128 via CDN).
- **Particle System**: Single `THREE.Points` object with `THREE.BufferGeometry` containing 900 point particles.
- **Attributes**:
  - `position`: `Float32Array(900 * 3)` coordinates procedurally distributed across 5 biological cluster centroids.
  - `color`: `Float32Array(900 * 3)` storing normalized RGB colors mapped to species and welfare themes:
    - Cluster 0: Canine Vitality (Warm Amber / Gold `#f59e0b`)
    - Cluster 1: Feline Grace & Agility (Emerald Green `#10b981`)
    - Cluster 2: Lagomorph Nature & Earth (Sage / Olive `#84cc16`)
    - Cluster 3: Cognitive Spark & Puzzles (Cyan / Turquoise `#06b6d4`)
    - Cluster 4: Welfare & Compassion (Rose / Coral `#f43f5e`)
  - `size`: `Float32Array(900)` generating natural point-size variance ($1.4 - 5.0\text{px}$).
- **Material & Texture**: High-performance canvas-generated circular soft radial glow sprite rendered with `THREE.AdditiveBlending` and `depthWrite: false`.

#### 4.2 Connecting Ecosystem Graph Edges
- **Geometry**: `THREE.LineSegments` utilizing a dynamic buffer geometry connecting nearby particles within clusters (distance threshold $< 17\text{ units}$, maximum 3 connections per particle), with an intentional $1.8\%$ cross-cluster bridge probability simulating interspecies ecological connectivity.
- **Material**: `THREE.LineBasicMaterial` with vertex colors enabled and 24% additive opacity to maintain readability without obscuring slide foreground text.

#### 4.3 Mouse Parallax & Dynamic Orbit Lerp
- Cursor movement maps normalized window coordinates $(x, y) \in [-1, 1]$ to target rotation angles:
  $$\Delta \theta_y = \text{mouseX} \cdot 0.45, \quad \Delta \theta_x = \text{mouseY} \cdot 0.35$$
- Smooth damping is achieved via linear interpolation (lerp) per frame:
  $$\text{rotation}_t = \text{rotation}_{t-1} + (\text{target} - \text{rotation}_{t-1}) \cdot 0.03$$
- **Slide-Reactive Camera Transitions**: Transitioning between slides updates the camera's spatial coordinate vector $(X, Y, Z)$, smoothly gliding and orbiting to spotlight different sectors of the organic constellation corresponding to the slide topic.

---

### 5. Verification and Acceptance Criteria

| Criteria ID | Category | Requirement Description | Verification Method | Status |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | **Deterministic Build** | Running `python generate_presentation.py` exits with code 0 and creates `presentation.html` in the root workspace. | Automated command execution. | **PASSED** |
| **AC-02** | **Slide Completeness** | Exactly 10 slides rendered with semantic IDs `slide-1` through `slide-10`, complete badges, titles, subtitles, and structured bodies. | DOM query and regex count. | **PASSED** |
| **AC-03** | **Subject Mastery** | Comprehensive coverage of Five Domains, Species Differences, Canine Puzzles, Senior Care, Feline Territory, Lagomorph Hay/GI Stasis, Safe Timber Architecture, Foraging, Multi-Pet Dynamics, and HHHHHMM Scale. | Manual and automated text inspection. | **PASSED** |
| **AC-04** | **3D WebGL Canvas** | Three.js point-cloud with 5 organic clusters, glowing circular sprites, connecting lines, and mouse parallax. | JavaScript VM parsing and browser execution. | **PASSED** |
| **AC-05** | **Navigation & Controls** | Arrow keys, spacebar, pageup/pagedown, navigation buttons, and bottom dots allow bidirectional traversal with active state updates. | DOM event inspection. | **PASSED** |
| **AC-06** | **Zero External Build Tools** | Presentation runs as a standalone HTML file without Node/npm build steps or Python external package dependencies. | Code audit. | **PASSED** |
| **AC-07** | **Responsive Design** | Graceful degradation across desktop, tablet, and mobile viewports with flexible CSS grids and scrolling cards. | CSS media query validation. | **PASSED** |
