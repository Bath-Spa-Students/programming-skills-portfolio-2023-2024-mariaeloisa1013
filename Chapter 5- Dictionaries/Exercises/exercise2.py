#Dictionary of propgramming words
print("\n\tGlossary\n")
glossary = {"integer": "a whole number ",
    "float": "numbers with decimal",
    "string": "text data",
    "variables": "a value",
    "statement": "a line of code"}

#print each word-meaning pair
word = "integer"
print("\n" + word.title() + ":" + glossary[word])
word = "float"
print("\n" + word.title() + ":" + glossary[word])
word = "string"
print("\n" + word.title() + ":" + glossary[word])
word = "variables"
print("\n" + word.title() + ":" + glossary[word])
word = "statement"
print("\n" + word.title() + ":" + glossary[word])