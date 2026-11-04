"""
Automated Screenshot Capture Utility for Companion Animal Welfare Presentation.
Authors: Inbal Ehre (ענבל אהרה) & Noy Shalev (נוי שלו)
Course:  Generative AI, LLMs & Agents | Dr. Yoram Segal | Bar-Ilan University

Captures high-resolution 1920x1080 viewport screenshots of presentation slides
using headless Chromium (Microsoft Edge) with unique temporary profiles.
"""

import subprocess
import tempfile
import time
from pathlib import Path


def capture_slide_screenshot(slide_number: int, output_image_path: Path):
    """Launches headless Edge to capture a crisp 1080p slide screenshot."""
    edge_executable = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    if not edge_executable.exists():
        edge_executable = Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe")
    
    if not edge_executable.exists():
        raise FileNotFoundError(f"Microsoft Edge executable not found at {edge_executable}")

    html_file = Path("presentation.html").resolve()
    target_url = f"file:///{html_file.as_posix()}?slide={slide_number}"
    output_image_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=f"edge_shot_{slide_number}_") as temp_profile:
        args = [
            str(edge_executable),
            "--headless=new",
            "--disable-gpu",
            f"--user-data-dir={temp_profile}",
            f"--screenshot={output_image_path.resolve()}",
            "--window-size=1920,1080",
            target_url
        ]

        print(f"[*] Capturing Slide {slide_number} -> {output_image_path.name}...")
        result = subprocess.run(args, capture_output=True, text=True)
        time.sleep(0.5)

    if output_image_path.exists():
        print(f"[+] Successfully captured {output_image_path.name} ({output_image_path.stat().st_size:,} bytes)")
    else:
        print(f"[!] Warning: Screenshot failed for slide {slide_number}. Stderr: {result.stderr}")


def main():
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    overview_img = screenshots_dir / "overview.png"
    slide_detail_img = screenshots_dir / "slide_detail.png"

    # Slide 1: Overview (Holistic Companion Care & Welfare Triad + Academic Authors Banner)
    capture_slide_screenshot(1, overview_img)
    
    # Slide 4: Detail (Senior Dog Care, Joint Support & Live Python Biometrics Engine)
    capture_slide_screenshot(4, slide_detail_img)


if __name__ == "__main__":
    main()
