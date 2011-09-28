What's this?
===========
Boo is a reimplementation of a handy tool I saw in one of [Zach Holman](https://github.com/holman)'s [screencasts](http://zachholman.com/screencast/vagranception/). Basically it's a key value store that allows you to save snippits of text that you can later find and copy to your clipboard.

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

Release Log
============
None yet. I'm still in pretty early stages of development, however boo is pretty usable even at this stage.