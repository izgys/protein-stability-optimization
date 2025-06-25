# 🧬 ColabFold Output: T4 Lysozyme WT and Mutants

This folder contains the output files from running [ColabFold](https://github.com/sokrypton/ColabFold) on the **wild-type (WT)** sequence of T4 Lysozyme and five **mutant sequences** generated with ProteinMPNN.

Each model (WT and mutants) has its own subfolder inside `colabfold_output/`, following the structure:

- `wt_model/`
- `mutant_0001/`
- `mutant_0002/`
- ...
- `mutant_0005/`

All output files from ColabFold are stored separately inside each corresponding folder.

## 📁 File Descriptions

| File | Description |
|------|-------------|
| `*_rank_001_alphafold2.pdb` | Best-ranked predicted structure (formerly rank_001) |
| `plddt_scores.png` | Plot showing per-residue confidence scores (pLDDT) |
| `msa_coverage.png` | Plot showing MSA coverage per residue |
| `scores_rank_001.json` | Prediction metadata and confidence metrics for the best model |
| `msa_input.a3m` | Multiple sequence alignment file used by ColabFold |

> Note: The `cite.bibtex` file with tool/database citations is shared globally and located at `colabfold_output/cite.bibtex`.

---

## 🧪 Run Parameters

- Structure prediction was run using **ColabFold (AlphaFold2 mode)** with:
  - `num_models = 5`
  - `num_recycles = 3`
  - `template_mode = none`
  - `use_amber = False`
- No templates or Amber relaxation were used.
- The best model was selected based on internal AlphaFold pLDDT confidence score.

---

## 📊 Interpretation of Key Plots

### 🔵 `plddt_scores.png` – Per-Residue Confidence

This plot shows AlphaFold’s **predicted confidence (pLDDT)** for each residue in the model.

- **Y-axis:** Confidence score (0–100)
- **X-axis:** Residue index
- **Lines:** Different AlphaFold models (rank_1 to rank_5)

#### ✅ How to interpret:
- Scores **>90** = very high confidence (blue in structure)
- Scores **<70** = lower confidence or potential disorder
- Sharp dips often indicate **low evolutionary support or flexible regions**
- The model chosen (`rank_001`) typically has the **most stable high-confidence regions**

---

### 🔴 `msa_coverage.png` – Sequence Alignment Depth

This plot shows how many homologous sequences were aligned to each residue (via MMseqs2).

- **X-axis:** Residue index
- **Y-axis:** Sequences in the MSA
- **Black line:** Number of aligned sequences per position (coverage)
- **Color map:** Sequence identity to query (red = low identity, blue = high)

#### ✅ How to interpret:
- **High coverage (black line up)** → strong MSA → better AlphaFold confidence
- **Sparse or red zones** → weak evolutionary signal → likely less reliable structure
- Matches well with dips in `plddt_scores.png`

Together, these plots give a **reliable view of where your structure is well-supported** and where it’s more uncertain.

---

## 📸 Additional Visualization

Annotated 3D renderings of the predicted structures colored by pLDDT score are available in:

results/figures/wt_structure_plddt_colored.png

This image was exported from the ColabFold notebook and visually complements the numerical confidence scores.


