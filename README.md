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

Running the Program
-------------------

To run the show parser, run:

```bash
$ ./show_parser.py
```

At this time, this simply prints the list of shows to the console. TODO: Output an HTML file.

To run the rental parser, run:

```bash
$ ./rental_parser.py --region <region>
```

**Note:** This is currently configured to run with the following regions: `bay_area` and `seattle`.

This produces `<region>_rentals.html`, which you can then open in your browser to view available listings.

Using the Collector
-------------------

The *Collector* simply pulls data from a set of sites, filling in a dictionary as specified by each site parser. Create a new *Collector* with a YAML config file, the directory of parsers, and specify whether you're debugging.

```bash
collector = Collector('config/<your_config_file>', '<parser_directory>', <True|False>)
list_of_dictionaries = collector.scrape_sites()
```

Updating configurations
-----------------------

As sites each have individual methods of displaying their topic information, you need to add the logic necessary for each site to the appropriate parsers directory. Create a new parser file with a *parse* method, and update the config file to include the name of the parser and the url of the page.

Building the Parser
-------------------

The mechanics of getting to the necessary fields are up to you, but the main show parser program expects to receive a list of dictionaries containing the fields *headliner*, *openers*, *date*, and *time*. The rental parser program expects a list of dictionaries containing the fields *title*, *price*, *address*, *bed/bath*, *size*, and *url*. 

Debugging
---------

When building a new parser, constantly loading the website can take some time. If you run the main parser with the `-d` option, the main parser will automatically load from an html file in the `debug_sites` directory. The name of the html file should match the individual parser's config name. For instance, if you have a parser specified as `masonic`, it would debug from `debug_sites/masonic/html`.

TODO
----

-	add more venues
-	include a test suite that can run local html files and verify output
