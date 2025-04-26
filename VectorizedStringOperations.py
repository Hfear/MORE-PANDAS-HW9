"""Clean a column of text data using .str.strip(), .str.lower(), .str.replace().
Use regex to extract structured data from strings.
Perform filtering based on string patterns.
Concatenate string columns and format output.
Apply .str.get() and .str.len() to analyze string content."""

import pandas as pd

data = {'words': ['  Cat ', 'Bat! ', 'Bee123', 'Sting#', ' Tree!!', 'Apple.  ']}
df = pd.DataFrame(data)

df['words_clean'] = df['words'].str.strip().str.lower().str.replace(r'[^\w\s]', '', regex=True)
df['first_three'] = df['words_clean'].str.extract(r'^(\w{3})')
df_filtered = df[df['words_clean'].str.startswith('b')]
df['concatenated'] = df['words_clean'] + df['first_three'].fillna('')
df['word_length'] = df['words_clean'].str.len()

print(df)
print("\n filtered:")
print(df_filtered[['words_clean']])
