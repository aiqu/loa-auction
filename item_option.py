A=5
B=3
C=1

# 상상 10
# 상중 8
# 상하 6
# 중중 6
# 상 5
option_grade = {
    '적에게 주는 피해 증가': {'2': A, '1.2': B, '0.55': C},
    '추가 피해': {'2.6': A, '1.6': B, '0.6': C},
    r'공격력 ': {'1.55': A, '0.95': B, '0.4': C},
    r'무기 공격력 ': {'3.0': A, '1.8': B, '0.8': C},
    '치명타 적중률': {'1.55': A, '0.95': B, '0.4': C},
    '치명타 피해': {'4': A, '2.4': B, '1.1': C}
}

class ItemOption:
    def __init__(self, option_response=""):
        self.type = ""
        self.name = ""
        self.value = 0
        if option_response == "":
            return
        if not option_response['Type'] in ('ARK_PASSIVE', 'ACCESSORY_UPGRADE'):
            raise TypeError(f"Only accepts ARK_PASSIVE or ACCESSORY_UPGRADE but got {option_response['Type']}")
        self.type = option_response['Type']
        self.name = option_response['OptionName']
        self.value = option_response['Value']
    def __str__(self):
        return f'{self.name}: {self.value}'
    def to_dict(self):
        return {'type': self.type, 'name': self.name, 'value': self.value}
    @classmethod
    def from_dict(cls, option_dict):
        new_item_option = ItemOption()
        new_item_option.type = option_dict['type']
        new_item_option.name = option_dict['name']
        new_item_option.value = option_dict['value']
        return new_item_option
    def option_grade(self):
        value_grade = option_grade.get(self.name, None)
        if not value_grade:
            return 0
        return value_grade.get(str(self.value), 0)