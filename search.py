import re

class Search:
    def __init__(self, filename='default.txt'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            raise Exception(f"File '{self.filename}' not found.")

    def clean(self):
        # Removes special characters from each line using regex
        self.lines = [re.sub(r'[^A-Za-z0-9\s]', '', line) for line in self.lines]

    def getLines(self, word):
        # Collect lines containing the word
        result = [word]
        for index, line in enumerate(self.lines):
            if word in line:
                result.append((index + 1, line))
        return result