OKCupid Filter
==============

A keyword filtering script for OKCupid. Automatically deletes messages with flagged terms. It also handles minimum and maximum length constraints.

Running is simple:

    python filter.py [-h] [--keywords KEYWORDS] [--minlength MINLENGTH]
                 [--maxlength MAXLENGTH]
                 username password

The script will scrape all of your unread messages, check which ones contain any of the keywords found in keywords.txt, and automatically delete the message thread.

Feedback and help setting it up
-------------------------------

I'm happy to hear OKC users' thoughts and feedback on this. Also, if you'd like to set it up on your machine, I can help with that too. Just message me on OKC: madethisupquick.