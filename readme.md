What's this?
===========
Boo is a reimplementation of a handy tool I saw in one of [Zach Holman](https://github.com/holman)'s [screencasts](http://zachholman.com/screencast/vagranception/). Basically it's a key value store that allows you to save snippets of text that you can later find and copy to your clipboard.

Example
=========
Let's try a simple usage example. I just found a funny picture of a friend and want to keep it stored for use as leverage the next time I need to borrow some money from him. Here's where boo can help me out. I open up a terminal window and type:

    boo funny-picture http://i.imgur.com/AEWxr.jpg

And now it's saved!

So now I need an extra server for a project I'm working on. I'm broke and my friend is reluctant to help me out, so I need some help from my friend boo! All I have to do is open a terminal window and type:

    boo funny-picture

and Boom! The URL is instantly copied to my clipboard, where I can send it in a completely non-threatening email to my friend in order to get my way!

Installation
=============
Fire up your terminal and type:

    git clone git://github.com/stevenleeg/boo.git
    cd boo
    sudo python setup.py install

And that's it! Boo is now at your service!

Commands
=========
### Create
    
    boo test hello world

Creates a new key, `test`, and sets it's value to `hello world`

### Get

    boo test

Gets the value of key `test` and copys it to your clipboard

### Delete

    boo rm test

Removes the key `test`

### Move (to be implemented)

    boo mv test hello

Renames the key `test` to `hello`

### All

    boo all

Lists all of the keys stored in your `~/.boom` file.

Known Bugs/Todo
================
 * It's currently OS X and Windows only (on OSX, it relies on AppKit to access to clipboard). Linux support will be coming soon.
 * I want to add some kind of grouping support. Right now the only way to do it is to name the keys you want to group something-keyname and use grep to filter them (use `boo all`).
 * Needs a `mv` command for renaming keys.

And of course if you have any ideas, feel free to open a new issue or if you're dedicated: submit a pull request!