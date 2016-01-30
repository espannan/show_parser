Local Show Parser
=================

Requirements
------------

This project requires Yaml and BeautifulSoup. To install, run:

```bash
$ pip install pyaml
$ pip install beautifulsoup4
```

Updating configurations
-----------------------

As venues each have individual methods of displaying their show information, you need to add the logic necessary for each site to the *venue_parsers* directory. Create a new parser file with a *parse* method, and update the *venues.yml* file to include the name of the parser and the url of the venue's show page.

Running the program
-------------------

To run, simply enter:

```bash
$ python show_collector.py
```

TODO
----

-	add more venues
-	include a test suite that can run local html files and verify output