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

"""Module of russian roulette game"""

from random import randint, shuffle


def _russian_roulette_game(number_of_bullets: int = 1) -> None:
    """This function represents russian roulette game

    :param number_of_bullets: Number of bullets in revolver
    """

    if not (type(number_of_bullets) == int):
        raise TypeError(f'Number of bullets must be int,'
                        f' got {type(number_of_bullets).__name__} instead')

    if not (1 <= number_of_bullets <= 6):
        raise ValueError(f'The number of bullets must be between 1 and 6,'
                         f' got {number_of_bullets} instead')

    magazine_turnover: int = 0
    bullet_slots: list[bool] = [i < number_of_bullets for i in range(6)]
    shuffle(bullet_slots)

    while number_of_bullets > 0:
        magazine_turnover = (magazine_turnover + randint(0, 36)) % 6  # roll the magazine
        number_of_bullets -= 1 if bullet_slots[magazine_turnover] else 0

        print(
            'BOOM!' if bullet_slots[magazine_turnover] else 'Click...',
            end=' ' if number_of_bullets > 0 else '\n'
        )

        bullet_slots[magazine_turnover] = False

        if number_of_bullets > 0:
            input()


def russian_roulette(number_of_bullets: int = 1) -> None:
    """The main function of game. Needed to restart the game

    :param number_of_bullets: Number of bullets in revolver
    """

    keep_playing: bool = True
    while keep_playing:
        _russian_roulette_game(number_of_bullets)
        keep_playing = input('Play one more? [y/N]: ').strip().lower() == 'y'


if __name__ == '__main__':
    russian_roulette(2)
