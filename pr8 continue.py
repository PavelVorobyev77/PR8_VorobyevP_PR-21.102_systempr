import os
import tempfile
import pickle


class Transaction:
    def __init__(self, amount, date, currency="USD", description=None):
        # Хранение данных о транзакции
        self._amount = amount
        self._date = date
        self._currency = currency
        self._description = description

    @property
    def amount(self):
        # Свойство для чтения суммы транзакции
        return self._amount

    @property
    def date(self):
        # Свойство для чтения даты транзакции
        return self._date

    @property
    def currency(self):
        # Свойство для чтения валюты транзакции
        return self._currency

    @property
    def usd_conversion_rate(self):
        # Свойство для чтения курса конверсии валюты к доллару
        return self._usd_conversion_rate

    @property
    def description(self):
        # Свойство для чтения описания транзакции
        return self._description

    @property
    def usd(self):
        # Свойство для чтения эквивалента транзакции в долларах
        return self._amount * self._usd_conversion_rate


class Account:
    def __init__(self, account_number, account_name):
        # Хранение данных о счете и транзакциях
        self.__account_number = account_number
        self.__account_name = account_name
        self.__transactions = []

    @property
    def account_number(self):
        # Свойство для чтения номера счета
        return self.__account_number

    @property
    def account_name(self):
        # Свойство для чтения названия счета
        return self.__account_name

    @account_name.setter
    def account_name(self, name):
        # Свойство для записи названия счета с проверкой длины
        if len(name) >= 4:
            self.__account_name = name
        else:
            raise ValueError("Account name should be at least 4 characters long.")

    def __len__(self):
        # Встроенная функция len() возвращает количество транзакций
        return len(self.__transactions)

    @property
    def balance(self):
        usd_transactions = [t for t in self.__transactions if t.currency == "USD"]
        return sum(t.amount for t in usd_transactions)

    @property
    def all_usd(self):
        # Свойство для проверки, все ли транзакции выполнены в долларах
        return all(t.currency == "USD" for t in self.__transactions)

    def apply(self, transaction):
        # Метод для добавления новой транзакции
        self.__transactions.append(transaction)

    def save(self):
        # Метод для сохранения данных счета
        data = {
            "account_number": self.__account_number,
            "account_name": self.__account_name,
            "transactions": self.__transactions,
        }
        file_name = self.__get_save_file_name()
        with open(file_name, "wb") as file:
            pickle.dump(data, file)

    def load(self):
        # Метод для загрузки данных счета
        file_name = self.__get_save_file_name()
        if os.path.exists(file_name):
            with open(file_name, "rb") as file:
                data = pickle.load(file)
                self.__account_number = data["account_number"]
                self.__account_name = data["account_name"]
                self.__transactions = data["transactions"]

    def __get_save_file_name(self):
        return os.path.join(
            os.path.expanduser("~"), "Desktop", f"{self.__account_number}.acc"
        )


# Создание нескольких транзакций
transaction1 = Transaction(amount=100, date="2023-01-01", currency="USD")
transaction2 = Transaction(amount=200, date="2023-02-01", currency="USD")
transaction3 = Transaction(amount=50, date="2023-03-01", currency="USD")

# Создание аккаунта с номером счета и названием
account = Account(account_number="1", account_name="My Account")

# Добавление транзакций в аккаунт
account.apply(transaction1)
account.apply(transaction2)
account.apply(transaction3)

account.save()

# Печать некоторой информации о счете и транзакциях
print(f"Account Number: {account.account_number}")
print(f"Account Name: {account.account_name}")
print(f"Number of Transactions: {len(account)}")
print(f"Balance: ${account.balance}")
print(f"All transactions in USD: {account.all_usd}")
