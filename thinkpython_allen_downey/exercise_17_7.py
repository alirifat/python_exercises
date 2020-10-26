class Kangaroo():
    def __init__(self):
        self.pouch_contests = []
    def put_in_pouch(self, other):
        self.pouch_contests.append(other)
    def __str__(self):
        return ' '.join([object.__str__(item) for item in self.pouch_contests])

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
kanga.put_in_pouch('a')
kanga.put_in_pouch('z')
roo.put_in_pouch('v')
print(kanga)
print(roo)
