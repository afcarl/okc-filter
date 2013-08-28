OKCupid Filter
==============

A keyword filtering script for OKCupid. Automatically deletes messages with flagged terms. It also optionally handles minimum and maximum length constraints, skipping read messages, and focusing only on initial messages to which you have not yet replied.

Running is simple:

	usage: python filter.py [-h] [--keywords KEYWORDS] [--minlength MINLENGTH]
			                [--maxlength MAXLENGTH] [--initial] [--unread]
			                username password

positional arguments:
  username              Your OKCupid username.
  password              Your OKCupid password.

optional arguments:
  -h, --help            show this help message and exit
  --keywords KEYWORDS   The file containing the banned keywords.
  --minlength MINLENGTH
                        The minimum length (number of characters) a message
                        must be to be acceptable.
  --maxlength MAXLENGTH
                        The maximum length (number of characters) a message
                        can be to be acceptable.
  --initial             Skip message threads if you've replied to them
                        already.
  --unread              Skip message threads if you've already read them.

The script will scrape all of your unread messages, check which ones contain any of the keywords found in keywords.txt, and automatically delete the message thread.

Feedback and help setting it up
-------------------------------

I'm happy to hear OKC users' thoughts and feedback on this. Also, if you'd like to set it up on your machine, I can help with that too. Just message me on OKC: madethisupquick.