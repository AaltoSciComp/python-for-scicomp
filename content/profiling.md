# Productivity tools and Profiling

## Productivity tools

```{questions}
   - Do you have preferences on the visual aspects of the code
     and how it should look?
   - Do you use any tools that help you create better looking
     code faster?
```

```{objectives}
   - Learn tools that can help you be more productive.
   - Learn how to follow standards that other people have created
     and how to pick your own favorite.
```

> [!IMPORTANT]  
> Left to do: Summarize [Productivity tools lecture](/content/productivity.rst) in 20 minutes.


## Profiling

```{questions}
   - When shall we worry about the performance of our code?
   - How do we find bottlenecks in our code?
   - How do we measure improvements in running time and memory usage?
```

```{objectives}
   - Understand when improving code performance is worth the time and effort.
   - Learn how to use profilers in Python.
   - Use `scalene` to find and optimize bottlenecks in a given code example.
```


> [!IMPORTANT]  
> Left to do:
> Give 20 minutes introduction to profiling:
> - [ ] Discuss when to profile
> - [ ] Discuss breifly manual profiling
> - [ ] Introduce function call profilers
> - [ ] Introduce line profilers
> - [ ] Visualize one code example using `scalane`


## Exercises

:::{exercise} Exercise Profiling-1
Work in progress: we will provide an exercise showing the improvement in
performance when introducing numpy and/or pandas.
:::

::::{exercise} Exercise Profiling-2
In this exercise we will use the `scalene` profiler to find out where most of the time is spent
and most of the memory is used in a given code example.

Please try to go through the exercise in the following steps:
1. Make sure `scalene` is installed in your environment (if you have followed
   this course from the start and installed the recommended software
   environment, then it is).
1. Download Leo Tolstoy's "War and Peace" from the following link (the text is
   provided by [Project Gutenberg](https://www.gutenberg.org/)):
   <https://www.gutenberg.org/cache/epub/2600/pg2600.txt>
   (right-click and "save as" to download the file and **save it as "book.txt"**).
1. **Before** you run the profiler, try to predict in which function the code
   will spend most of the time and in which function it will use most of the
   memory.
1. Run the `scalene` profiler on the following code example and browse the
   generated HTML report to find out where most of the time is spent and where
   most of the memory is used:
   ```console
   $ scalene example.py
   ```
   Alternatively you can do this (and then open the generated file in a browser):
   ```console
   $ scalene example.py --html > profile.html
   ```
   You can find an example of the generated HTML report in the solution below.
1. Does the result match your prediction? Can you explain the results?

```python
"""
The code below reads a text file and counts the number of unique words in it
(case-insensitive).
"""
import re


def count_unique_words1(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    words = re.findall(r"\b\w+\b", text.lower())
    return len(set(words))


def count_unique_words2(file_path: str) -> int:
    unique_words = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            words = re.findall(r"\b\w+\b", line.lower())
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)
    return len(unique_words)


def count_unique_words3(file_path: str) -> int:
    unique_words = set()
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            words = re.findall(r"\b\w+\b", line.lower())
            for word in words:
                unique_words.add(word)
    return len(unique_words)


def main():
    _result = count_unique_words1("book.txt")
    _result = count_unique_words2("book.txt")
    _result = count_unique_words3("book.txt")


if __name__ == "__main__":
    main()
```

:::{solution}
  ```{figure} profiling/exercise2.png
  :alt: Result of the profiling run for the above code example.
  :width: 100%

  Result of the profiling run for the above code example. You can click on the image to make it larger.
  ```

  Results:
  - Most time is spent in the `count_unique_words2` function.
  - Most memory is used in the `count_unique_words1` function.

  Explanation:
  - The `count_unique_words2` function is the slowest because it **uses a list**
    to store unique words and checks if a word is already in the list before
    adding it.
    Checking whether a list contains an element might require traversing the
    whole list, which is an O(n) operation.
  - The `count_unique_words1` and `count_unique_words3` functions are faster
    because they **use a set** to store unique words.
    Checking whether a set contains an element is an O(1) operation.
  - The `count_unique_words1` function uses the most memory because it **creates
    a list of all words** in the text file and then **creates a set** from that
    list.
  - The `count_unique_words3` function uses less memory because it traverses
    the text file line by line instead of reading the whole file into memory.

  What we can learn from this exercise:
  - When processing large files, it can be good to read them line by line
    instead of reading the whole file into memory.
  - It is good to get an overview over standard data structures and their
    advantages and disadvantages (e.g. adding an element to a list is fast but checking whether
    it already contains the element is slow).
  :::
::::
