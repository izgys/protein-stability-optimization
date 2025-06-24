from pdbfixer import PDBFixer
from openmm.app import PDBFile

fixer = PDBFixer(filename='./t4_lysozyme_wt_for_mpnn.pdb')
fixer.findMissingResidues()
fixer.findMissingAtoms()
fixer.addMissingAtoms()
fixer.removeHeterogens(True)  # Removes ligands, waters, etc.

PDBFile.writeFile(fixer.topology, fixer.positions, open('fixed_structure.pdb', 'w'))
