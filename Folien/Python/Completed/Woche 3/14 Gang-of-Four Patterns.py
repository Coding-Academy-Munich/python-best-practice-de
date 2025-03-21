# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Gang-of-Four Patterns</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ### Design-Pattern im GoF-Katalog
#
# -   **Pattern Name and Classification**
#     The pattern's name conveys the essence of the pattern succinctly. A
#     good name is vital, because it will become part of your design
#     vocabulary.
#
# -   **Intent**
#     A short statement that answers the following question: What does the
#     design pattern do? What is its rational and intent? What particular
#     design issue or problem does it address?
#
# -   **Also Known As**
#     Other well-known names for the pattern, if any.

# %% [markdown]
# ### Design-Pattern im GoF-Katalog
#
# -   **Motivation**
#     A scenario that illustrates a design problem and how the class and
#     object structures in the pattern solve the problem. The scenario will
#     help you understand the more abstract descriptions of the pattern
#     that follows.
#
# -   **Applicability**
#     What are the situations in which the design pattern can be applied?
#     What are examples of poor designs that the pattern can address? How
#     can you recognize these situations?
#
# -   **Structure**
#     A graphical representation of the classes in the pattern using a
#     notation based on the Object Modelling Technique (OMT). We also use
#     interaction diagrams to illustrate sequences of requests and
#     collaborations between objects.


# %% [markdown]
#
# ### Design-Pattern im GoF-Katalog
#
# -   **Participants**
#     The classes and/or objects participating in the design pattern and
#     their responsibilities.
#
# -   **Collaborations**
#     How the participants collaborate to carry out their
#     responsibilities.
#
# -   **Consequences**
#     How does the pattern support its objectives? What are the trade-offs
#     and results of using the pattern? What aspects of system structure
#     does it let you vary independently?
#
# -   **Implementation**
#     What pitfalls, hints, or techniques should you be aware of when
#     implementing the pattern? Are there language-specific issues?


# %% [markdown]
# ### Design-Pattern im GoF-Katalog
#
# -   **Sample Code**
#     Code fragments that illustrate how you might implement the pattern
#     in C++ or Smalltalk.
#
# -   **Known Uses**
#     Examples of the pattern found in real systems. We include at least
#     two examples from different domains.
#
# -   **Related Patterns**
#     What design patterns are closely related to this one? What are the
#     important differences? With which other patterns should this one be
#     used?

# %% [markdown]
#
# ### Klassifikation der GoF Design Pattern
#
# -   **Creational Patterns** (befassen sich mit der Erzeugung von
#     Objekten)
#
# -   **Structural Patterns** (befassen sich mit der strukturellen
#     Komposition von Klassen oder Objekten)
#
# -   **Behavioral Patterns** (befassen sich mit der Interaktion von
#     Objekten und der Verteilung von Verantwortlichkeiten)


# %% [markdown]
# ### Creational Patterns
#
# -   **Abstract Factory** Provide an interface for creating families of
#     related or dependent objects without specifying their concrete
#     classes.
#
# -   **Builder** Separate the construction of a complex object from its
#     representation so that the same construction process can create
#     different representations.
#
# -   **Factory Method** Define an interface for creating an object, but
#     let subclasses decide which class to instantiate. Factory Method
#     lets a class defer instantiation to subclasses.
#
# -   **Prototype** Specify the kinds of objects to create using a
#     prototypical instance, and create new objects by copying this
#     prototype.
#
# -   **Singleton** Ensure a class only has one instance, and provide a
#     global point of access to it.


# %% [markdown]
# ### Structural Patterns
#
# -   **Adapter** Convert the interface of a class into another interface
#     clients expect. Adapter lets classes work together that couldn't
#     otherwise because of incompatible interfaces.
#
# -   **Bridge** Decouple an abstraction from its implementation so that
#     the two can vary independently.
#
# -   **Composite** Compose objects into tree structures to represent
#     part-whole hierarchies. Composite lets clients treat individual
#     objects and compositions of objects uniformly.


# %% [markdown]
# ### Structural Patterns
#
# -   **Decorator** Attach additional responsibilities to an object
#     dynamically. Decorators provide a flexible alternative to
#     subclassing for extending functionality.
#
# -   **Facade** Provide a unified interface to a set of interfaces in a
#     subsystem. Facade defines a higher-level interface that makes the
#     subsystem easier to use.
#
# -   **Flyweight** Use sharing to support large numbers of fine-grained
#     objects efficiently.
#
# -   **Proxy** Provide a surrogate or placeholder for another object to
#     control access to it.

# %% [markdown]
# ### Behavioral Patterns
#
# -   **Chain of Responsibility** Avoid coupling the sender of a request
#     to its receiver by giving more than one object a chance to handle
#     the request. Chain the receiving objects and pass the request along
#     the chain until an object handles it.
#
# -   **Command** Encapsulate a request as an object, thereby letting you
#     parameterize clients with different requests, queue or log requests,
#     and support undoable operations.
#
# -   **Interpreter** Given a language, define a representation for its
#     grammar along with an interpreter that uses the representation to
#     interpret sentences in the language.
#
# -   **Iterator** Provide a way to access the elements of an aggregate
#     object sequentially without exposing its underlying representation.


# %% [markdown]
# ### Behavioral Patterns
#
# -   **Strategy** Define a family of algorithms, encapsulate each one,
#     and make them interchangeable. Strategy lets the algorithm vary
#     independently from clients that use it.
#
# -   **Template Method** Define the skeleton of an algorithm in an
#     operation, deferring some steps to subclasses. Template Method lets
#     subclasses redefine certain steps of an algorithm without changing
#     the algorithm's structure.
#
# -   **Visitor** Represent an operation to be performed on the elements
#     of an object structure. Visitor lets you define a new operation
#     without changing the classes of the element on which it operates.

