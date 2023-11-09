# Markdown vs. Jupyter Notebooks, or: a wider exploration of when to use which filetype

In this piece, I want to explore when to use which file type - what can be used when? To introduce why I ask this question (and then try to answer it), I'll do a quick recap of what this project is and how I got here:

1. I listened to DnD podcasts frequently
2. I made the observation that the people interviewed often describe motives for their behaviour.
3. I thought: that's cool.
4. I thought: maybe these motives can be collected and analysed somehow.
5. I also wanted to learn how to webscrape and do text analysis.
6. My partner challenged me to add a few steps, being:
7. Install Linux on a Raspberry Pi
8. Learn how to SSH into said Pi
9. Work from there
10. I created a few directories and files on the Pi
11. And then proceeded to put everything on Github, so I'd also learn how to use Git/gh
12. I then forgot all about this project.

UNTIL NOW.
<br> And to continue this project, I'll ask these questions:
- What are the differences between, say, Markdown and Jupyter Notebooks?
- When is it better to use A, when is it better to use B?
- Are there other filetypes or languages or whatever that I should explore? (this is a question I'll push to the back, because I think my scope is wide enough as it is).


## What is Markdown?

[Markdown](https://www.markdownguide.org) is a markup language. It offers some simple formatting options to make your texts easier to read. It is NOT html, nor does it pretend to be. For anything that Markdown cannot do, you can use HTML. Markdown files are stored in a plaintext file with an .md or .markdown extension. It can always be opened and read as a plain text file. It can then be converted into HTML or a print-ready document through a Markdown application that can process your md file. 

### How does Github publish a markdown file?
In this case, it sounds as though Github supports conversion of MD to HTML on their website, but I don't know how that happens exactly. However, github does provide the options to show _Preview_, _Code_ and _Blame_. Preview shows the formatted md file, while Code shows the underlying code. That's great for me, because now I can find out how to do extra things in MD. For example:

```python

#I can make a code box.

r = str("an example of a code box")
print(r)
```

## What is Jupyter Notebooks?

Then there's Jupyter Notebooks. JN _uses_ Markdown to format your texts, but is a [simplified notebook authoring app for interactive computing](https://jupyter-notebook.readthedocs.io/en/stable/). Not only can it provide you with codeblocks, but as a reader you can actually run the codes in the codeblocks, so you can test the code yourself and see the results. This is great for generating graphs while also explaining _how_ these graphs were made.


## A very quick and dirty conclusion
While using Jupyter Notebooks is very interesting, I do believe that it is unnecessary at this point in time. An MD file will do for the requests script. Once we get to the data-analysis and graph-making part however, I'll absolutely consider using .ipynb.


See ya.








