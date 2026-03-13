# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Abstrakte Klassen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Motivation
#
# - Wir hatten bei einer Aufgabe zur Vererbung die folgende Klassenhierarchie:

# %%
class Employee: ...


# %%
class Manager(Employee): ...


# %%
class Worker(Employee): ...


# %% [markdown]
#
# - `Employee` dient nur dazu das gemeinsame Verhalten von `Manager` und `Worker`
#   zu definieren
# - Es sollten keine Instanzen von `Employee` erzeugt werden können
# - Im Moment ist das aber möglich

# %% [markdown]
#
# ## Abstrakte Klassen
#
# - Klassen, von denen keine direkte Instanz erzeugt werden kann
# - Haben die Klasse `abc.ABC` als Basisklasse
#     - (Eigentlich ist eine Metaklasse verantwortlich für das Verhalten)
# - Erlauben die Verwendung des `@abstractmethod` Decorators um abstrakte Methoden
#   zu definieren
#     - Der Rumpf einer abstrakten Methode ist oft `...`
# - Abstrakte Klassen, die nur abstrakte Methoden haben nennt man Interfaces
#     - Interfaces beschreiben Anforderungen an ihre Unterklassen

# %%
...

# %% [markdown]
#
# ### Die abstrakte `Employee` Klasse

# %%
from abc import ABC, abstractmethod


# %%
class Employee(ABC):
    @abstractmethod
    def salary(self) -> float: ...


# %%
# e = Employee()

# %%
# e.salary()

# %% [markdown]
#
# ### Die `Manager` und `Worker` Klassen

# %%
class Manager(Employee):  # type: ignore
    def __repr__(self):
        return f"Manager()"

    def salary(self) -> float:
        return 100_000.0


# %%
m = Manager()
m

# %%
m.salary()


# %%
class Worker(Employee):  # type: ignore
    def __repr__(self):
        return f"Worker()"

    def salary(self) -> float:
        return 50_000.0


# %%
w = Worker()
w

# %%
w.salary()


# %% [markdown]
#
# ### Die `Company` Klasse
#
# - Wir definieren eine Klasse, die eine Liste von `Employee` Objekten verwaltet

# %%
class Company:
    def __init__(self, employees: list[Employee]):
        self._employees = employees

    def __repr__(self):
        return f"Company({self._employees})"

    def monthly_expenses(self) -> float:
        return sum(e.salary() for e in self._employees)


# %%
c = Company([m, w])
c

# %%
c.monthly_expenses()

# %% [markdown]
# - Abstrakte Methoden können eine Implementierung haben
# - Klassen, die von einer abstrakten Klasse erben aber nicht alle abstrakten
#   Methoden überschreiben sind selber abstrakt.

# %%
from abc import ABC, abstractmethod


# %%
class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("Hi!")


# %%
class MyClass(MyBase, ABC):
    pass


# %%
# mc = MyClass()


# %%
class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")


# %%
yc = YourClass()
yc.my_method()

# %% [markdown]
#
# ## Workshop: Nochmal Geometrische Formen
#
# In diesem Workshop implementieren Sie Klassen für geometrische Formen unter
# Verwendung von abstrakten Basisklassen (ABCs).
#
# - Erstellen Sie eine Basisklasse `Shape` mit abstrakten Methoden für die
#   Berechnung von Fläche und Umfang.
# - Erstellen Sie konkrete Unterklassen für Rechtecke und Kreise, die von der
#   Klasse `Shape` erben und die abstrakten Methoden implementieren.
# - Testen Sie Ihre Implementierung mit verschiedenen Dimensionen.


# %% [markdown]
#
# ### Hinweise
#
# - Sie können das Modul `math` für den Wert von π verwenden.
# - Die Fläche eines Rechtecks berechnet sich als `width * height`, der Umfang als
#   `2 * (width + height)`.
# - Die Fläche eines Kreises berechnet sich als `π * radius ** 2`, der Umfang als
#   `2 * π * radius`.


# %%
from abc import ABC, abstractmethod
import math


# %%
class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...


# %%
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# %%
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# %%
rectangle = Rectangle(width=4, height=5)

# %%
assert rectangle.area() == 20

# %%
assert rectangle.perimeter() == 18

# %%
circle = Circle(radius=3)

# %%
from math import isclose

# %%
assert isclose(circle.area(), 28.2743, abs_tol=1e-4)

# %%
assert isclose(circle.perimeter(), 18.8495, abs_tol=1e-4)


# %% [markdown]
#
# ### Bonusaufgaben:
#
# - Erweitern Sie den Workshop, indem Sie zusätzliche Klassen für geometrische
#   Formen wie `Triangle` erstellen, die von `Shape` erben und ihre jeweiligen
#   Methoden implementieren.
# - Erstellen Sie eine Klasse `Drawing`, die eine Liste von Formen speichert und
#   Methoden zur Berechnung der Gesamtfläche und des Gesamtumfangs aller Formen in
#   der Zeichnung implementiert (unter der Annahme, dass sie sich nicht
#   überschneiden).

# %%
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

    @property
    def base(self):
        return self.a

    @property
    def height(self):
        return (
            0.5
            / self.a
            * math.sqrt(
                (self.a + self.b + self.c)
                * (self.a + self.b - self.c)
                * (self.a - self.b + self.c)
                * (-self.a + self.b + self.c)
            )
        )

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.a + self.b + self.c


# %%
triangle = Triangle(a=3, b=4, c=5)

# %%
assert triangle.area() == 6

# %%
assert triangle.perimeter() == 12


# %%
class Drawing:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)


# %%
drawing = Drawing(shapes=[rectangle, circle, triangle])

# %%
assert isclose(
    drawing.total_area(),
    rectangle.area() + circle.area() + triangle.area(),
    abs_tol=1e-4,
)

# %%
assert isclose(
    drawing.total_perimeter(),
    rectangle.perimeter() + circle.perimeter() + triangle.perimeter(),
    abs_tol=1e-4,
)


# %% [markdown]
#
# ## Workshop: Bessere Versionen der bisherigen Aufgaben
#
# Wir haben in allen bisherigen Workshops Klassen definiert, von denen es keine
# Instanzen geben sollte. Das konnten wir bisher im Code aber nicht ausdrücken.
#
# Im vorherigen Workshop haben wir das fur die geometrischen Formen explizit
# geändert.
#
# Verbessern Sie die Lösungen der anderen Vererbungs-Workshops ebenfalls, indem
# Sie die Basisklassen als abstrakte Klassen definieren.

