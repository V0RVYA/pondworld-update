from gymnasium.envs.registration import register

register(
    id='pond-v0',
    entry_point='pondworld.envs:Pond',
)
