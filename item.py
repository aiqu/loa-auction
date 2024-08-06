from item_option import ItemOption

def parse_options(options_response):
    options = list()
    for option in options_response:
        if option['Type'] not in ('ARK_PASSIVE', 'ACCESSORY_UPGRADE'):
            continue
        options.append(ItemOption(option))
    return options

class Item:
    def __init__(self, item_response=""):
        self.name = ""
        self.quality = -1
        self.price = -999
        self.options = []
        if item_response == "" or not ('BuyPrice' in item_response['AuctionInfo']):
            return
        self.name = item_response['Name']
        self.quality = item_response['GradeQuality']
        self.price = item_response['AuctionInfo']['BuyPrice']
        self.options = parse_options(item_response['Options'])
    def __str__(self):
        return f'{self.name}, Quality: {self.quality}, Price: {self.price}, Options grade: {self.get_total_option_grade()} Options: {','.join([f'{o}' for o in self.options])}'
    def to_dict(self):
        return {'name': self.name, 'quality': self.quality, 'price': self.price, 'options': [o.to_dict() for o in self.options]}
    @classmethod
    def from_dict(cls, item_dict):
        new_item = Item()
        new_item.name = item_dict['name']
        new_item.price = item_dict['price']
        new_item.quality = item_dict['quality']
        new_item.options = [ItemOption.from_dict(o) for o in item_dict['options']]
        return new_item
    def get_total_option_grade(self):
        return sum([o.option_grade() for o in self.options])
    def __lt__(self, other):
        my_grade = self.get_total_option_grade()
        other_grade = other.get_total_option_grade()
        if my_grade != other_grade:
            return my_grade < other_grade
       # option -> price
        return self.price > other.price 