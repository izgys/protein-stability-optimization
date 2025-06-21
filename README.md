# 🧬 Protein Stability Optimization with AI + Molecular Dynamics

**Author:** [Your Name]  
**Project Type:** Computational Protein Design + Machine Learning + Molecular Simulation  
**Status:** 🚧 In Progress  
**Estimated Time:** ~5 weeks (1 hour/day)

---

## 📍 Project Overview

This project explores the use of **AI-based protein sequence design** tools, such as **ProteinMPNN** and **ThermoMPNN**, to generate stabilizing mutations in a well-characterized model protein. The stability of the wild-type and designed mutants is then evaluated using **Molecular Dynamics (MD)** simulations and structural analysis.

The entire workflow is built to be a practical, portfolio-worthy demonstration of integrating **machine learning**, **protein engineering**, and **physics-based simulation**.

---

## 🎯 Objectives

- ✅ Predict stabilizing mutations using **ProteinMPNN** or **ThermoMPNN**
- ✅ Simulate the wild-type and mutant protein structures using **OpenMM** or **GROMACS**
- ✅ Analyze simulation results (RMSD, hydrogen bonds, ΔΔG proxies)
- ✅ Evaluate and visualize structural stability differences
- ✅ Create a clean, reproducible, and documented project for your GitHub portfolio

---

## 🛠️ Tools and Technologies

| Tool/Library        | Purpose                                  |
|---------------------|------------------------------------------|
| **ProteinMPNN**     | AI-based sequence design / inverse folding |
| **AlphaFold2 / ColabFold** | Protein structure prediction              |
| **OpenMM** or **GROMACS** | Molecular Dynamics engine                  |
| **Python + NumPy + matplotlib** | Data analysis and plotting          |
| **PyMOL / VMD**      | Structure visualization (optional)       |

---

## 🧪 Protein Target

- **Protein:** T4 Lysozyme (mutant L99A or wild-type)
- **PDB ID:** [2LZM](https://www.rcsb.org/structure/2LZM)
- **Length:** ~164 residues
- **Why this target?** It's well-studied, small, and has known stability mutants — ideal for benchmarking AI design tools and simulations.

---

## 🧭 Workflow Summary

```mermaid
graph TD
    A[Start: Wild-Type Structure] --> B[Run ProteinMPNN for Mutant Design]
    B --> C[Select Top Mutants]
    C --> D[Run AlphaFold2 to Predict 3D Structures]
    D --> E[Prepare MD Systems (WT + Mutants)]
    E --> F[Run MD Simulations]
    F --> G[Analyze RMSD, H-Bonds, ΔE]
    G --> H[Compare Stability]
