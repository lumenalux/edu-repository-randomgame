# randgame ![](https://img.shields.io/badge/python-%3E%3D3.9-blue?style=for-the-badge&logo=python)
Mini project. Made for practice in the design of the git repository. 
This is a program that runs from the console. 
You can choose 3 games in it. 
Namely coin toss, dice toss and russian roulette.
## Installation
Open the directory where you want to put the project. Open a terminal on it
and put the command below:
```bash
git clone https://github.com/lumenalux/edu-repository-randomgame
```
## Usage
To use the program, open the project directory, then open
terminal and run ```main.py``` like this:
```bash
python main.py coin
```
The program supports 3 commands: 
```coin```, ```dice```, ```russian_roulette``` 
each of which launches the corresponding game.

Two games run without parameters:
```bash
python main.py coin

python main.py dice
```

Russian roulette can be also run without parameters:
```bash
python main.py russian_roulette
```
But you can also start with a parameter that indicates
the number of bullets in the revolver:
```bash
python main.py russian_roulette --param 3
```
>In this case, Russian roulette was launched 
> with __*three*__ bullets in the store instead of __*one*__

>__Note__: _The number of bullets can be between **one** and **six**_

## Licence
Licensed under the 
[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).