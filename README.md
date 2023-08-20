# Last Pencil Game 

Python-based game where players compete against a bot using strategic decisions.

## Contents
- [Description](#description)
- [Rules](#rules)
- [Bot Strategy](#bot-strategy)
- [Setup & Execution](#setup--execution)

## Description
**Last Pencil** is a simulation game designed to test strategic decision-making. The user plays against a bot, aiming to understand and counteract the bot's pre-defined strategy.

## Rules
1. Specify the initial number of pencils.
2. Players take turns to pick 1, 2, or 3 pencils.
3. The player forced to pick the last pencil loses.

## Bot Strategy
The bot follows a specific strategy:
- If in a winning position, it makes choices to maintain its advantage.
- In a losing position, the bot selects randomly between 1 and 3.

## Setup & Execution
1. Ensure you have Python 3 installed. If not, install it using:
<pre>
  sudo apt-get install python3
</pre>
2. Clone this repository:
<pre>
  git clone https://github.com/micredis/hs-last-pencil.git
</pre>
3. Run the game:
<pre>
  python3 hs-last-pencil/task/game.py
</pre>
Follow the on-screen prompts to play.
