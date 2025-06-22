# 🧬 ColabFold Output: Wild-Type T4 Lysozyme

This folder contains the output files from running [ColabFold](https://github.com/sokrypton/ColabFold) on the wild-type sequence of T4 Lysozyme using AlphaFold2.

## 📁 File Descriptions

| File | Description |
|------|-------------|
| `wt_structure.pdb` | Best-ranked predicted structure (formerly rank_001) |
| `plddt_scores.png` | Plot showing per-residue confidence scores (pLDDT) |
| `msa_coverage.png` | Plot showing MSA coverage per residue |
| `scores_rank_001.json` | Prediction metadata and confidence metrics for the best model |
| `msa_input.a3m` | Multiple sequence alignment file used by ColabFold |
| `cite.bibtex` | Citations for the tools/databases used in this prediction |

---

## 🧪 Notes

- Structure prediction was run using **ColabFold (AlphaFold2 mode)** with `num_recycles=3` and `num_models=5`.
- No templates or Amber refinement were used.
- The best model was selected based on pLDDT score (ColabFold default ranking).

