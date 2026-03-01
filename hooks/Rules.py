from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from ..Helpers import is_option_enabled, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def SurvReq(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    surv_in_pool = get_option_value(multiworld, player, "surv_in_pool")
    surv_required = get_option_value(multiworld, player, "surv_required")
    return "|@Victory Token:" + str(min(surv_in_pool, surv_required)) + "|"