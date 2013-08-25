OKCupid Filter
==============

A keyword filtering script for OKCupid. Automatically deletes messages with flagged terms.

Running is simple:

    python filter.py username password

The script will scrape all of your unread messages, check which ones contain any of the keywords found in keywords.txt, and automatically delete the message thread.