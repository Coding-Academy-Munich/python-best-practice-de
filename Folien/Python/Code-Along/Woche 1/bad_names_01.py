from dataclasses import dataclass


@dataclass
class BadNames:  # type: ignore
    the_list: list

    def get_them(self):
        list1 = []
        for x in self.the_list:
            if x[1] == 1:
                list1.append(x)
        return list1


if __name__ == "__main__":
    thing = BadNames([(i, 0, 0) for i in range(64)])
    thing.the_list[2] = (2, 1, 0)

    assert thing.get_them() == [(2, 1, 0)]
    print(thing.get_them())
