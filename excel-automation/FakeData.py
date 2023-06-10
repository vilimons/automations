import pandas as pd
import random
from faker import Faker
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Any, NoReturn, TypeVar

pd.set_option('display.max_columns', None)
DateStr: TypeVar = str


@dataclass
class FakeDataset:
    dataset_size: int = field(default=1000)
    start_date: DateStr = field(default='01/01/2015')
    end_date: DateStr = field(default='01/01/2023')
    filter_list: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.fake = Faker('de_DE')
        fake_data = self.create_fake_customers()
        self.fake_dataframe = self.create_fake_customer_dataset(
            fake_data, self.filter_list)

    def create_transaction_dates(self) -> datetime.date:
        # Transactions Dates, start and end date must follow month/day/year date pattern
        start_date = datetime.strptime(self.start_date, '%m/%d/%Y')
        end_date = datetime.strptime(self.end_date, '%m/%d/%Y')
        if start_date > end_date:
            raise ValueError("Start date can´t be bigger than end date.")
        transaction_date = self.fake.date_between(start_date, end_date)
        return transaction_date

    def create_fake_customers(self) -> Dict[str, Any]:
        transaction_date = list(
            map(lambda date: self.create_transaction_dates(), range(self.dataset_size)))
        name = list(map(lambda name: self.fake.name(),
                    range(self.dataset_size)))
        gender = list(map(lambda choice: random.choice(
            ["M", "F"]), range(self.dataset_size)))
        email = list(map(lambda email: self.fake.ascii_email(),
                     range(self.dataset_size)))
        city = list(map(lambda city: self.fake.city(),
                    range(self.dataset_size)))
        product_id = list(map(lambda p_id: self.fake.ean(
            length=8), range(self.dataset_size)))
        amount_spent = list(map(lambda amount: self.fake.pyfloat(right_digits=2,
                                                                 positive=True,
                                                                 min_value=1,
                                                                 max_value=100), range(self.dataset_size)))

        fake_data_dict = {
            'transaction_date': transaction_date,
            'name': name,
            'gender': gender,
            'email': email,
            'city': city,
            'product_id': product_id,
            'amount_spent': amount_spent
        }
        return fake_data_dict

    def create_fake_customer_dataset(self, fake_dict: Dict[str, Any], columns_wanted: List[str] = None) -> pd.DataFrame:
        if columns_wanted:
            if not set(columns_wanted).issubset(set(fake_dict.keys())):
                raise ValueError(""""Can only create fake dataset with 
                transaction_date, name, gender, email, city, product_id""")
            filter_dict = dict(
                filter(lambda key: key[0] in columns_wanted, fake_dict.items()))
            return pd.DataFrame(filter_dict)
        else:
            return pd.DataFrame(fake_dict)

    def save_excel(self) -> NoReturn:
        self.fake_dataframe.to_excel(
            excel_writer=f"./data/fake_data.xlsx", index=False)


if __name__ == "__main__":
    fake_data = FakeDataset()
    fake_data.save_excel()
