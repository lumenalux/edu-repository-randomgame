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

"""Module of coin game"""

from random import randint as get_tossing_case


def _coin_toss() -> str:
    """This function represents coin game

    :return: Result of tossing coin
    """

    # Since a coin falls on an edge in two of 12,000 cases
    coin_toss_cases: dict[str, range] = {
        '⊚ head': range(1, 6000),  # In 5999 out of 12000 cases
        '⎉ tail': range(6000, 11999),  # In 5999 out of 12000 cases
        '⊘ edge': range(11999, 12001),  # In 2 out of 12000 cases
    }

    tossing_value: float = get_tossing_case(1, 12000)
    for tossing_result, case_range in coin_toss_cases.items():
        if tossing_value in case_range:
            return tossing_result


def coin() -> None:
    """The main function of game. Needed to restart the game
    :rtype: object
    """

    keep_playing: bool = True
    while keep_playing:
        print(_coin_toss())
        keep_playing = input('Do you want to continue tossing? [y/N]: ').strip().lower() == 'y'


if __name__ == '__main__':
    coin()
