# chaos-game
## install base package using:

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps chaos_game_base
```

## usage:

```
from chaos_game_base import chaos
game = chaos.DefaultFernChaosGame()
game_out = game.play(60000)
game_out.color('red')
game_out.plot()
```