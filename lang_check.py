from dsl.semantic import *
from dsl.parser import *
from dsl.hands import *
from model.match import *
from model.tournament import *
import os
import settings
import logging
import pandas as pd

logging.basicConfig(level=logging.FATAL)
logging.info("Poker Analyser v{}".format(os.getenv("VERSION")))
logging.debug("Hand history at {}".format(os.getenv("HAND_HISTORY_PATH")))


tournaments = read_all_tournaments()

pre_flop_actions = []
flop_actions = []
turn_actions = []
river_actions = []

# todo -> parallelized map reduce

for tournament_log in tournaments:  # enumerable
    try:
        print("starting tournament")
        tournament = interpret(tournament_log)
        pre_flop_actions = pre_flop_actions + tournament.pre_flop_actions
        flop_actions = flop_actions + tournament.flop_actions
        turn_actions = turn_actions + tournament.turn_actions
        river_actions = river_actions + tournament.river_actions
        break
    except Exception as ex:
        print("something bad happened here")
        print(ex)
    finally:
        print("finished tournament")

print("\n\n\n@@@@@@@@@")
print(pd.DataFrame(pre_flop_actions).fillna(0))
print("\n\n\n@@@@@@@@@")
print(pd.DataFrame(flop_actions).fillna(0))
print("\n\n\n@@@@@@@@@")
print(pd.DataFrame(turn_actions).fillna(0))
print("\n\n\n@@@@@@@@@")
print(pd.DataFrame(river_actions).fillna(0))