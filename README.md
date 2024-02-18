Value decomposition with maximum correntropy for multi-agent deep reinforcement learning

As an example, to run the MCMIX on One-step Matrix Game:
```shell
python src/main.py --config=mcc_qmix --env-config=matrix_game
```
As an example, to run the MCMIX on predator-prey:
```shell
python src/main.py --config=mcc_qmix --env-config=pred_prey_punish
```

As an example, to run the MCMIX on 3s5z_vs_3s6z with epsilon annealed over 5mil timesteps:
```shell
python src/main.py --config=mcc_qmix --env-config=sc2 with env_args.map_name=3s5z_vs_3s6z t_max=5010000 epsilon_anneal_time=500000
```
