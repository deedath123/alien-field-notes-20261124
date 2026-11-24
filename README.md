# Alien Field Notes: The Two Day Earth Review

[![Competition](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/deedath123/alien-field-notes-20261124/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/deedath123/alien-field-notes-20261124/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

Entry for the [make.fun bounty](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000): an alien tourist's one-line review of Earth, under 200 characters.

## The line

> Earth, 3/5 stars. Stunning oceans, but the locals stare at glowing rectangles 7 hours a day, ignore the microwave beep, reheat the same meal twice, and call it dinner. Would abduct again.

## What it does

`main.py` (Python 3, standard library only) writes the review line to `/output/entry.txt`. It creates `/output` if needed, asserts the line is 1–200 characters, a single line, and not whitespace-only, and the output is deterministic — byte-identical on every run.

## Run it

```sh
python3 main.py
```

Then read `/output/entry.txt`.
