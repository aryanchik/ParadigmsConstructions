class Unique(object):
    def __init__(self, items, **kwargs):

        self.ignore_case = kwargs.get('ignore_case', False)


        self.items = items
        self.index = 0


        self.seen = set()


        if not isinstance(items, (list, tuple)):
            self.items = list(items)

    def __next__(self):
        while self.index < len(self.items):
            current_item = self.items[self.index]
            self.index += 1


            if self.ignore_case and isinstance(current_item, str):
                key = current_item.lower()
            else:
                key = current_item


            if key not in self.seen:
                self.seen.add(key)
                return current_item

        raise StopIteration

    def __iter__(self):
        return self
