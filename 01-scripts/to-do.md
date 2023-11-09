# To Do-list for the requests file

I wrote a script to request transcripts from Darknet Diaries!
<br>However, I think it could be improved.

## What improvements can be made?

1. Choose an appropriate filetype
2. Make the function to request files more elegant
3. Remove unnecessary fluff
4. Move on to the next step!


## 1. Choosing an appropriate filetype

The filetype could be switched from a .py to a more readable filetype (like an md or jupyter notebook). However, I am unsure what the benefits and other issues with this are. Let's take a step back and discern: what is the purpose of this file for me? And what do I intend to learn from it?

The main purpose for me is to a) learn how to do this and b) be able to easily re-do these steps for another project. That means that the text should read as more of a "How To" while executing the steps, rather than a clean .py-file that contains as little info as possible and is easily executable. So it's an example including explanation, or an explanation including an example. Whichever you prefer.

### *To Do*
[] investigate the difference and preference between a MarkDown and a Jupyter Notebook file. 
[] turn the script into an .md file or jupyter notebookfile that includes code blocks


## 2. Make the function to request files more elegant

At this point, the range of transcripts that is pulled from DarkNetDiaries is manually defined to be from a range from [1,134]. This is fine for doing an analysis on a pre-defined set of scripts, but in the future it might be nicer to have it a) find out which file has been added last and b) update up until the last published transcript.
