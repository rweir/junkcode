# tiny twisted plugin system example

Copied from [the Twisted docs](https://docs.twistedmatrix.com/en/stable/core/howto/plugin.html),
this is just here to make it super clear how to layout your code for
twisted.plugin.

Make sure this directory is in PYTHONPATH.  Note that twisted and
twisted/plugins are *NOT* packages, but are specially trawled by getPlugins.
