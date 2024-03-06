experiments_mapping = { 
                        "Adam's ε": "epsilon",
                        "Batch Size": "batch_sizes",
                        "Conv. Activation Function": "layer_funct_conv",
                        "Convolutional Normalization": "normalizations_convs", 
                        "Convolutional Width": "CNN_widths",
                        "Dense Activation Function": "layer_funct_dense",
                        "Dense Normalization": "normalizations",
                        "Dense Width": "widths",
                        "Discount Factor": "gammas",
                        "Exploration ε": "eps_train",
                        "Learning Rate": "learning_rate",
                        "Minimum Replay History": "min_replay_history",
                        "Number of Atoms": "num_atoms", 
                        "Number of Convolutional Layers": "convs", 
                        "Number of Dense Layers": "depths",
                        "Replay Capacity": "replay_capacity",
                        "Reward Clipping": "clip_rewards",
                        "Target Update Period": "target_update_periods",
                        "Update Horizon": "update_horizon",
                        "Update Period": "update_periods",
                        "Weight Decay": "weightdecay",
                    }

ATARI_100K_GAMES = [
            'Alien', 'Amidar', 'Assault', 'Asterix', 'BankHeist', 'BattleZone',
            'Boxing', 'Breakout', 'ChopperCommand', 'CrazyClimber', 'DemonAttack',
            'Freeway', 'Frostbite', 'Gopher', 'Hero', 'Jamesbond', 'Kangaroo',
            'Krull', 'KungFuMaster', 'MsPacman', 'Pong', 'PrivateEye', 'Qbert',
            'RoadRunner', 'Seaquest', 'UpNDown'
            ]