"""
15. Glossary 2: clean up the code from Exercise 14 by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""
programming_word = {
    'dictionary': 'ovidhan',
    'condition': 'shorto',
    'set': 'sajano',
    'tuple': 'matra',
    'loop': 'repeat'
}
for key, value in programming_word.items():
    print(key, ":", value)

programming_word['string'] = 'character'
programming_word['integer'] = 'number'
programming_word['float'] = 'doshomik'
programming_word['variable'] = 'cholok'
programming_word['data'] = 'upatto'

print("\nAfter insert: \n")
for key, value in programming_word.items():
    print(key, ":", value)
