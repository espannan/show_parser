Local Show Parser
=================

Requirements
------------

If you are first setting up, run: 

```bash
$ mkvirtualenv scraper
$ pip install -r requirements.txt
```

If returning and updating requirements, run:

```bash
$ workon scraper
$ pip install -r requirements.txt
```

If not already installed, download [PhantomJS](http://phantomjs.org/download.html) and copy the phantomjs file to /usr/local/bin/. 

Using the Collector
-------------------

The *Collector* simply pulls data from a set of sites, filling in a dictionary as specified by each site parser. Create a new *Collector* with a YAML config file and specify whether you're debugging.

```bash
collector = Collector('config/<your_config_file>')
list_of_dictionaries = collector.scrape_sites()
```

Updating configurations
-----------------------

As sites each have individual methods of displaying their topic information, you need to add the logic necessary for each site to the appropriate parsers directory. Create a new parser file with a *parse* method, and update the config file to include the name of the parser and the url of the page.

Building the Parser
-------------------

The mechanics of getting to the necessary fields are up to you, but the main program expects to receive a list of dictionaries containing the fields *headliner*, *openers*, *date*, and *time*.

Running the program
-------------------

To run, simply enter either of the following commands:

```bash
$ ./show_parser.py
$ ./rental_parser.py
```

TODO
----

-	add more venues
-	include a test suite that can run local html files and verify output