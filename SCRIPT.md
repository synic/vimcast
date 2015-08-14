VimCast Screencast Script
=========================

Introduction
------------

The goal of this video is not to teach anyone how to use VIM, but rather,
demonstrate to programmers why VIM might be a better choice than some of your
other plaintext programming editors, and even IDEs.

Most programmers have heard of VIM.  They've probably even heard the phrase
"best programming editor evar" in one fo the usual editor flamewars.  A good
portion of these programmers might even download VIM and give it a try.

The issue at this point is that, VIM is so different and foreign compared to
other editors, that it's hard to get past even the splash screen, and even
then, the benefits to the editor aren't glaringly obvious.  In fact, the
interface is so unintuitive that it seems very primitive and old.  You may
wonder to yourself, *WHY* would I want to use some old ass command line editor
that doesn't even have a proper gui, when I can just use pretty sublime or
Eclipse or something.

**[SHOW SPLASH SCREEN WITH DEFAULT THEME AND NO PLUGINS]**

I completely admit, the default interface of VIM is pretty scary.  It turns a
lot of people away, and that's without the fact that the learning curve can be
somewhat high.  At initial glance, you may be wondering where even basic items
that you take for granted in other editors are, like tabs, or search and
replace, or even an "open file" dialog.

I can tell you at this juncture, there's no reason to get discouraged.  VIM
*DOES* indeed support 99% of the features you want, either out of the box or
with some configuring.

But, that still doesn't answer why you'd want to use this old ass CLI editor
when there are newer, prettier, more user friendly options available.

The first reason is this:  VIM is an outside the box editor.  The way you
use it is completely different from other editors.  The result is a workflow
that ends up being much faster, easier, and much more efficient.

VIM is designed to be used ENTIRELY from the keyboard, and most functions can
even be accessed without leaving your home row.  Basically anything you need to
do while coding can be done by using your keyboard.  This doesn't mean VIM
doesn't support the mouse, because it does, it's often just faster to do it
via the keyboard.  If your hands aren't leaving your keyboard every 5 seconds
to move your mouse, *you are going to be faster*.

The second reason is: VIM is very extensible.  Much of the best functionality
is provided via plugins, and plugins can be written in several different
languages (vimscript, python, perl, ruby, etc).

**[SHOW VUNDLE USAGE]**

1.  Open .vimrc and show the Vundle packages, describe some of the more
    important plugins.
2.  Show one or two of the projects on github
3.  Run `:PluginUpdate`


Command Mode
------------

The default mode VIM drops you in is called "command mode".  This is easily
where most of the confusion comes from when learning VIM.  Instead of
immediately being able type your code directly in the editor window, you are
dropped into command mode, where almost every keystroke or combination of
keystrokes equals a command.  Trying to type code in this mode will probably
not do anything close to what you want.

You may be thinking to yourself, why is command mode the default - it really
doesn't make any sense, but if you think about it, how much time do you
spend actually straight up writing out code vs time spent navigating and
editing code that already exists?  Unless you're some sort of magical wizard,
I'd bet that you spend more time doing the latter.

Another benefit to the idea of a "command" mode, where all keystrokes are
possible commands, is that most commands don't require crazy key combinations
(like in emacs).  Often commands are just one or two letters, near the home
row.  Nearly all the commands in command mode accept different kinds of
"modifiers" that extend the command's functionality - for instance, many
commands accept a number before the actual command, that signifies how many
times to perform the command.  As an example, the command `dd` will remove the
current line from the file.  If you type `5dd`, it will remove the current
line, and the 4 lines after it.  Many commands can also be combined.

**[DEMO VARIOUS COMMANDS IN COMMAND MODE]**

1.  Demo moving around the file, including going to specific line numbers,
moving to the beginning of the line, end of the line, moving over words,
searching.
2.  Demo easymotion.
3.  Demo `diw`, `ciw`, `C`, `D`, `dd`, `yy`, `p`, `A`, `o`, and `O`, and demo
them again with repeat modifiers.
4.  Fully demo `dt` and `ct`.  Demo surround.vim
5.  Demo `xp`.
6.  Demo `r`.
7.  Demo splitting windows.  Demo switching between windows.  Demo resizing
the windows using your mouse.
8.  Demo making marks.

Insert Mode
-----------

**DEMO**: Briefly demo insert mode.  Demo omnicomplete, and local completion.

Visual Mode
-----------

**DEMO**: Show how visual mode can be better than selecting with a
mouse, via `v`, `CTRL+v`, and `V`.  Show how you can copy various blocks
of text into different clipboards, and paste them out.


It's a Flippin` console client!
-------------------------------

Ok, I know you're thinking a) that there's just no possible way that a console
editor can be better at managing multiple files or a even a project with
hundreds of files, or many projects with hundreds of files and that b) there's
no possible way that a console editor can be even 2% as pretty as ATOM or
whatever.

VIM has many different ways of working with multiple files.

**[DEMO FILE MANAGMENT]**

1.  Demo NERDTree
2.  Demo BufExplorer
3.  Demo splitting windows
4.  Demo `CTRL+P`
5.  Talk about how tabs work in vim

**[SHOW THAT VIM DOESN'T HAVE TO BE THE WORST LOOKING EDITOR]**

1.  Demo solarized
2.  Demo various other plugins
3.  Possibly demo various other screenshots


I'm still not sold!  What else is cool about VIM?
-------------------------------------------------

**[DEMO]**

1.  Demo modelines.
2.  Demo advanced search and replace.
3.  Demo undoing, type some stuff, make some commands, undo once, make some
more commands, open `:Gundo`, talk about `:earlier 5m`
4.  Demo the help system.
5.  Demo `:Gist`, and `:Gblame`
