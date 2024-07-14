# %%
with open("data/GPM.md", "r", encoding="utf-8") as file:
    data = file.read()

questions = data.split("###")
questions = filter(lambda x: x != "", questions)
questions = list(map(lambda x: x.split("\n\n"), questions))

pairs = {}

for q in questions:
    pairs[q[0]] = q[1]

len(pairs)
# %%

import random
from IPython.display import display, Markdown

# %% IPython compatible execution

key = random.choice(list(pairs.keys()))
value = pairs[key]
pairs.pop(key)

display(Markdown(key))
input()
display(Markdown(value))