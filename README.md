Local Show Parser
=================

Requirements
------------

If you are first setting up, run: 

```bash
$ mkvirtualenv shows
$ pip install -r requirements.txt
```

If returning and updating requirements, run:

```bash
$ workon shows
$ pip install -r requirements.txt
```

If not already installed, download [PhantomJS](http://phantomjs.org/download.html) and copy the phantomjs file to /usr/local/bin/. 

Updating configurations
-----------------------

As venues each have individual methods of displaying their show information, you need to add the logic necessary for each site to the *venue_parsers* directory. Create a new parser file with a *parse* method, and update the *venues.yml* file to include the name of the parser and the url of the venue's show page.

Building the Parser
-------------------

The mechanics of getting to the necessary fields are up to you, but the main program expects to receive a list of dictionaries containing the fields *headliner*, *openers*, *date*, and *time*.

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