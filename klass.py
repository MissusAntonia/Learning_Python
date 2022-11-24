class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year

    def __str__(self):
        return f'FunEvent(tags={self.tags},year={self.year})'


tags=['Eid','adha']
year=2022
bootcamp =FunEvent(tags,year)
print(bootcamp)
tags.append('bootcamp')
year =2023
print(bootcamp)
