# Productivity tools

:::{objectives}
- Know about tools that can help you **spot code problems** and help you following
  a **consistent code style** without you having to do it manually.
- Get an overview of **AI-based tools** and how they can help you
  writing code.
:::

:::{instructor-note}
- Demo/discussion: 20 min
:::


## Linters and formatters

**Linter**: Tool that analyzes source code to detect potential errors, unused
imports, unused variables, code style violations, and to improve readability.
- Popular linters:
  - [Autoflake](https://pypi.org/project/autoflake/)
  - [Flake8](https://flake8.pycqa.org/)
  - [Pyflakes](https://pypi.org/project/pyflakes/)
  - [Pycodestyle](https://pycodestyle.pycqa.org/)
  - [Pylint](https://pylint.readthedocs.io/)
  - [Ruff](https://docs.astral.sh/ruff/)

**Formatter**: Tool that automatically formats your code to a consistent style,
for instance following [PEP 8](https://peps.python.org/pep-0008/).

- Popular formatters:
  - [Black](https://black.readthedocs.io/)
  - [YAPF](https://github.com/google/yapf)
  - [Ruff](https://docs.astral.sh/ruff/)

In this course we will focus on [Ruff](https://docs.astral.sh/ruff/) since it
can do **both checking and formatting** and you don't have to switch between
multiple tools.

:::{discussion} Linters and formatters can be configured to your liking
These tools typically have good defaults. But if you don't like the defaults,
you can configure what they should ignore or how they should format or not format.
:::


## Examples

This code example (which we possibly recognize from the previous section about
{ref}`profiling`)
has few problems (highlighted):
```{code-block} python
---
emphasize-lines: 2, 7, 10
---
import re
import requests


def count_unique_words(file_path: str) -> int:
    unique_words = set()
    forgotten_variable = 13
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            words = re.findall(r"\b\w+\b", line.lower()))
            for word in words:
                unique_words.add(word)
    return len(unique_words)
```

Please try whether you can locate these problems using Ruff:
```console
$ ruff check
```

Next, let us try to auto-format a code example which is badly formatted and also difficult
to read:
:::::{tabs}
  ::::{tab} Badly formatted
  ```python
  import re
  def  count_unique_words (file_path : str)->int:
    unique_words=set()
    with open(file_path,"r",encoding="utf-8") as file:
      for line in file:
        words=re.findall(r"\b\w+\b",line.lower())
        for word in words:
          unique_words.add(word)
    return len(   unique_words   )
  ```
  ::::

  ::::{tab} Auto-formatted
  ```python
  import re
  
  
  def count_unique_words(file_path: str) -> int:
      unique_words = set()
      with open(file_path, "r", encoding="utf-8") as file:
          for line in file:
              words = re.findall(r"\b\w+\b", line.lower())
              for word in words:
                  unique_words.add(word)
      return len(unique_words)
  ```

  This was done using:
  ```console
  $ ruff format
  ```
  ::::
:::::


## Type checking

A (static) type checker is a tool that checks whether the types of variables in your
code match the types that you have specified.
- Tools:
  - [Mypy](https://mypy.readthedocs.io/)
  - [Pyright](https://github.com/microsoft/pyright) (Microsoft)
  - [Pyre](https://pyre-check.org/) (Meta)


## Integration with editors

Many/most of the above tools can be integrated with your editor.  For instance,
you can configure your editor to automatically format your code when you save
the file. However, this only makes sense when all team members agree to follow
the same style, otherwise saving and possibly committing changes to version
control will show up changes to code written by others which you possibly
didn't intend to make.


## Integration with Jupyter notebooks

It is possible to automatically format your code in Jupyter notebooks!
For this to work you need
the following three dependencies installed:
- `jupyterlab-code-formatter`
- `black`
- `isort`

More information and a screen-cast of how this works can be found at
<https://jupyterlab-code-formatter.readthedocs.io/>.


## Integration with version control

If you use version control and like to have your code checked or formatted
**before you commit the change**, you can use tools like [pre-commit](https://pre-commit.com/).


## AI-assisted coding

We can use AI as an assistant/apprentice:
- Code completion
- Write a test based on an implementation
- Write an implementation based on a test

Or we can use AI as a mentor:
- Explain a concept
- Improve code
- Show a different (possibly better) way of implementing the same thing


:::{figure} productivity/chatgpt.png
:alt: Screenshot of ChatGPT
:width: 100%

Example for using a chat-based AI tool.
:::

:::{figure} productivity/code-completion.gif
:alt: Screen-cast of working with GitHub Copilot
:width: 100%

Example for using AI to complete code in an editor.
:::

:::{admonition} AI tools open up a box of questions
- Legal
- Ethical
- Privacy
- Lock-in/ monopolies
- Lack of diversity
- Will we still need to learn programming?
- How will it affect learning and teaching programming?
:::
