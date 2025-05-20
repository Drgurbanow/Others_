import csv
from collections import defaultdict
from typing import IO

class Solve_all_2:
    _All = list()

    def __init__(self, file_csv: str):
        if isinstance(file_csv, str):
            self.file = file_csv
            self.__read()
        else:
            raise TypeError("WRONG_PATH")

    def __read(self):
        with open(self.file, mode="r", encoding="utf-8") as file:
            for i in csv.DictReader(file):
                Solve_all_2._All.append(i)

    def __type_conv(self, t: IO):
        if t == "'invoice_id":
            return "int"
        if t in ('units_sold', 'price_per_unit', 'amount'):
            return "float"
        if t == 'date':
            return "datetime"
        return "str"

    def __help_count(self, mode: str):
        x = defaultdict(int)
        modes = {"amount": 'float(i["amount"])', 'quantity': '1', 'unit_sold': 'int(i["units_sold"])'}
        for i in self._All:
            x[i["product_name"]] += eval(modes[mode])
        return x

    def get_the_data_types(self):
        for i in self._All:
            return dict((k, __class__.__type_conv(self, k)) for k, v in i.items())

    def sold_amount(self):
        x = __class__.__help_count(self, "amount")
        return dict((k, round(v, 2)) for k, v in sorted(x.items(), key=lambda i: i[1], reverse=True)[:10])

    def sold_quantity(self):
        x = __class__.__help_count(self, "quantity")
        return dict(sorted(x.items(), key=lambda i: i[1], reverse=True))

    def product_per_unit_sold(self):
        x = __class__.__help_count(self, "unit_sold")
        return dict(sorted(x.items(), key=lambda i: i[1], reverse=True))

    def about_target(self, target='HAND WARMER SCOTTY DOG DESIGN'):
        x = dict()
        for i in self._All:
            if i['product_name'] == target:
                x.setdefault(i['invoice_id'], {}).setdefault(i['product_name'], i['units_sold'])
        return x

    def sold_sum_per_check(self):
        x = dict()
        for i in self._All:
            x.setdefault(i['invoice_id'], {"units": 0, "amount": 0.0})
            x[i['invoice_id']]["units"] += int(i["units_sold"])
            x[i['invoice_id']]["amount"] += round(float(i['amount']))
        return x

    def slice_data(self, start: int = 20, stop: int = 60):
        return dict(sorted(self.sold_sum_per_check().items())[start:stop])

    def slice_statistics(self):
        amount_sum = sum(float(i['amount']) for i in self.slice_data().values())
        avg_check_sum = amount_sum / len(self.slice_data())
        max_check = max(self.slice_data().items(), key=lambda x: float(x[1]['amount']))
        return {max_check[0]: max_check[1]}, avg_check_sum, amount_sum
    