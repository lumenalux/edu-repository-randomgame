# Copyright © 2021 Martyniuk Stefan. All rights reserved.
# Contacts: stefanmartinuk@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module of dice game"""

from random import randint


def dice_toss() -> str:
    """This function represents dice tossing

    :return: Result of tossing dice
    """

    die_faces: dict[int, str] = {
        1: '⚀ one',
        2: '⚁ two',
        3: '⚂ three',
        4: '⚃ four',
        5: '⚄ five',
        6: '⚅ six',
    }

    return die_faces[randint(1, 6)]


def dice() -> None:
    """The main function of game. Needed to restart the game"""

    keep_playing: bool = True
    while keep_playing:
        print(dice_toss())
        keep_playing = input('Do you want to continue? [y/N]: ').strip().lower() == 'y'


if __name__ == '__main__':
    dice()
