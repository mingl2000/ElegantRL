import torch as th
from torch.cuda import graph

GPU_ID = -1
NODES = 100
GRAPH_TYPE = 'BA'
PREFIXES = ["BA_900", "BA_1000", "BA_1100", "BA_1200", "BA_2000", "BA_5000"]  # Replace with your desired prefixes


def calc_device(gpu_id: int):
    return th.device(f'cuda:{gpu_id}' if th.cuda.is_available() and gpu_id >= 0 else 'cpu')


NETWORKSAVEPATH = "pretrained_agent/eco/network_best_BA_40spin.pth"
GRAPHSAVELOC = "../../data/syn_BA"

DEVICE = calc_device(GPU_ID)
if GRAPH_TYPE == 'BA':
    if NODES == 20:
        N_SPINS_TRAIN = 20
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NODES == 40:
        N_SPINS_TRAIN = 40
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NODES == 60:
        N_SPINS_TRAIN = 60
        NB_STEPS = 5000000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 300000
        SAVE_NETWORK_FREQUENCY = 200000
        TEST_FREQUENCY = 20000
    elif NODES == 100:
        N_SPINS_TRAIN = 100
        NB_STEPS = 8000000
        REPLAY_START_SIZE = 1500
        REPLAY_BUFFER_SIZE = 10000
        UPDATE_TARGET_FREQUENCY = 2500
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 400000
        TEST_FREQUENCY = 50000
    elif NODES == 200:
        N_SPINS_TRAIN = 200
        NB_STEPS = 8000000
        REPLAY_START_SIZE = 3000
        REPLAY_BUFFER_SIZE = 15000
        UPDATE_TARGET_FREQUENCY = 4000
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 80000
        TEST_FREQUENCY = 10000
elif GRAPH_TYPE == 'ER':
    if NODES == 20:
        N_SPINS_TRAIN = 20
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NODES == 40:
        N_SPINS_TRAIN = 40
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NODES == 60:
        N_SPINS_TRAIN = 60
        NB_STEPS = 5000000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 300000
        SAVE_NETWORK_FREQUENCY = 200000
        TEST_FREQUENCY = 20000
    elif NODES == 100:
        N_SPINS_TRAIN = 100
        NB_STEPS = 8000000
        REPLAY_START_SIZE = 1500
        REPLAY_BUFFER_SIZE = 10000
        UPDATE_TARGET_FREQUENCY = 2500
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 400000
        TEST_FREQUENCY = 50000
    elif NODES == 200:
        N_SPINS_TRAIN = 200
        NB_STEPS = 10000000
        REPLAY_START_SIZE = 3000
        REPLAY_BUFFER_SIZE = 15000
        UPDATE_TARGET_FREQUENCY = 4000
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 400000
        TEST_FREQUENCY = 50000
