"""
Player Actions [DiamondQuest]

Shorthand representations of valid player actions.

Author(s): Harley Davis, Elizabeth Larson, Jason C. McDonald
"""

# LICENSE (BSD-3-Clause)
# Copyright (c) 2020 MousePaw Media.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#
# CONTRIBUTING
# See https://www.mousepawmedia.com/developers for information
# on how to contribute to our projects.

from enum import Enum

from diamondquest.common import Direction

class ToolType(Enum):
    NONE = 0
    PICKAXE = 1
    DRILL = 2
    TNT = 3
    COFFEE = 0xC0FFEE

class PlayerAction:
    IDLE_STAND = (Direction.BELOW, ToolType.NONE, Direction.HERE)
    IDLE_CLIMB = (Direction.BELOW, ToolType.NONE, Direction.HERE)
    IDLE_COFFEE = (Direction.BELOW, ToolType.COFFEE, Direction.HERE)
    IDLE_LEFT = (Direction.LEFT, ToolType.NONE, Direction.HERE)
    IDLE_ABOVE = (Direction.ABOVE, ToolType.NONE, Direction.HERE)
    IDLE_RIGHT = (Direction.RIGHT, ToolType.NONE, Direction.HERE)

    WALK_LEFT = (Direction.BELOW, ToolType.NONE, Direction.LEFT)
    WALK_RIGHT = (Direction.BELOW, ToolType.NONE, Direction.RIGHT)

    COFFEE_LEFT = (Direction.BELOW, ToolType.COFFEE, Direction.LEFT)
    COFFEE_RIGHT = (Direction.BELOW, ToolType.COFFEE, Direction.RIGHT)

    CLIMB_UP = (Direction.HERE, ToolType.NONE, Direction.ABOVE)
    CLIMB_DOWN = (Direction.HERE, ToolType.NONE, Direction.BELOW)
    CLIMB_LEFT = (Direction.HERE, ToolType.NONE, Direction.LEFT)
    CLIMB_RIGHT = (Direction.HERE, ToolType.NONE, Direction.RIGHT)

    PICKAXE_ABOVE_LEFT = (Direction.BELOW, ToolType.PICKAXE, Direction.ABOVE_LEFT)
    PICKAXE_ABOVE = (Direction.BELOW, ToolType.PICKAXE, Direction.ABOVE)
    PICKAXE_ABOVE_RIGHT = (Direction.BELOW, ToolType.PICKAXE, Direction.ABOVE_RIGHT)
    PICKAXE_LEFT = (Direction.BELOW, ToolType.PICKAXE, Direction.LEFT)
    PICKAXE_RIGHT = (Direction.BELOW, ToolType.PICKAXE, Direction.RIGHT)
    PICKAXE_BELOW_LEFT = (Direction.BELOW, ToolType.PICKAXE, Direction.BELOW_LEFT)
    PICKAXE_BELOW_RIGHT = (Direction.BELOW, ToolType.PICKAXE, Direction.BELOW_RIGHT)

    DRILL_UP = (Direction.BELOW, ToolType.DRILL, Direction.ABOVE)
    DRILL_DOWN = (Direction.BELOW, ToolType.DRILL, Direction.BELOW)
    DRILL_LEFT = (Direction.BELOW, ToolType.DRILL, Direction.LEFT)
    DRILL_RIGHT = (Direction.BELOW, ToolType.DRILL, Direction.RIGHT)

    IDLE_TNT = (Direction.BELOW, ToolType.TNT, Direction.HERE)

    TNT_LEFT = (Direction.BELOW, ToolType.TNT, Direction.LEFT)
    TNT_RIGHT = (Direction.BELOW, ToolType.TNT, Direction.RIGHT)

    ABOVE_PICKAXE_LEFT = (Direction.ABOVE, ToolType.PICKAXE, Direction.LEFT)
    ABOVE_PICKAXE_BELOW_LEFT = (Direction.ABOVE, ToolType.PICKAXE, Direction.BELOW_LEFT)
    ABOVE_PICKAXE_BELOW = (Direction.ABOVE, ToolType.PICKAXE, Direction.BELOW)
    ABOVE_PICKAXE_BELOW_RIGHT = (Direction.ABOVE, ToolType.PICKAXE, Direction.BELOW_RIGHT)
    ABOVE_PICKAXE_RIGHT = (Direction.ABOVE, ToolType.PICKAXE, Direction.RIGHT)

    LEFT_PICKAXE_ABOVE = (Direction.LEFT, ToolType.PICKAXE, Direction.ABOVE)
    LEFT_PICKAXE_ABOVE_RIGHT = (Direction.LEFT, ToolType.PICKAXE, Direction.ABOVE_RIGHT)
    LEFT_PICKAXE_RIGHT = (Direction.LEFT, ToolType.PICKAXE, Direction.RIGHT)
    LEFT_PICKAXE_BELOW = (Direction.LEFT, ToolType.PICKAXE, Direction.BELOW)
    LEFT_PICKAXE_BELOW_RIGHT = (Direction.LEFT, ToolType.PICKAXE, Direction.BELOW_RIGHT)

    RIGHT_PICKAXE_ABOVE_LEFT = (Direction.RIGHT, ToolType.PICKAXE, Direction.ABOVE_LEFT)
    RIGHT_PICKAXE_ABOVE = (Direction.RIGHT, ToolType.PICKAXE, Direction.ABOVE)
    RIGHT_PICKAXE_LEFT = (Direction.RIGHT, ToolType.PICKAXE, Direction.LEFT)
    RIGHT_PICKAXE_BELOW_LEFT = (Direction.RIGHT, ToolType.PICKAXE, Direction.BELOW_LEFT)
    RIGHT_PICKAXE_BELOW = (Direction.RIGHT, ToolType.PICKAXE, Direction.BELOW)