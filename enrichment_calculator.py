#!/usr/bin/env python3
"""
===============================================================================
Companion Animal Enrichment & Metabolic Calculator
===============================================================================
Authors: Inbal Ohana (ענבל אהרה) & Noy Shalev (נוי שלו)
Course:  Generative AI, LLMs & Agents | Dr. Yoram Segal | Bar-Ilan University
Topic:   Companion Animal Welfare, Nutrition & Cognitive Enrichment
===============================================================================

A standalone veterinary science & behavioral analytics engine that calculates:
1. Resting Energy Requirement (RER) via Kleiber's Law: RER = 70 * (mass_kg)^0.75
2. Maintenance Energy Requirement (MER) tailored for Canine, Feline, and Lagomorph species
3. Contra-Freeloading & Cognitive Foraging Caloric Budgets (20-35% daily MER)
4. Multi-Tier Cognitive Puzzle Scheduling (Level 1 beginner to Level 3 sequential problem-solving)
5. Senior Mobility & Joint Load Scoring with low-impact "Sniffari" exercise prescriptions
"""

import sys
import math
import json
import argparse
from typing import Dict, Any, List

# Ensure UTF-8 output even in Windows cmd/PowerShell with OEM codepages
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class CompanionEnrichmentCalculator:
    """Veterinary metabolic and cognitive enrichment modeling engine."""

    SPECIES_CANINE = "canine"
    SPECIES_FELINE = "feline"
    SPECIES_LAGOMORPH = "lagomorph"

    # Multipliers relative to RER based on WSAVA and NRC nutritional guidelines
    MER_FACTORS = {
        SPECIES_CANINE: {
            "puppy_growth": 2.5,
            "adult_intact": 1.8,
            "adult_neutered": 1.6,
            "senior_active": 1.4,
            "senior_geriatric": 1.2,
            "weight_loss_prone": 1.1,
        },
        SPECIES_FELINE: {
            "kitten_growth": 2.2,
            "adult_intact": 1.4,
            "adult_neutered": 1.2,
            "senior_geriatric": 1.1,
            "weight_loss_prone": 0.9,
        },
        SPECIES_LAGOMORPH: {
            "juvenile_growth": 2.0,
            "adult_maintenance": 1.5,
            "senior_maintenance": 1.25,
            "high_fiber_dietary_baseline": 1.35,
        },
    }

    def __init__(self):
        pass

    @staticmethod
    def calculate_rer(weight_kg: float) -> float:
        """Calculate Resting Energy Requirement (kcal/day) using allometric scaling."""
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0 kg")
        return round(70.0 * math.pow(weight_kg, 0.75), 1)

    def calculate_mer(
        self,
        weight_kg: float,
        species: str = SPECIES_CANINE,
        life_stage: str = "senior_geriatric",
    ) -> Dict[str, Any]:
        """Calculate Maintenance Energy Requirement and breakdown."""
        species = species.lower()
        if species not in self.MER_FACTORS:
            species = self.SPECIES_CANINE

        factors = self.MER_FACTORS[species]
        if life_stage not in factors:
            life_stage = list(factors.keys())[0]

        multiplier = factors[life_stage]
        rer = self.calculate_rer(weight_kg)
        mer = round(rer * multiplier, 1)

        return {
            "species": species,
            "weight_kg": weight_kg,
            "life_stage": life_stage,
            "rer_kcal": rer,
            "mer_multiplier": multiplier,
            "mer_kcal": mer,
        }

    def calculate_cognitive_foraging(
        self,
        weight_kg: float,
        species: str = SPECIES_CANINE,
        life_stage: str = "adult_neutered",
        cognitive_tier: int = 2,
    ) -> Dict[str, Any]:
        """
        Calculate daily contra-freeloading foraging budget and puzzle schedule.
        Contra-freeloading indicates that animals prefer working for food over identical free food.
        """
        mer_data = self.calculate_mer(weight_kg, species, life_stage)
        mer_kcal = mer_data["mer_kcal"]

        # Foraging budget allocation (25% to 35% of daily calories)
        budget_pct = 0.30 if species == self.SPECIES_CANINE else (0.25 if species == self.SPECIES_FELINE else 0.35)
        foraging_kcal = round(mer_kcal * budget_pct, 1)
        base_meal_kcal = round(mer_kcal - foraging_kcal, 1)

        puzzles = self.get_puzzle_recommendations(species, cognitive_tier)

        return {
            "mer_data": mer_data,
            "foraging_budget_pct": round(budget_pct * 100, 1),
            "foraging_kcal": foraging_kcal,
            "base_meal_kcal": base_meal_kcal,
            "cognitive_tier": cognitive_tier,
            "daily_sessions": 2 if cognitive_tier <= 2 else 3,
            "recommended_duration_minutes": 15 if cognitive_tier == 1 else (25 if cognitive_tier == 2 else 35),
            "puzzles": puzzles,
        }

    def get_puzzle_recommendations(self, species: str, tier: int) -> List[Dict[str, str]]:
        """Return progressive puzzle recommendations based on tier and species."""
        tier = max(1, min(3, tier))
        catalog = {
            self.SPECIES_CANINE: {
                1: [
                    {"name": "Dense Fleece Snuffle Mat", "mechanism": "Olfactory extraction & micro-rooting", "reward_rate": "High (continuous reinforcement)"},
                    {"name": "Lick Mat with Bone Broth/Pumpkin", "mechanism": "Tongue stimulation & endorphin release", "reward_rate": "Continuous slow-feed"},
                ],
                2: [
                    {"name": "Multi-Chamber Sliding Tile Board", "mechanism": "Nose nudge & paw displacement", "reward_rate": "Intermittent progressive"},
                    {"name": "Rolling Wobbler Treat Dispenser", "mechanism": "Kinetic displacement & balance tracking", "reward_rate": "Variable ratio schedule"},
                ],
                3: [
                    {"name": "Sequential Rotary Peg Lock Maze", "mechanism": "Step-dependent sequential unlatching", "reward_rate": "Targeted terminal reward"},
                    {"name": "Scent Discrimination Shell Carousel", "mechanism": "Olfactory target search vs decoy odor", "reward_rate": "Accurate match reward"},
                ],
            },
            self.SPECIES_FELINE: {
                1: [
                    {"name": "Shallow Egg-Carton Forage Board", "mechanism": "Single-claw hooked extraction", "reward_rate": "Immediate feedback"},
                    {"name": "Crinkle Paper Box Scatter", "mechanism": "Auditory & tactile prey-rooting", "reward_rate": "High engagement"},
                ],
                2: [
                    {"name": "Multi-Tube Vertical Tower", "mechanism": "Depth perception & targeted pawing", "reward_rate": "Gravity-assisted drop"},
                    {"name": "Rolling Slow-Release Spheres", "mechanism": "Batting and pursuit predatory sequence", "reward_rate": "Motion-activated"},
                ],
                3: [
                    {"name": "Multi-Level Lidded Compartments", "mechanism": "Lever pushing and latch-flipping", "reward_rate": "Complex manipulation"},
                    {"name": "Vertical Wall-Mounted Maze Run", "mechanism": "Three-dimensional problem solving", "reward_rate": "Territorial pursuit"},
                ],
            },
            self.SPECIES_LAGOMORPH: {
                1: [
                    {"name": "Hanging Timothy Hay Woven Balls", "mechanism": "Natural reach & tug foraging posture", "reward_rate": "Continuous fiber grazing"},
                    {"name": "Apple Wood Chew Sticks with Herb Rub", "mechanism": "Dental incisor attrition & gnawing", "reward_rate": "Olfactory stimulation"},
                ],
                2: [
                    {"name": "Multi-Chamber Cardboard Castle Burrow", "mechanism": "Spatial navigation & digging tunnels", "reward_rate": "Herbal treat rewards"},
                    {"name": "Pellet Stacking Cups", "mechanism": "Nose tipping and lifting cups", "reward_rate": "Hidden forage revelation"},
                ],
                3: [
                    {"name": "Log Foraging Box with Substrate Layers", "mechanism": "Multi-tier excavating & scent tracking", "reward_rate": "Layered dried floral finds"},
                    {"name": "Interactive Sisal Tug Drawers", "mechanism": "Teeth grasp & directional pull", "reward_rate": "Herbal seed cluster access"},
                ],
            },
        }

        species_catalog = catalog.get(species, catalog[self.SPECIES_CANINE])
        return species_catalog.get(tier, species_catalog[2])

    def calculate_senior_joint_profile(
        self,
        weight_kg: float,
        age_years: float,
        species: str = SPECIES_CANINE,
        joint_condition: str = "moderate_osteoarthritis",
    ) -> Dict[str, Any]:
        """
        Assess joint stress index, mobility recommendations, and low-impact sniffing protocol.
        """
        # Baseline joint load index (0 to 100)
        # Weight load scaling: higher body mass creates exponential joint cartilage shear force
        weight_factor = min(40.0, (weight_kg / 30.0) * 35.0)
        age_factor = min(40.0, (age_years / 12.0) * 35.0)

        condition_penalties = {
            "healthy_senior": 5.0,
            "mild_stiffness": 15.0,
            "moderate_osteoarthritis": 25.0,
            "severe_spondylosis_dysplasia": 35.0,
        }
        condition_penalty = condition_penalties.get(joint_condition, 20.0)

        joint_load_index = round(min(100.0, weight_factor + age_factor + condition_penalty), 1)

        # Sniffari protocol calculations
        # 15 minutes of scent exploration = mental fatigue equivalent to 45-60 min brisk walking without joint pounding
        recommended_sniffari_mins = max(15, min(40, int(45 - (joint_load_index * 0.3))))
        recommended_foam_thickness_cm = 10 if weight_kg < 20 else (12 if weight_kg < 35 else 15)
        max_ramp_incline_deg = 18 if joint_load_index > 65 else 24

        mer_data = self.calculate_mer(weight_kg, species, "senior_geriatric")

        return {
            "species": species,
            "weight_kg": weight_kg,
            "age_years": age_years,
            "joint_condition": joint_condition,
            "joint_load_index": joint_load_index,
            "severity_grade": "Grade III: High Articular Care" if joint_load_index > 70 else (
                "Grade II: Moderate Care & Scent Pacing" if joint_load_index > 45 else "Grade I: Preventative Care"
            ),
            "sniffari_walk_mins": recommended_sniffari_mins,
            "walking_equivalent_pace": f"Equivalent to {recommended_sniffari_mins * 3} mins cardiovascular aerobic exhaustion with zero joint impact",
            "orthopedic_foam_depth_cm": recommended_foam_thickness_cm,
            "max_ramp_incline_deg": max_ramp_incline_deg,
            "recommended_runner_coverage_pct": 85 if joint_load_index > 60 else 70,
            "mer_caloric_target_kcal": mer_data["mer_kcal"],
        }

    def generate_html_card(self, profile_type: str = "senior_canine") -> str:
        """
        Generate a pre-rendered, beautifully styled HTML card with live calculation metrics
        ready for embedding into presentation slides.
        """
        if profile_type == "senior_canine":
            # Profile for a 9-year-old 28kg Golden Retriever with moderate osteoarthritis
            data = self.calculate_senior_joint_profile(
                weight_kg=28.0,
                age_years=9.0,
                species=self.SPECIES_CANINE,
                joint_condition="moderate_osteoarthritis"
            )
            return f"""
<div class="calc-widget" style="background: rgba(22, 19, 17, 0.88); border: 1px solid rgba(217, 119, 54, 0.35); border-radius: 14px; padding: 18px 22px; margin-top: 15px; box-shadow: 0 12px 30px rgba(0,0,0,0.45); backdrop-filter: blur(12px);">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(232, 213, 196, 0.12); padding-bottom: 10px; margin-bottom: 12px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #d97736; box-shadow: 0 0 10px #d97736;"></span>
            <span style="font-family: 'Fraunces', serif; font-size: 1.05rem; color: #fdfbf7; font-weight: 600;">Live Engine: Senior Canine Biometrics</span>
        </div>
        <span style="font-size: 0.75rem; background: rgba(217, 119, 54, 0.18); color: #e0a96d; padding: 3px 9px; border-radius: 20px; border: 1px solid rgba(217,119,54,0.3); font-weight: 600;">enrichment_calculator.py</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 12px;">
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">RER (Kleiber)</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #e8d5c4; font-family: 'Fraunces', serif;">{data['mer_caloric_target_kcal'] / 1.2:.0f} <span style="font-size: 0.75rem; font-weight: 400; color: #87a987;">kcal</span></div>
            <div style="font-size: 0.68rem; color: #8a8275;">70 × (28kg)^0.75</div>
        </div>
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Senior MER</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #e0a96d; font-family: 'Fraunces', serif;">{data['mer_caloric_target_kcal']:.0f} <span style="font-size: 0.75rem; font-weight: 400; color: #87a987;">kcal/d</span></div>
            <div style="font-size: 0.68rem; color: #8a8275;">Multiplier: 1.2× RER</div>
        </div>
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Joint Load Index</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #d97736; font-family: 'Fraunces', serif;">{data['joint_load_index']} <span style="font-size: 0.75rem; font-weight: 400; color: #a89f91;">/ 100</span></div>
            <div style="font-size: 0.68rem; color: #e0a96d;">{data['severity_grade'].split(':')[0]}</div>
        </div>
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Daily Sniffari</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #87a987; font-family: 'Fraunces', serif;">{data['sniffari_walk_mins']} <span style="font-size: 0.75rem; font-weight: 400; color: #a89f91;">mins</span></div>
            <div style="font-size: 0.68rem; color: #8a8275;">Zero articular shear</div>
        </div>
    </div>
    <div style="font-size: 0.8rem; color: #d5cbbf; line-height: 1.5; background: rgba(18, 17, 16, 0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid #87a987;">
        <strong>Biomechanical Prescription:</strong> {data['orthopedic_foam_depth_cm']}cm medical viscoelastic foam bedding &bull; Max ramp gradient &le; {data['max_ramp_incline_deg']}&deg; &bull; {data['recommended_runner_coverage_pct']}% non-slip floor coverage &bull; <em>{data['walking_equivalent_pace']}</em>.
    </div>
</div>
"""
        elif profile_type == "foraging_puzzle":
            # Profile for cognitive foraging breakdown
            data = self.calculate_cognitive_foraging(
                weight_kg=22.0,
                species=self.SPECIES_CANINE,
                life_stage="adult_neutered",
                cognitive_tier=2
            )
            return f"""
<div class="calc-widget" style="background: rgba(22, 19, 17, 0.88); border: 1px solid rgba(135, 169, 135, 0.35); border-radius: 14px; padding: 18px 22px; margin-top: 15px; box-shadow: 0 12px 30px rgba(0,0,0,0.45); backdrop-filter: blur(12px);">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(232, 213, 196, 0.12); padding-bottom: 10px; margin-bottom: 12px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #87a987; box-shadow: 0 0 10px #87a987;"></span>
            <span style="font-family: 'Fraunces', serif; font-size: 1.05rem; color: #fdfbf7; font-weight: 600;">Live Engine: Contra-Freeloading & Foraging Architecture</span>
        </div>
        <span style="font-size: 0.75rem; background: rgba(135, 169, 135, 0.18); color: #87a987; padding: 3px 9px; border-radius: 20px; border: 1px solid rgba(135,169,135,0.3); font-weight: 600;">enrichment_calculator.py</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 12px;">
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Total Daily MER</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #e8d5c4; font-family: 'Fraunces', serif;">{data['mer_data']['mer_kcal']:.0f} <span style="font-size: 0.75rem; font-weight: 400; color: #87a987;">kcal/d</span></div>
            <div style="font-size: 0.68rem; color: #8a8275;">Canine (22kg, Adult)</div>
        </div>
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Contra-Freeloading</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #e0a96d; font-family: 'Fraunces', serif;">{data['foraging_kcal']:.0f} <span style="font-size: 0.75rem; font-weight: 400; color: #d97736;">kcal</span></div>
            <div style="font-size: 0.68rem; color: #8a8275;">30% of daily calories</div>
        </div>
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Cognitive Tier</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #d97736; font-family: 'Fraunces', serif;">Tier {data['cognitive_tier']} <span style="font-size: 0.75rem; font-weight: 400; color: #a89f91;">/ 3</span></div>
            <div style="font-size: 0.68rem; color: #87a987;">Intermediate Dynamic</div>
        </div>
        <div style="background: rgba(35, 30, 26, 0.7); padding: 10px; border-radius: 8px; border: 1px solid rgba(214, 180, 150, 0.1);">
            <div style="font-size: 0.72rem; color: #a89f91; text-transform: uppercase; letter-spacing: 0.05em;">Target Pacing</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #87a987; font-family: 'Fraunces', serif;">{data['daily_sessions']} &times; {data['recommended_duration_minutes']} <span style="font-size: 0.75rem; font-weight: 400; color: #a89f91;">min</span></div>
            <div style="font-size: 0.68rem; color: #8a8275;">Dopaminergic cycle</div>
        </div>
    </div>
    <div style="font-size: 0.8rem; color: #d5cbbf; line-height: 1.5; background: rgba(18, 17, 16, 0.6); padding: 8px 12px; border-radius: 6px; border-left: 3px solid #d97736;">
        <strong>Prescribed Apparatus:</strong> <em>{data['puzzles'][0]['name']}</em> ({data['puzzles'][0]['mechanism']}) &bull; <em>{data['puzzles'][1]['name']}</em> ({data['puzzles'][1]['mechanism']}). Stimulates active problem-solving without cognitive distress.
    </div>
</div>
"""
        return ""


def main():
    parser = argparse.ArgumentParser(
        description="Companion Animal Welfare, Nutrition & Cognitive Enrichment Calculator"
    )
    parser.add_argument("--species", choices=["canine", "feline", "lagomorph"], default="canine", help="Species")
    parser.add_argument("--weight", type=float, default=25.0, help="Weight in kilograms")
    parser.add_argument("--age", type=float, default=8.0, help="Age in years")
    parser.add_argument("--stage", default="senior_geriatric", help="Life stage multiplier key")
    parser.add_argument("--joint-condition", default="moderate_osteoarthritis", help="Joint condition status")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3], default=2, help="Cognitive puzzle tier")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--demo", action="store_true", help="Run comprehensive multi-species demonstration")

    args = parser.parse_args()
    calculator = CompanionEnrichmentCalculator()

    if args.demo:
        print("\n" + "=" * 78)
        print(" COMPANION ANIMAL METABOLIC & COGNITIVE ENRICHMENT ENGINE DEMO")
        print(" Authors: Inbal Ohana (ענבל אהרה) & Noy Shalev (נוי שלו)")
        print(" Course:  Generative AI, LLMs & Agents | Dr. Yoram Segal | Bar-Ilan University")
        print("=" * 78 + "\n")

        # 1. Senior Golden Retriever
        sr_dog = calculator.calculate_senior_joint_profile(28.0, 9.5, "canine", "moderate_osteoarthritis")
        print("🐾 [CANINE SENIOR PROFILE]")
        print(f"  Target Pet: 9.5 yr Golden Retriever, 28.0 kg")
        print(f"  Resting Energy Requirement (RER): {calculator.calculate_rer(28.0)} kcal/day")
        print(f"  Senior Maintenance (MER):         {sr_dog['mer_caloric_target_kcal']} kcal/day")
        print(f"  Joint Stress Index:               {sr_dog['joint_load_index']} / 100 ({sr_dog['severity_grade']})")
        print(f"  Daily Sniffari Protocol:          {sr_dog['sniffari_walk_mins']} mins low-intensity olfactory tracking")
        print(f"  Home Environmental Adaptation:    {sr_dog['orthopedic_foam_depth_cm']}cm foam bed, max {sr_dog['max_ramp_incline_deg']} deg ramp\n")

        # 2. Adult Feline Contra-freeloading
        cat_forage = calculator.calculate_cognitive_foraging(4.5, "feline", "adult_neutered", 2)
        print("🐱 [FELINE COGNITIVE FORAGING PROFILE]")
        print(f"  Target Pet: 4.0 yr Domestic Shorthair, 4.5 kg")
        print(f"  Daily MER:                        {cat_forage['mer_data']['mer_kcal']} kcal/day")
        print(f"  Foraging Caloric Budget (25%):    {cat_forage['foraging_kcal']} kcal/day")
        print(f"  Recommended Puzzle Apparatus:     {cat_forage['puzzles'][0]['name']}")
        print(f"  Engagement Pacing:                {cat_forage['daily_sessions']} sessions of {cat_forage['recommended_duration_minutes']} mins\n")

        # 3. Lagomorph Hay & Digestion Profile
        rabbit_mer = calculator.calculate_mer(2.2, "lagomorph", "adult_maintenance")
        print("🐰 [LAGOMORPH DIETARY & FORAGING PROFILE]")
        print(f"  Target Pet: 3.0 yr Holland Lop, 2.2 kg")
        print(f"  RER (70 * 2.2^0.75):              {rabbit_mer['rer_kcal']} kcal/day")
        print(f"  Maintenance Requirement:          {rabbit_mer['mer_kcal']} kcal/day")
        print(f"  Baseline Forage Requirement:      85%+ long-strand Timothy hay + cecotrope recycling")
        print(f"  Enrichment Device:                Woven Timothy hay sphere + Apple wood gnawing branch\n")
        print("=" * 78)
        return

    # Individual calculation
    rer = calculator.calculate_rer(args.weight)
    mer_res = calculator.calculate_mer(args.weight, args.species, args.stage)
    joint_res = calculator.calculate_senior_joint_profile(args.weight, args.age, args.species, args.joint_condition)
    forage_res = calculator.calculate_cognitive_foraging(args.weight, args.species, args.stage, args.tier)

    combined = {
        "authors": ["Inbal Ohana (ענבל אהרה)", "Noy Shalev (נוי שלו)"],
        "institution": "Bar-Ilan University | Dr. Yoram Segal",
        "inputs": vars(args),
        "metabolic": mer_res,
        "joint_profile": joint_res,
        "cognitive_foraging": forage_res,
    }

    if args.json:
        print(json.dumps(combined, indent=2))
    else:
        print(f"RER: {rer} kcal | MER: {mer_res['mer_kcal']} kcal | Joint Index: {joint_res['joint_load_index']} | Sniffari: {joint_res['sniffari_walk_mins']} min")


if __name__ == "__main__":
    main()
