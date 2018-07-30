# PYROMATIC - Pyramid implemented RENT-O-MATIC project

This is an adaptation of the Rent-o-matic project as described in the
[Leonardo Giordani blog post about Clean Architecture with Python](http://blog.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/).
The original project was done in Flask and can be found [here](https://github.com/lgiordani/rentomatic).


## TODOS

* Implement another layer relative to data handling. In this case, the repository
  deals directly with information at memory and we want to be able to retrieve and
  save it in the database

* Implement XML serializers for the project entitities

* Add logging

## REFS

https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html


## Relevant notes


### [Abstract Base Classes](http://blog.thedigitalcatonline.com/blog/2016/04/03/abstract-base-classes-in-python/)
    The difference between a real and a virtual subclass is very simple: a real subclass 
    knows its relationship with the parent class through its __bases__ attribute, and can 
    thus implicitly delegate the resolution of missing methods. A virtual subclass knows 
    nothing about the class that registered it, and nowhere in the subclass will you find
    something that links it to the parent class. Thus, a virtual parent class is useful 
    only as a categorization.
    
    Classes that can register other classes, thus becoming virtual parents of those, 
    are called in Python Abstract Base Classes, or ABCs.
    
    It is very important to understand that registering a class does not imply any form 
    of check about methods or attributes. Registering is just the promise that a given
    behaviour is provided by the registered class.

### [WSGI - Web Server Gateway Interface](https://www.python.org/dev/peps/pep-3333/)

**(pronounced "whiz-gee" with a hard "g" or "whiskey")**

WSGI is a descendant of CGI, or Common Gateway Interface. When the web was just taking
baby steps, CGI proliferated because it worked with many languages, and there were no
other solutions. On the downside, it was slow and limited. Python apps could only use
CGI, mod_python, Fast CGI or some other flavor of a web server. WSGI was developed to
create a standard interface to route web apps and frameworks to web servers.

* It's an interface specification
* Designed to guide the construction application and client communication
* Server and application sides are specified at PEP 3333
* It can be stacked
* The ones in the middle (middleware), must implement both sides of the specification (client and server)
* A WSGI compliant server receives the request, pass it to the application and send it back the response returned by the application. It should do just that


Check [this](https://blog.appdynamics.com/engineering/an-introduction-to-python-wsgi-servers-part-1/) awesome post on WSGI web apps and options.


[WSGI tutorial](http://wsgi.tutorial.codepoint.net/)

#### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/)

* Waitress is a pure Python WSGI application server
* It does not have any external dependencies out of Python
* PasteDeploy handles the configuration of WSGI web components using INI files

    A config file has different sections. The only sections Paste Deploy cares 
    about have prefixes, like app:main or filter:errors – the part after the : 
    is the “name” of the section, and the part before gives the “type”. Other
    sections are ignored.

### PasteDeploy, setup.py and Python Eggs

```
    #
    # The only sections Paste Deploy cares about have prefixes

    # app:main specifices the type: name, so this is type 'app' with name 'main'

    [app:main]

    #
    # Python Eggs are a distribution and installation format produced by
    # setuptools and distribute that adds metadata to a normal Python package
    # (among other things).


    use = egg:pyromatic

    sqlalchemy.url = sqlite:///%(here)s/pyromatic.sqlite

    retry.attempts = 3

    ## OpenAPI
    pyromatic_api_file=%(here)s/pyromatic_api.yaml

    [server:main]
    use = egg:waitress#main
    listen = localhost:6543

```

The first important part about an Egg is that it has a specification. This is
formed from the name of your distribution (the name keyword argument to setup()),
and you can specify a specific version. So you can have an egg named MyApp, or
MyApp==0.1 to specify a specific version.

For our application:

```
setup(
    name='pyromatic',
    version='0.0',
    description='pyromatic',
    long_description=README + '\n\n' + CHANGES,

    ...

    entry_points={
        'paste.app_factory': [
            'main = pyromatic:main',
        ],
    },
)

```

The second is entry points. These are references to Python objects in your
packages that are named and have a specific protocol. “Protocol” here is just a
way of saying that we will call them with certain arguments, and expect a
specific return value.

In Pyramid, behind the curtains, the pyramid.paster package takes care of handling
the selected loader, in our case the PasteDeploy's loadapp. The app is configured
using the imported loader but is found by the `plaster` lib that seeks for
**pkg_resources entry points**. From the docs:

    This script can support any config format so long as the application (or the user)
    has installed the loader they expect to use. For example, pip install
    plaster_pastedeploy. The loader is then found by plaster.get_settings() based on
    the specific config uri provided. The application does not need to configure the
    loaders. They are discovered via pkg_resources entrypoints and registered for
    specific schemes.

So, although we see code that are unrelated on the memory level (because loadapp and
pyramid.paster apparently doesn't pass it around the app to each other), they do
deal with the same application because the same configuration file  used by both
mentions the same Python entry point: `egg:pyromatic:main`
