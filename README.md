# AutoANKI

**Still WIP**

AutoANKI is a tool designed to help you create and manage flashcards for efficient learning and memorization. Similar to ANKI, this application allows you to generate digital flashcards, organize them into decks, and review them using spaced repetition techniques. 

It generates questions automatically from your Markdown lecture notes. Right now, the markdown file must be structured accordingly to be understandable to the AutoANKI script

\newpage

# Markdown Converter
___

Workhorse architecture for this project is Markdown rendering. Special elements are rendered via images. For example latex, graphs end so on. 

Features:

- Not Markdown feature blocks: 
    - Latex: Matplotlib (or IPython if possible)
    - Plots: Sympy + Numpy + Matplotlib
    - Charts: idk
    - Graph: 
    - Latex: $\frac{\alpha}{\beta}$

[[graph: x**2]]

\newpage

# Planned Features

- **Create Flashcards**: Easily create flashcards with question & answer.
- **Organize into Decks**: Group related flashcards into decks for focused study sessions. Ask related questions via network based topic grouping. Ask related questions from similar topics
- **Spaced Repetition**: Use the built-in spaced repetition algorithm to optimize your study schedule.
- **Import/Export**: Import flashcards from CSV files and export your decks for backup or sharing.
- **Progress Tracking**: Monitor your learning progress with detailed statistics.
- **LLM**: conveniance is key, a common problem with regular ANKI is, that you have to find matching ANKI sets or create your own. That may lead to high quality sets, but sets a very high bar for starting to learn with ANKI. Why not generate questions automatically by an LLM based on the content of your lecture script with a human (you) in the loop? Generate questions about the content of your lecture notes and keep only the ones you like. Then answer and store the questions for repetition learning afterwards.

\newpage

# License

This project is licensed under the MIT License. 

Happy Studying! 📚