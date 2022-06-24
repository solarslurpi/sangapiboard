
Python code for the Openflexure Microscope Server is located in [this Gitlab repo](http://gitlab.com/openflexure/openflexure-microscope-server).

Arduino code for the Sangaboard is located in [this Gitlab repo](http://gitlab.com/bath_open_instrumentation_group/sangaboard).

Sangaboard Python modules are located in [this Gitlab repo](https://gitlab.com/bath_open_instrumentation_group/pysangaboard)

Strategy : write a shim of ExtensibleSerialInterface and see if I can mask changes to OFM code.  New strategy is to reimplement the Sangaboard class.