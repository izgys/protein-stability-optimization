import MDAnalysis as mda
from MDAnalysis.analysis.rms import RMSD
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn aesthetic style
sns.set(style='darkgrid')

# Path to wild-type PDB
wt_path = '../data/colabfold_output/wt_model/wt_structure_rank_001_alphafold2.pdb'

# Mutant list
mutants = [
    'mutant_0001',
    'mutant_0002',
    'mutant_0003',
    'mutant_0004',
    'mutant_0005',
]

# Load reference (WT)
ref = mda.Universe(wt_path)
ref_atoms = ref.select_atoms('protein and backbone')

# Calculate RMSD for each mutant
rmsd_results = {}

for mutant in mutants:
    path = f'../data/colabfold_output/{mutant}/{mutant}_rank_001_alphafold2.pdb'
    mobile = mda.Universe(path)
    mobile_atoms = mobile.select_atoms('protein and backbone')

    # RMSD alignment and calculation
    rmsd = RMSD(mobile_atoms, ref_atoms, select='backbone').run()
    rmsd_value = rmsd.rmsd[-1, 2]  # Last frame, RMSD column
    rmsd_results[mutant] = rmsd_value
    print(f'{mutant}: RMSD = {rmsd_value:.3f} Å')

# Plotting
plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    x=list(rmsd_results.keys()),
    y=list(rmsd_results.values()),
    color=sns.color_palette()[0],  # Use default Seaborn blue
    edgecolor=None
)

# Annotate values inside bars
for bar, value in zip(barplot.patches, rmsd_results.values()):
    height = bar.get_height()
    barplot.annotate(f'{value:.3f}',
                     xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                     ha='center', va='center',
                     fontsize=11, fontweight='bold', color='white')

# Styling
plt.ylabel('RMSD to WT (Å)', fontsize=12, weight='bold')
plt.title('Backbone RMSD of Mutants vs WT', fontsize=14, weight='bold')
plt.xticks(rotation=45, fontsize=10, weight='bold')
plt.yticks(fontsize=10)
plt.tight_layout()

# Save figure
plt.savefig('../results/figures/mutant_vs_wt_rmsd.png', dpi=300)
plt.show()
