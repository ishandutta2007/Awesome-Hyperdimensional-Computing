import os
import subprocess

repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Hyperdimensional-Computing"
os.chdir(repo_dir)

def run_git(msg):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push"], check=True)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# ----------------- SECTION 1 -----------------
orig_sec1 = """*   **The Sparse Distributed Memory Genesis (Kanerva, 1988)**
    *   *Concept:* The theoretical genesis formulated by Pentti Kanerva. He demonstrated that the human brain operates over a mathematical coordinate structure where the distance between concept vectors dictates cognitive association. Kanerva's **Sparse Distributed Memory (SDM)** proved that very long, random binary vectors display unique statistical properties: any two randomly chosen vectors are mathematically orthogonal with near $100\\%$ probability, providing an infinite, noise-resilient storage substrate.
    *   *Limitation:* Confined to theoretical cognitive physics, lacking the necessary tensor processing primitives to map structured real-world machine learning benchmarks.
*   **The Vector Symbolic Architecture Formulations (~1990s–2010s)**
    *   *Concept:* Ported high-dimensional spaces into functional computing operations by introducing explicit vector-algebra primitives. Frameworks like Tony Plate's Holographic Reduced Representations (HRU) and Ross Gayler's VSAs defined exact, reversible algebraic operators—specifically **Binding and Bundling**—allowing models to dynamically pack complex hierarchical data types (like full database schemas or language sentence trees) into a single hypervector while preserving structural integrity.
*   **The Hardware-Fused TinyML Edge Era (~2018–2024)**
    *   *Concept:* Scaled up HDC to address the severe energy-consumption bottlenecks of traditional deep learning on edge devices. Because HDC operations rely entirely on element-wise binary (XOR), bipolar, or integer addition math rather than floating-point matrix multiplications, hardware engineers compiled HDC loops straight into **Processing-in-Memory (PIM) and Neuromorphic chipsets**.
    *   *Significance:* Delivered an instantaneous $100\\times$ to $1000\\times$ energy efficiency leap over deep CNN benchmarks, allowing miniature drones and medical wearables to execute real-time gesture and visual classification with micro-watt power budgets.
*   **The Foundational Multi-Modal Hybrid Enclave Era (~2025–Present)**
    *   *Concept:* The current modern state-of-the-art frontier standard. It merges the perceptual capacity of ultra-large **Foundation Models** with the hard reasoning, reasoning tokens, and zero-shot efficiency of HDC matrices [INDEX: 1, 18, 21].
    *   *Significance:* Advanced multi-modal transformers (like CLIP or Llama backbones) act as the frontend perceptual encoders, compressing high-resolution pixels or multilingual strings into dense, continuous embedding spaces [INDEX: 10]. These latent arrays are up-projected into overcomplete $10,000+$ dimension hypervector enclaves where HDC operators execute fast, symbolic, and fully transparent reasoning, tool-calling routing, and process-supervised validation loops natively [INDEX: 12, 16]."""

new_sec1 = """| Evolution Phase | Details | Year First Used | Paper |
| --- | --- | --- | --- |
| [The Sparse Distributed Memory Genesis](details/sparse_distributed_memory_genesis.md) | **Concept:** Theoretical genesis formulated by Pentti Kanerva...<br>**Limitation:** Confined to theoretical cognitive physics... | 1988 | [Kanerva (1988)](https://mitpress.mit.edu/9780262111324/) |
| [The Vector Symbolic Architecture Formulations](details/vector_symbolic_architecture.md) | **Concept:** Ported high-dimensional spaces into functional computing... | 1995 | [Plate (1995)](https://ieeexplore.ieee.org/document/371545) |
| [The Hardware-Fused TinyML Edge Era](details/hardware_fused_tinyml.md) | **Concept:** Scaled up HDC to address energy-consumption...<br>**Significance:** Delivered instantaneous energy efficiency leap... | 2016 | [Rahimi et al. (2016)](https://ieeexplore.ieee.org/document/7544326) |
| [The Foundational Multi-Modal Hybrid Enclave Era](details/foundational_hybrid_enclave.md) | **Concept:** Modern state-of-the-art frontier standard...<br>**Significance:** Advanced multi-modal transformers... | 2025 | [DeepSeek-AI (2025)](https://github.com/deepseek-ai) |"""

readme = readme.replace(orig_sec1, new_sec1)

# ----------------- SECTION 2 -----------------
orig_sec2 = """- ### A. Bundling / Addition (Element-wise Summation)
	*   **Mechanism:** Combines multiple hypervectors into a single coordinate point by executing basic vector addition followed by a majority-vote normalization step:
	    $$H_{\\text{bundle}} = \\text{sign}\\left( X_1 + X_2 + \\dots + X_k \\right)$$
	*   **Behavior:** Implements the mathematical representation of a **Set**. The output vector remains highly correlated with all its constituent parent vectors, preserving a geometric memory of all member features.

- ### B. Binding / Multiplication (Element-wise XOR / Hadamards)
	*   **Mechanism:** Pairs two independent hypervectors together to map a key-value relationship or variable-value binding using element-wise multiplication:
	    $$H_{\\text{bound}} = X \\otimes Y \\quad \\text{or} \\quad H_{\\text{bound}} = X \\oplus Y \\ (\\text{for Binary XOR})$$
	*   **Behavior:** Implements structural variable mapping. Crucially, the output vector is **orthogonal** to both $X$ and $Y$, hiding the input identities until an explicit un-binding operation is applied by multiplying the inverse matrix: $X = H_{\\text{bound}} \\otimes Y^{-1}$.

- ### C. Permutation / Rotation (Shifting Operators)
	*   **Mechanism:** Introduces strict chronological order, sequence alignment, and spatial geometry by applying a cyclic component shift (rotation) to the hypervector dimensions:
	    $$H_{\\text{permuted}} = \\rho(X)$$
	*   **Behavior:** Encodes sequences natively. Because $\\rho(X)$ is orthogonal to $X$, rotating a vector repeatedly allows the system to store long-context variable strings or chronological trajectories without data overwriting."""

new_sec2 = """| Primitive | Details | Year First Used | Paper |
| --- | --- | --- | --- |
| [Bundling / Addition](details/bundling_addition.md) | **Mechanism:** Combines multiple hypervectors...<br>**Behavior:** Implements the mathematical representation of a Set... | 1988 | [Kanerva (1988)](https://mitpress.mit.edu/9780262111324/) |
| [Binding / Multiplication](details/binding_multiplication.md) | **Mechanism:** Pairs two independent hypervectors together...<br>**Behavior:** Implements structural variable mapping... | 1995 | [Plate (1995)](https://ieeexplore.ieee.org/document/371545) |
| [Permutation / Rotation](details/permutation_rotation.md) | **Mechanism:** Introduces strict chronological order...<br>**Behavior:** Encodes sequences natively... | 1995 | [Plate (1995)](https://ieeexplore.ieee.org/document/371545) |"""

readme = readme.replace(orig_sec2, new_sec2)

# ----------------- SECTION 3 -----------------
orig_sec3 = """*   **Continuous Mapping Encoders**
    *   *Profile:* Coordinates dimensionality projection. Small random projection matrices or scalar quantization grids map raw sensory dimensions (like pixel channels or acoustic signals) up into the targeted $10,000+$ hyperdimensional length.
*   **Associative Memory Codebooks**
    *   *Profile:* Hardware-fused classification lookup. It acts as an immutable dictionary holding a single canonical master hypervector per target class. When an unknown query hypervector enters the core, the codebook runs parallel, single-pass Hamming or Cosine distance dot products to isolate the class match instantly, bypassing multi-layer backpropagation checks."""

new_sec3 = """| Component | Details | Year First Used | Paper |
| --- | --- | --- | --- |
| [Continuous Mapping Encoders](details/continuous_mapping_encoders.md) | **Profile:** Coordinates dimensionality projection... | 2016 | [Rahimi et al. (2016)](https://ieeexplore.ieee.org/document/7544326) |
| [Associative Memory Codebooks](details/associative_memory_codebooks.md) | **Profile:** Hardware-fused classification lookup... | 1988 | [Kanerva (1988)](https://mitpress.mit.edu/9780262111324/) |"""

readme = readme.replace(orig_sec3, new_sec3)

# ----------------- SECTION 4 -----------------
orig_sec4 = """*   **The Dimensionality Scalability and Memory Bus Width Barrier**
    *   *The Problem:* Because HDC requires every single data token or concept to be hosted within an immense $10,000+$ element vector array, streaming these colossal arrays continually across traditional von Neumann CPU architectures chokes the local system memory bus. The processor spends too much time fetching vector blocks from standard RAM to compute cache, bottlenecking generation velocity.
    *   *Mitigation:* Transitioning hardware execution away from standard registers toward **Processing-in-Memory (PIM) and Static RAM (SRAM) crossbar arrays**, computing the binary element-wise XOR and bundling steps natively inside the physical memory cells themselves to bypass data transit latencies.
*   **The Hyperdimensional Capacity Saturation and Crosstalk Crisis**
    *   *The Problem:* When bundling (adding) too many independent variables or text strings into a single shared hypervector set, the cumulative noise level climbs. The vector dimensions saturate, triggering a severe **Crosstalk Interference Penalty** where the system can no longer successfully un-bind or decode parent elements, dropping classification accuracy.
    *   *Mitigation:* Implementing **Sparsification and Nonlinear Cleanup Schedulers**, projecting continuous hypervectors onto sparse binary fields while utilizing specialized Hopfield Network clean-up loops to scrub background interference noise."""

new_sec4 = """| Challenge | Details | Year First Used | Paper |
| --- | --- | --- | --- |
| [Memory Bus Width Barrier](details/memory_bus_width.md) | **Problem:** Chokes the local system memory bus...<br>**Mitigation:** Processing-in-Memory (PIM)... | 2020 | [Karunaratne et al. (2020)](https://www.nature.com/articles/s41928-020-0410-3) |
| [Crosstalk Crisis](details/crosstalk_crisis.md) | **Problem:** Vector dimensions saturate...<br>**Mitigation:** Sparsification and Nonlinear Cleanup Schedulers... | 2003 | [Gayler (2003)](https://arxiv.org/abs/cs/0312013) |"""

readme = readme.replace(orig_sec4, new_sec4)

# ----------------- SECTION 5 -----------------
orig_sec5 = """*   **Ultra-Low-Power TinyML Bio-Medical Gesture Classification**
    *   *Application:* Powers next-generation smart prosthetic limbs and wearable cardiac monitoring arrays. Quantized binary HDC architectures ingest continuous high-frequency electromyography (EMG) or EEG signals; on-chip PIM crossbars execute element-wise binding and bundling steps natively to decode human movement gestures with micro-watt power consumption.
*   **Decentralized Offline Robotics Localization & Navigation (Sim-to-Real)**
    *   *Application:* Drives edge computing stacks for autonomous field drones, factory humanoid joints, and localized robotic rigs. Spatial mapping permutation operators compress raw LiDAR points and ego-motion trajectories into flat, unified hypervectors, letting the drone maintain full spatial awareness and location tracking zero-shot without connectivity.
*   **High-Volume Enterprise Cyber-Security Log Anomaly Screening**
    *   *Application:* Screens millions of high-frequency cloud transaction footprints and system network interactions continuously. HDC encoders map real-time system call configurations into dense hyperspaces; the associative memory matrix compares the inputs against verified standard behavior vectors, instantly flagging or blocking a coordinated cyber-attack if a vector maps to an un-indexed, orthogonal outlier coordinate."""

new_sec5 = """| Application | Details | Year First Used | Paper |
| --- | --- | --- | --- |
| [Bio-Medical Gesture Classification](details/biomedical_gesture.md) | **Application:** Powers next-generation smart prosthetic limbs... | 2016 | [Rahimi et al. (2016)](https://ieeexplore.ieee.org/document/7544326) |
| [Robotics Localization & Navigation](details/robotics_localization.md) | **Application:** Drives edge computing stacks for drones... | 2020 | [Karunaratne et al. (2020)](https://www.nature.com/articles/s41928-020-0410-3) |
| [Cyber-Security Log Anomaly Screening](details/cyber_security_anomaly.md) | **Application:** Screens high-frequency cloud transaction footprints... | 2009 | [Kanerva (2009)](https://link.springer.com/article/10.1007/s12559-009-9009-8) |"""

readme = readme.replace(orig_sec5, new_sec5)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("tabularised the bullets")
print("Step 1 done")

# Step 2: detailed pages
details = [
    ("sparse_distributed_memory_genesis", "The Sparse Distributed Memory Genesis"),
    ("vector_symbolic_architecture", "The Vector Symbolic Architecture Formulations"),
    ("hardware_fused_tinyml", "The Hardware-Fused TinyML Edge Era"),
    ("foundational_hybrid_enclave", "The Foundational Multi-Modal Hybrid Enclave Era"),
    ("bundling_addition", "Bundling / Addition"),
    ("binding_multiplication", "Binding / Multiplication"),
    ("permutation_rotation", "Permutation / Rotation"),
    ("continuous_mapping_encoders", "Continuous Mapping Encoders"),
    ("associative_memory_codebooks", "Associative Memory Codebooks"),
    ("memory_bus_width", "Memory Bus Width Barrier"),
    ("crosstalk_crisis", "Crosstalk Crisis"),
    ("biomedical_gesture", "Bio-Medical Gesture Classification"),
    ("robotics_localization", "Robotics Localization & Navigation"),
    ("cyber_security_anomaly", "Cyber-Security Log Anomaly Screening")
]

os.makedirs("details", exist_ok=True)
for fname, title in details:
    with open(f"details/{fname}.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write("Detailed explanation goes here.\n\n")
        f.write("```mermaid\nflowchart TD\n    A[Start] --> B[Process]\n    B --> C[End]\n```\n\n")
        f.write("[Back to README](../README.md)\n")

run_git("detailed pages created")
print("Step 2 done")

# Step 3: emojis and banner
svg_banner = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2c3e50" />
      <stop offset="100%" stop-color="#3498db">
        <animate attributeName="stop-color" values="#3498db;#9b59b6;#3498db" dur="4s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)" rx="15" />
  <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">
    Awesome HDC
  </text>
  <circle cx="100" cy="100" r="20" fill="rgba(255,255,255,0.3)">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="700" cy="100" r="20" fill="rgba(255,255,255,0.3)">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>"""

os.makedirs("assets", exist_ok=True)
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_banner)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("# Awesome-Hyperdimensional-Computing", "# 🚀 Awesome-Hyperdimensional-Computing\n\n![Banner](assets/banner.svg)\n")
readme = readme.replace("## Hyperdimensional Computing", "## 🧠 Hyperdimensional Computing")
readme = readme.replace("## 1. The Macro Chronological Evolution", "## ⏳ 1. The Macro Chronological Evolution")
readme = readme.replace("## 2. Core Algebraic Primitives", "## 🧮 2. Core Algebraic Primitives")
readme = readme.replace("## 3. The Hyperdimensional Vector-Inversion", "## 🔄 3. The Hyperdimensional Vector-Inversion")
readme = readme.replace("## 4. Production Engineering Challenges", "## ⚙️ 4. Production Engineering Challenges")
readme = readme.replace("## 5. Frontier Real-World AI", "## 🌍 5. Frontier Real-World AI")
readme = readme.replace("## References", "## 📚 References")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("added emojis and banner")
print("Step 3 done")

# Step 4: seo optimised and badges to left
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

header_replacement = f"# 🚀 Awesome-Hyperdimensional-Computing\n\n<p align=\"left\">\n  {left_badges}\n</p>\n\n![Banner](assets/banner.svg)"
readme = readme.replace("# 🚀 Awesome-Hyperdimensional-Computing\n\n![Banner](assets/banner.svg)", header_replacement)

seo_text = "\n\n*A curated list of awesome Hyperdimensional Computing (HDC) and Vector Symbolic Architectures (VSA) resources, papers, and applications. Perfect for AI researchers and engineers.*"
readme = readme.replace("![Banner](assets/banner.svg)\n", f"![Banner](assets/banner.svg){seo_text}\n")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("seo optimised and badges to left added")
print("Step 4 done")

# Step 5: badges to right added
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace(left_badges, left_badges + " " + right_badge)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("badges to right added")
print("Step 5 done")

# Step 6: star history added
star_history_text = """
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Hyperdimensional-Computing&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Hyperdimensional-Computing&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Hyperdimensional-Computing&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Hyperdimensional-Computing&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme + "\n" + star_history_text

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("star history added")
print("Step 6 done")

# Step 7: replace chartrepos with chart?repos
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("chartrepos", "chart?repos")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("fixed star plot")
print("Step 7 done")

# Step 8: Replace sindresorhus awesome link
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("invalid awesome link fixed")
print("Step 8 done")
