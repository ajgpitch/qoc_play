# -*- coding: utf-8 -*-
"""
Created on 10 April 2024
@author: Alexander Pitchford
@email: alex.pitchford@gmail.com

The system in this example is a single qubit in a constant field in z
with a variable control field in x
The target evolution is the Hadamard gate irrespective of global phase

The user can experiment with the timeslicing, by means of changing the
number of timeslots and/or total time for the evolution.
Different initial (starting) pulse types can be tried.
The initial and final pulses are displayed in a plot
"""
#import sys
import numpy as np
import matplotlib.pyplot as plt
import qutip as qt
#import datetime

from qutip import Qobj, identity, sigmax, sigmaz
#from qutip import hadamard_transform
#from qutip.core import hadamard_transform
from qutip import gates

#QuTiP control modules
#import qutip.control.pulseoptim as cpo

example_name = 'Hadamard'

# ****************************************************************
# Define the physics of the problem

nSpins = 1

H_d = sigmaz()
H_c = [sigmax()]
# Number of ctrls
n_ctrls = len(H_c)

U_0 = identity(2**nSpins)
# Hadamard gate
#U_targ = Qobj(np.array([[1,1],[1,-1]], dtype=complex)/np.sqrt(2))
# Hadamard is determinant -1, so need prefactor phase for SU fidelity
#U_targ = 1.0j*hadamard_transform(nSpins)
U_targ = gates.hadamard_transform(nSpins)
# ***** Define time evolution parameters *****
# Number of time slots
n_ts = 100
# Time allowed for the evolution
evo_time = 6

# ***** Define the termination conditions *****
# Fidelity error target
fid_err_targ = 1e-10
# Maximum iterations for the optisation algorithm
max_iter = 200
# Maximum (elapsed) time allowed in seconds
max_wall_time = 120
# Minimum gradient (sum of gradients squared)
# as this tends to 0 -> local minima has been found
min_grad = 1e-20


# # Initial pulse type
# # pulse type alternatives: RND|ZERO|LIN|SINE|SQUARE|SAW|TRIANGLE|
# p_type = 'ZERO'
# # *************************************************************
# # File extension for output files

# f_ext = "{}_n_ts{}_ptype{}.txt".format(example_name, n_ts, p_type)

# # Run the optimisation
# print("\n***********************************")
# print("Starting pulse optimisation")
# result = cpo.optimize_pulse_unitary(H_d, H_c, U_0, U_targ, n_ts, evo_time,
#                 fid_err_targ=fid_err_targ, min_grad=min_grad,
#                 max_iter=max_iter, max_wall_time=max_wall_time,
# #                dyn_params={'oper_dtype':Qobj},
#                 #phase_option='SU',
#                 fid_params={'phase_option':'PSU'},
#                 out_file_ext=f_ext, init_pulse_type=p_type,
#                 log_level=log_level, gen_stats=True)

# print("\n***********************************")
# print("Optimising complete. Stats follow:")
# result.stats.report()
# print("\nFinal evolution\n{}\n".format(result.evo_full_final))

# print("********* Summary *****************")
# print("Initial fidelity error {}".format(result.initial_fid_err))
# print("Final fidelity error {}".format(result.fid_err))
# print("Final gradient normal {}".format(result.grad_norm_final))
# print("Terminated due to {}".format(result.termination_reason))
# print("Number of iterations {}".format(result.num_iter))
# #print("wall time: ", result.wall_time
# print("Completed in {} HH:MM:SS.US".\
#         format(datetime.timedelta(seconds=result.wall_time)))
# print("***********************************")

# # Plot the initial and final amplitudes
# fig1 = plt.figure()
# ax1 = fig1.add_subplot(2, 1, 1)
# ax1.set_title("Initial control amps")
# #ax1.set_xlabel("Time")
# ax1.set_ylabel("Control amplitude")
# for j in range(n_ctrls):
#     ax1.step(result.time,
#              np.hstack((result.initial_amps[:, j], result.initial_amps[-1, j])),
#              where='post')

# ax2 = fig1.add_subplot(2, 1, 2)
# ax2.set_title("Optimised Control Sequences")
# ax2.set_xlabel("Time")
# ax2.set_ylabel("Control amplitude")
# for j in range(n_ctrls):
#     ax2.step(result.time,
#              np.hstack((result.final_amps[:, j], result.final_amps[-1, j])),
#              where='post')
# plt.tight_layout()
# plt.show()
