from mpi4py import MPI
import numpy as np
import sys
import vina
from vina import Vina

v = Vina(sf_name='vina')

v.set_receptor('1iep_receptor.pdbqt')

file1 = open('TestSet/newFiles.txt')

for line in file1:
    ligand = line.strip()
    v.set_ligand_from_file(ligand)
    print_ligand_center(ligand)
    v.compute_vina_maps(center=[15.90, 53.903, 16.917], box_size=[20,20,20]
#    v.compute_vina_maps(center=[center['center_x'], center['center_y'], center['center_z']], box_size=[size['size_x'], size['size_y'], size['size_z']])
    
# print_ligand_center(mkprep.setup)

# Score the current pose
#    energy = v.score()
#    print('Score before minimization: %.3f (kcal/mol)' % energy[0])

# Minimized locally the current pose
#    energy_minimized = v.optimize()
#    print('Score after minimization : %.3f (kcal/mol)' % energy_minimized[0])
#    v.write_pose('1iep_ligand_minimized.pdbqt', overwrite=True)

# Dock the ligand
    v.dock(exhaustiveness=32, n_poses=20)
    v.write_poses('1iep_ligand_vina_out.pdbqt', n_poses=5, overwrite=True)

