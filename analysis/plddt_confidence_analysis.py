import os
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define paths and sample identifiers
base_path = "../data/colabfold_output"
samples = ["wt_model", "mutant_0001", "mutant_0002", "mutant_0003", "mutant_0004", "mutant_0005"]

# Storage lists
labels = []
plddts = []
ranking_confidences = []

# Extract scores from JSON files
for sample in samples:
    json_path = os.path.join(base_path, sample, "scores_rank_001.json")
    with open(json_path, 'r') as f:
        data = json.load(f)
        labels.append(sample)

        # Handle plddt as scalar or list
        plddt = data.get("plddt", 0)
        if isinstance(plddt, list):
            plddts.append(np.mean(plddt))
        else:
            plddts.append(plddt)

        # Handle ranking_confidence
        rc = data.get("ranking_confidence", 0)
        if isinstance(rc, list):
            ranking_confidences.append(np.mean(rc))
        else:
            ranking_confidences.append(rc)

# Set seaborn style
sns.set(style="darkgrid")

# Plot pLDDT scores
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=labels, y=plddts, color='#8B6F9C')

# Customize appearance
plt.title("Average pLDDT Confidence Score per Model", fontsize=14, fontweight='bold')
plt.ylabel("pLDDT (0–100)", fontsize=12, fontweight='bold')
plt.xticks(rotation=45, fontsize=10, fontweight='bold')
plt.yticks(fontsize=10)

for bar, score in zip(barplot.patches, plddts):
    barplot.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() / 2,  # <-- center vertically
        f"{score:.1f}",
        ha='center',
        va='center',
        fontsize=11,
        fontweight='bold',
        color='white'
    )


# Save and display
plt.tight_layout()
plt.savefig("../results/figures/plddt_scores_comparison.png", dpi=300)
plt.show()
