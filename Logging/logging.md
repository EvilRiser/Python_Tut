## Basic Logging Tutorial
_____

```
Note: The default level is WARNING
```

```python

```
Example
```python
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')
```

##### Logging to a file

-> logging.basicConfig(filename=,
                        filemode=,
                        encoding=,
                        level=
)
```python
import logging
logging.basicConfig(filename='example.log',  filemode='w', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

#### Changing the format of displayed messages

To change the format which is used to display messages, you need to specify the format you want to use

format='%(asctime)s %(levelname)s:%(message)s'
datefmt='%m/%d/%Y %I:%M:%S %p'

```python

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
```
will print  

```python
12/12/2010 11:46:36 AM is when this event was logged.
```


## Advanced Logging Tutorial

The logging library takes a modular approach and offers several categories of components: loggers, handlers, filters, and formatters.  

* Loggers expose the interface that application code directly uses.  
* Handlers send the log records (created by loggers) to the appropriate destination.  
* Filters provide a finer grained facility for determining which log records to output.
* Formatters specify the layout of log records in the final output.

Log event information is passed between loggers, handlers, filters and formatters in a LogRecord instance.

Logging is performed by calling methods on instances of the Logger class.  


A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:
```python
logger = logging.getLogger(__name__)
```
This means that logger names track the package/module hierarchy, and it’s intuitively obvious where events are logged just from the logger name.  

It is, of course, possible to log messages to different destinations. Support is included in the package for writing log messages to files, HTTP GET/POST locations, email via SMTP, generic sockets, queues, or OS-specific logging mechanisms such as syslog or the Windows NT event log. Destinations are served by handler classes. You can create your own log destination class if you have special requirements not met by any of the built-in handler classes.

The default format set by basicConfig() for messages is:
```
severity:logger name:message
```
## Configuring Logging

Programmers can configure logging in three ways:

1. Creating loggers, handlers, and formatters explicitly using Python code that calls the configuration methods listed above.
2. Creating a logging config file and reading it using the fileConfig() function.
3. Creating a dictionary of configuration information and passing it to the dictConfig() function.



Example
  using simple logger, a console handler, and a simple formatter

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```
Output
```
$ python simple_logging_module.py
2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
2005-03-19 15:10:26,620 - simple_example - INFO - info message
2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
2005-03-19 15:10:26,697 - simple_example - ERROR - error message
2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message
```

The following Python module creates a logger, handler, and formatter nearly identical to those in the example listed above, with the only difference being using filehandler
```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

logging.conf file
```
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

Output
```
$ python simple_logging_config.py
2005-03-19 15:38:55,977 - simpleExample - DEBUG - debug message
2005-03-19 15:38:55,979 - simpleExample - INFO - info message
2005-03-19 15:38:56,054 - simpleExample - WARNING - warn message
2005-03-19 15:38:56,055 - simpleExample - ERROR - error message
2005-03-19 15:38:56,130 - simpleExample - CRITICAL - critical message
```

logfile.yaml
```
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  simpleExample:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```


REFERENCE: https://docs.python.org/3/howto/logging-cookbook.html#

