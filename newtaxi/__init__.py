from gym.envs.registration import register

register(
    id='NewTaxi-v0',
    entry_point='newtaxi.newtaxi:NewTaxi',
)