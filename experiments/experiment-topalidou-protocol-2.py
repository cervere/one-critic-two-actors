# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from experiment import Experiment

def session(exp):
    exp.model.setup()
    records = np.zeros((exp.n_block, exp.n_trial), dtype=exp.task.records.dtype)

    # Day 1 : GPi OFF
    g1 = exp.model["GPi:cog → THL:cog"].gain
    g2 = exp.model["GPi:mot → THL:mot"].gain
    exp.model["GPi:cog → THL:cog"].gain = 0
    exp.model["GPi:mot → THL:mot"].gain = 0
    for trial in exp.task:
        exp.model.process(exp.task, trial, model = exp.model)
    records[0] = exp.task.records

    # Day 2: GPi ON
    exp.model["GPi:cog → THL:cog"].gain = g1
    exp.model["GPi:mot → THL:mot"].gain = g2
    for trial in exp.task:
        exp.model.process(exp.task, trial, model = exp.model)
    records[1] = exp.task.records

    # Day 1 : GPi OFF
#    exp.model["GPi:cog → THL:cog"].gain = 0
#    exp.model["GPi:mot → THL:mot"].gain = 0
#    for trial in exp.task:
#        exp.model.process(exp.task, trial, model = exp.model)
#    records[2] = exp.task.records
        
    return records


experiment = Experiment(model = "model-topalidou.json",
                        task = "task-topalidou.json",
                        result = "data/experiment-topalidou-protocol-2.npy",
                        report = "data/experiment-topalidou-protocol-2.txt",
                        n_session = 12, n_block = 2, seed = None)
#                        n_session = 12, n_block = 2, seed = 533)
records = experiment.run(session, "Protocol 2")


# Save performance (one column per session)
# -----------------------------------------------------------------------------
# P = np.squeeze(records["best"][:,0])
# np.savetxt("data/experiment-topalidou-protocol-2-D1-P.csv", P.T, fmt="%d", delimiter=",")
# P = np.squeeze(records["best"][:,1])
# np.savetxt("data/experiment-topalidou-protocol-2-D2-P.csv", P.T, fmt="%d", delimiter=",")
# P = np.squeeze(records["best"][:,2])
# np.savetxt("data/experiment-topalidou-protocol-2-D3-P.csv", P.T, fmt="%d", delimiter=",")
# P = np.squeeze(records["RT"][:,0])
# np.savetxt("data/experiment-topalidou-protocol-2-D1-RT.csv", P.T, fmt="%.4f", delimiter=",")
# P = np.squeeze(records["RT"][:,1])
# np.savetxt("experiment-topalidou-protocol-2-D2-RT.csv", P.T, fmt="%.4f", delimiter=",")
# P = np.squeeze(records["RT"][:,2])
# np.savetxt("experiment-topalidou-protocol-2-D3-RT.csv", P.T, fmt="%.4f", delimiter=",")


# Textual results
# -----------------------------------------------------------------------------
P = np.squeeze(records["best"][:,0,:25])
P = P.mean(axis=len(P.shape)-1)
print("D1 start: %.3f ± %.3f" % (P.mean(), P.std()))
P = np.squeeze(records["best"][:,0,-25:])
P = P.mean(axis=len(P.shape)-1)
print("D1 end:   %.3f ± %.3f" % (P.mean(), P.std()))

P = np.squeeze(records["RT"][:,0])
print("D1 mean RT: %.3f ± %.3f" % (P.mean(), P.std()))

print()

P = np.squeeze(records["best"][:,1,:25])
P = P.mean(axis=len(P.shape)-1)
print("D2 start: %.3f ± %.3f" % (P.mean(), P.std()))
P = np.squeeze(records["best"][:,1,-25:])
P = P.mean(axis=len(P.shape)-1)
print("D2 end:   %.3f ± %.3f" % (P.mean(), P.std()))

P = np.squeeze(records["RT"][:,1])
print("D2 mean RT: %.3f ± %.3f" % (P.mean(), P.std()))

# print()

# P = np.squeeze(records["best"][:,2,:25])
# P = P.mean(axis=len(P.shape)-1)
# print("D3 start: %.3f ± %.3f" % (P.mean(), P.std()))
# P = np.squeeze(records["best"][:,2,-25:])
# P = P.mean(axis=len(P.shape)-1)
# print("D3 end:   %.3f ± %.3f" % (P.mean(), P.std()))

# P = np.squeeze(records["RT"][:,2])
# print("D3 mean RT: %.3f ± %.3f" % (P.mean(), P.std()))

print("-"*30)



# Graphical results
# -----------------------------------------------------------------------------
from figures import *


records = records[:,:2,:]
title = "Protocol 2"
filename = "data/experiment-topalidou-protocol-2-P-all.pdf"
figure_P_all(records, [0, 1], title=title, filename=filename)


# figure_H_P(records, [0,1,0], "Protocol 2", "data/experiment-topalidou-protocol-2-H-P.pdf")
# figure_H_RT(records, [0,1,0], "Protocol 2", "data/experiment-topalidou-protocol-2-H-RT.pdf")

#figure_P(records, GPi=[0,1,0], save=False, show=True,
#         title="Protocol 2", filename="data/experiment-topalidou-protocol-2-P.pdf")
#figure_V(records, GPi=[0,1,0], 
#         title="Protocol 2", filename="data/experiment-topalidou-protocol-2-V.pdf")

# filename = "data/experiment-topalidou-protocol-2-P-individual.pdf"
# figure_P_individual(records, GPi=[0, 1, 0],
#                     title="Protocol 2", filename=filename)

# filename = "data/experiment-topalidou-protocol-2-RT-individual.pdf"
# figure_RT_individual(records, GPi=[0, 1, 0],
#                      title="Protocol 2", filename=filename)

# figure_RT(records, [0,1,0], "Protocol 2", "data/experiment-topalidou-protocol-2-RT.pdf")
