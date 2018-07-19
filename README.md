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



## Study references

# [RESTFUL APIs Tutorial](https://restfulapi.net/)

Principal entidade no que se diz respeito ao entendimento de RESTFUL APIs é **RECURSO**.
Recurso é o elemento delineador dos principios que moldam o design arquitetural do
*Representational State Transfer*.

As 6 linhas guia de uma arquitetura são:

* Cliente-Servidor (client-server)
* Sem estado (stateless)
* Cacheable
* Interface uniforme (uniform interface)
* Sistema com camadas (layered system)
* Codigo sob demanda (code on demand)

Os 3 ultimos items tem implicações mais profundas na direção de implementação.

####     
    Uniform interface – By applying the software engineering principle of generality 
    to the component interface, the overall system architecture is simplified and the 
    visibility of interactions is improved. In order to obtain a uniform interface, 
    multiple architectural constraints are needed to guide the behavior of components. 
    
    REST is defined by four interface constraints: 
        - identification of resources;
        - manipulation of resources through representations;
        - self-descriptive messages;
        - hypermedia as the engine of application state

#### 
    Layered system – The layered system style allows an architecture to be composed of hierarchical 
    layers by constraining component behavior such that each component cannot “see” beyond the 
    immediate layer with which they are interacting.

#### 
    Code on demand (optional) – REST allows client functionality to be extended by downloading and 
    executing code in the form of applets or scripts. This simplifies clients by reducing the 
    number of features required to be pre-implemented.

## Cornerstones

    One of the first implementations may be found in the Boundary-Control-Entity model proposed by 
    Ivar Jacobson in his masterpiece "Object-Oriented Software Engineering: A Use Case Driven Approach" 
    published in 1992, but Martin lists other more recent versions of this architecture.


https://blog.8thlight.com/uncle-bob/2012/08/13/the-clean-architecture.html
https://blog.8thlight.com/uncle-bob/2014/05/12/TheOpenClosedPrinciple.html
https://www.youtube.com/watch?v=HhNIttd87xs
http://www.taimila.com/blog/ddd-and-testing-strategy/

## Conceitos

https://spring.io/understanding/HATEOAS

### Discussoes

https://capgemini.github.io/architecture/is-rest-best-microservices/
https://medium.com/@ericjwhuang/restful-api-vs-microservice-eea903ac3e73
https://container-solutions.com/argument-rest-microservices/
https://medium.com/@andreasreiser94/why-hateoas-is-useless-and-what-that-means-for-rest-a65194471bc8
https://jeffknupp.com/blog/2014/06/03/why-i-hate-hateoas/


https://www.infoq.com/news/2016/10/service-based-architecture
## Tutoriais


### General REST

https://dzone.com/articles/restful-web-services-with-python-flask

https://realpython.com/create-a-rest-api-in-minutes-with-pyramid-and-ramses/
https://medium.com/@ssola/building-microservices-with-python-part-i-5240a8dcc2fb
http://blog.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/


https://www.fullstackpython.com/api-creation.html
### Techs

https://www.toptal.com/python/orchestrating-celery-python-background-jobs

### Guides

https://cloud.google.com/apis/design/


### Courses

https://www.coursera.org/specializations/software-design-architecture


## Anotações

O elemento de representatividade de um determinado **recurso** deve ser sempre levado
em conta quando se está realizando a modelagem de uma API REST. O serializador (encoder)
deve lidar com o MODELO e mapear de forma devida pra parte do formato que se está desejando
representar o objeto

