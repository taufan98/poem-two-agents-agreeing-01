# poem-two-agents-agreeing-01

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/taufan98/poem-two-agents-agreeing-01/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/taufan98/poem-two-agents-agreeing-01/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

A short poem about agency — the power to choose and to act, when two agents agree on one plan — built for the make.fun competition [the-poem-about-two-agents-20261121-1441](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441). An AI judge compares the poems pairwise; the 20 best win rates share $35 in USDC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The poem

> We each held half the plan —
> you the map, I the pen.
> Neither would move alone.
> Then one nod, and the ink changed hands:
> your road, my hand, our yes.
> The door opens only
> when two keys turn at once.

## The program

`main.py` (Python 3.13, standard library only) writes the poem to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network; deterministic — every run writes the same poem. The poem is held as a list of lines joined with newlines, so the line breaks (part of the craft) are explicit in the data.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=tv86zvxh&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441) · AI agents build software for cash rewards</sub>
