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

"""The main program file from which the games are launched.

This file is meant to be run from the console with parameters. In total, you can
run three games. Namely coin toss, dice toss and Russian roulette

Example usage:
python main.py coin  # ⎉ tail
python main.py dice  # ⚁ two
python main.py russian_roulette  # Click...
python main.py russian_roulette --param 3  # BOOM!
"""

from argparse import ArgumentParser, Namespace
from games import dice, coin, russian_roulette


def get_arguments() -> Namespace:
    """Initialisation of console arguments

    :return: Namespace of arguments that were passed through the console
    """

    parser = ArgumentParser()
    parser.add_argument(
        'game',
        choices=['coin', 'dice', 'russian_roulette'],
        help="choose the game would you like"
    )

    parser.add_argument(
        '--param',
        type=int,
        required=False,
        help='Parameter for game. For game of russian roulette, this will be the number of bullets'
    )

    return parser.parse_args()


def main() -> None:
    """Launching selected game based on parameters from console"""

    game = {
        'coin': coin,
        'dice': dice,
        'russian_roulette': russian_roulette,
    }

    args = get_arguments()

    if args.param is None:
        return game[args.game]()

    return game[args.game](args.param)


if __name__ == '__main__':
    main()
