# PYROMATIC - Pyramid implemented RENT-O-MATIC project

This is an adaptation of the Rent-o-matic project as described in the
[Leonardo Giordani blog post about Clean Architecture with Python](http://blog.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/).
The original project was done in Flask and can be found [here](https://github.com/lgiordani/rentomatic).



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
