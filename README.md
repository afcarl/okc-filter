OKCupid Filter
==============

A keyword filtering script for OKCupid. Automatically deletes messages with flagged terms. It also optionally handles minimum and maximum length constraints, skipping read messages, and focusing only on initial messages to which you have not yet replied.

Running is simple:

	usage: python filter.py [-h] [--keywords KEYWORDS] [--minlength MINLENGTH]
			                [--maxlength MAXLENGTH] [--initial] [--unread]
			                username password

Positional arguments:

* __username__:              Your OKCupid username.

* __password__:              Your OKCupid password.

Optional arguments:

* __-h, --help__:            shows this help message and exits

* __--keywords KEYWORDS__:   The file containing the banned keywords.

* __--minlength MINLENGTH__: The minimum length (number of characters) a message must be to be acceptable.

* __--maxlength MAXLENGTH__: The maximum length (number of characters) a message can be to be acceptable.

* __--initial__:             Skip message threads if you've replied to them already.

* __--unread__:              Skip message threads if you've already read them.

The script will scrape all of your unread messages, check which ones contain any of the keywords found in keywords.txt, and automatically delete the message thread.

Feedback and help setting it up
-------------------------------

I'm happy to hear OKC users' thoughts and feedback on this. Also, if you'd like to set it up on your machine, I can help with that too. Just message me on OKC: madethisupquick.