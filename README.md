As an example, to run the MCMIX on One-step Matrix Game:
```shell
python src/main.py --config=mcc_qmix --env-config=matrix_game
```
As an example, to run the MCMIX on predator-prey with td_lambda=0.3:
```shell
python src/main.py --config=mcc_qmix --env-config=pred_prey_punish with td_lambda=0.3
```

As an example, to run the MCMIX on 3s5z with epsilon annealed over 1mil timesteps:
```shell
python src/main.py --config=mcc_qmix --env-config=sc2 with env_args.map_name=3s5z t_max=2010000 epsilon_anneal_time=100000
```

python src/main.py --config=mcc_qmix --env-config=pred_prey_punish
