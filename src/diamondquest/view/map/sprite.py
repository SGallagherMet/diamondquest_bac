"""
Spr teView [DiamondQuest]

Renders the player sprite on the screen.

Author(s): Elizabeth Larson, Jason C. McDonald
"""

# LICENSE (BSD-3-Clause)
# Copyright (c) 2020 MousePaw Media.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the foillowing disclaimer.
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

import pygame

from diamondquest.common.constants import TEXTURE_RES, STEP_MAX
from diamondquest.common import loader, Direction
from diamondquest.model import PlayerAction, ToolType
from diamondquest.common import Resolution
from diamondquest.common import loader
from diamondquest.view.window import Window

class SpriteTexture:
    texture_locations = {}
        IDLE_STAND: ((0, 0), (0, 1)),
        IDLE_CLIMB: ((3, 0), (3, 0)),
        #IDLE_LEFT: ((), ()),
        #IDLE_ABOVE: ((), ()),
        #IDLE_RIGHT: ((), ()),
        #WALK_LEFT: ((1, 0), (1, 1)),  # flip
        WALK_RIGHT: ((1, 0), (1, 1)),
        CLIMB_UP: ((3, 0), (3, 1)),
        CLIMB_DOWN: ((3, 0), (3, 1)),
        CLIMB_LEFT: ((3, 0), (3, 1)),
        CLIMB_RIGHT: ((3, 0), (3, 1)),
        #PICKAXE_ABOVE_LEFT: ((), ()),
        #PICKAXE_ABOVE: ((), ()),
        #PICKAXE_ABOVE_RIGHT: ((), ()),
        #PICKAXE_LEFT: ((4, 0), (4, 1)),  # flip
        PICKAXE_RIGHT: ((4, 0), (4, 1)),
        # PICKAXE_BELOW_LEFT: ((), ()),
        # PICKAXE_BELOW_RIGHT: ((), ()),
        # DRILL_UP: ((), ()),
        DRILL_DOWN: ((6, 0), (6, 1)),
        DRILL_LEFT: ((6, 4), (6, 5)),
        DRILL_RIGHT: ((6, 2), (6, 3)),
        #IDLE_TNT: ((), ()),
        #TNT_LEFT: ((7, 0), (7, 1)), # flip
        TNT_RIGHT: ((7, 0), (7, 1)),
        #ABOVE_PICKAXE_LEFT: ((), ()),  # TODO: Fill out as sprites are added
        #ABOVE_PICKAXE_BELOW_LEFT: ((), ()),
        #ABOVE_PICKAXE_BELOW: ((), ()),
        #ABOVE_PICKAXE_BELOW_RIGHT: ((), ()),
        #ABOVE_PICKAXE_RIGHT: ((), ()),
        #LEFT_PICKAXE_ABOVE: ((), ()),
        #LEFT_PICKAXE_ABOVE_RIGHT: ((), ()),
        #LEFT_PICKAXE_RIGHT: ((), ()),
        #LEFT_PICKAXE_BELOW: ((), ()),
        #LEFT_PICKAXE_BELOW_RIGHT: ((), ()),
        #RIGHT_PICKAXE_ABOVE_LEFT: ((), ()),
        #RIGHT_PICKAXE_ABOVE: ((), ()),
        #RIGHT_PICKAXE_LEFT: ((), ()),
        #RIGHT_PICKAXE_BELOW_LEFT: ((), ()),
        #RIGHT_PICKAXE_BELOW: ((), ())
        # (TOOL, TOOL, DIRECTION, DIRECTION"  # Action, Tool, Anchor, Work Direction

    cache = dict()

    @classmethod
    def texture_location(cls, sprite, step=0):
        """Return the texture x, y, h, w for a given sprite.
        sprite - the player action
        step - which animation step to show (presently 0 or 1)
        """
        if step > STEP_MAX:
            raise ValueError(f"Sprite animations only support up to step {STEP_MAX}")
        reg = cls.texture_locations[sprite][step]
        x, y = (n * TEXTURE_RES for n in reg)
        return (x, y, TEXTURE_RES, TEXTURE_RES)

    @classmethod
    def load_texture(cls, texture):
        """Load a sprite
        Utilizes map blocks's height and width (16x16)"""
        try:
            return cls.cache[texture]
        except KeyError:
            spritesheet = loader.load_texture("sprite")

            miner = pygame.Surface(
                (TEXTURE_RES, TEXTURE_RES), pygame.SRCALPHA
            )
            miner.blit(
                spritesheet,
                (0, 0),
                SpriteTexture.texture_location(texture),
            )

            bh = Resolution.get_primary().block_height
            miner = pygame.transform.scale(miner, (bh, bh))

            cls.cache[(texture, variant)] = miner
            return miner