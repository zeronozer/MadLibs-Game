# MadLibs Game

This is a simple command line MadLibs game written in Python. Users provide words to fill in the blanks in randomly chosen story templates to generate fun stories.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Testing](#testing) 
- [Contributing](#contributing)

## About 

This project is based on a MadLibs tutorial, with modifications and improvements made to demonstrate Python best practices and readable code.

Key features:

- Selects a random story template 
- Parses the story to find words to replace
- Prompts user to input replacement words
- Populates the story template and prints the final result

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repo
   ```sh
   git clone https://codeberg.org/zennon/MadLibs-Game.git
   ```
2. Navigate to project directory

### Running the Game

```py
python story.py
```

## Usage

- Run the game using `python python.py`
- Provide words when prompted to fill in the story blanks
- Laugh at the silly stories generated!

## Code Overview

- `MadLibs` - Class representing the game 
- `__init__()` - Initializes game objects
- `pick_random_story()` - Selects random story file
- `parse()` - Parses story file content  
- `find_words()` - Finds placeholder words to replace
- `ask()` - Prompts user for word inputs
- `generate()` - Populates and prints final story

## Testing

TODO: Add unit tests to validate game logic and input handling.

### Credits

- Inspired by a tutorial by Tech With Tim

The original tutorial this code is based on is by "Tech With Tim" and can be found here: [link](https://youtu.be/21FnnGKSRZo?t=1428)

## Contributing

Contributions are welcome! Please open an issue or PR for any enhancements.

Some ideas for improvements:

- Additional stories
- Option to play again
- User input validation
- Unit tests