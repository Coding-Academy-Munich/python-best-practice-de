# %%
# <!--
# clang-format off
# -->
# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>SOLID: Liskov-Substitutions-Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # SOLID: Liskov Substitutions-Prinzip
#
# Ein Objekt einer Unterklasse soll immer für ein Objekt der Oberklasse
# eingesetzt werden können.

# %% [markdown]
#
# ## LSP Verletzung

# %%
# This Python code snippet is an include directive for input/output operations.
# It does not have a direct Python equivalent because Python does not require such preprocessor directives.
# Python's input/output functionality is available by default.


# %%
class Rectangle:
    def __init__(self, l: float, w: float):
        self._length = l
        self._width = w

    def area(self) -> float:
        return self._length * self._width

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, l: float):
        self._length = l

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, w: float):
        self._width = w


# %%
class Square(Rectangle):
    def __init__(self, l: float):
        super().__init__(l, l)

    def set_length(self, l: float):
        self.length = l
        self.width = l

    def set_width(self, w: float):
        self.length = w
        self.width = w


# %%
class Rectangle:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value: int):
        self._length = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    def area(self) -> int:
        return self._length * self._width


my_rect = Rectangle(3, 4)
print(f"Area is {my_rect.area()}")
my_rect.length = 10
my_rect.width = 12
print(
    f"After setting values: Length is {my_rect.length}, Width is {my_rect.width}\nArea is now {my_rect.area()}"
)

# %%
my_square = Square(3)
print(f"Area is {my_square.area()}")
my_square.length = 10
my_square.width = 12
print(
    f"After setting values: Length is {my_square.length}, Width is "
    f"{my_square.width}\nArea is now {my_square.area()}"
)
