
"""
MadLibs Game: 

A fun word game where players provide words to fill in the blanks in a story.

This code showcases my skills and knowledge in Python programming, following best practices and readability.

It is based on one of the projects presented in a tutorial video: https://youtu.be/21FnnGKSRZo

# ! I have implemented the project with my own modifications and improvements.
"""

import re
import random

class MadLibs:
    """
    A class that represents a Mad Libs game.

    Attributes:
        story_files (list): A list of file names containing stories.
        story_file (str): The randomly chosen story file.
        story (str): The parsed content of the story file.
        words (set): A set of words to be replaced in the story.
        answers (dict): A dictionary to store user's answers for words.

    Methods:
        pick_random_story(): Randomly selects a story file.
        parse(story_file): Parses the content of the story file.
        find_words(story): Finds the words to be replaced in the story.
        ask(): Asks the user to input words for replacement.
        generate(): Generates the final story by replacing the words.
    """

    def __init__(self, story_files):
        """
        Initializes a MadLibs game object.

        Args:
            story_files (list): A list of file names containing stories.
        """
        self.story_files = story_files
        self.story_file = self.pick_random_story() # Select a random story file
        self.story = self.parse(self.story_file) # Parse the story file
        self.words = self.find_words(self.story) # Find all the placeholder words in the story
        self.answers = {} # Dictionary to store user's answers

    def pick_random_story(self):
        """
        Randomly selects a story file from the provided list.

        Returns:
            str: The name of the randomly chosen story file.
        """
        return random.choice(self.story_files)

    def parse(self, story_file):
        """
        Parses the content of the story file.

        Args:
            story_file (str): The name of the story file.

        Returns:
            str: The parsed content of the story file.
        """

        with open(story_file) as f:
            return f.read()

    def find_words(self, story):
        """
        Finds the words to be replaced in the story.

        Args:
            story (str): The story content.

        Returns:
            set: A set of words to be replaced in the story.
        """
        pattern = re.compile(r"<(.*?)>")
        words = pattern.findall(story)
        return set(words)

    def ask(self):
        """
        Asks the user to input words for replacement.
        """
        for word in self.words:
            if word not in self.answers:
                answer = input("Enter a word for {}: ".format(word))
                self.answers[word] = answer

    def generate(self):
        """
        Generates the final story by replacing the words and prints it.
        """
        for word, answer in self.answers.items():
            pattern = re.compile(r'<{}>'.format(word))
            self.story = pattern.sub(answer, self.story)
        print(self.story)


if __name__ == "__main__":
    story_files = ["story1.txt", "story2.txt", "story3.txt"]
    game = MadLibs(story_files)
    game.ask() # Ask user for inputs
    game.generate() # Generate and print the final story