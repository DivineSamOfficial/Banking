
from faker import Faker
from datetime import datetime, timedelta
import csv
import os
import random 


fake = Faker()
def id_generator(start=1):
    """
    Generates a sequence of unique identifiers starting from the given `start` value.
    Parameters:
        start (int, optional): The starting value of the sequence. Defaults to 1.
    Yields:
        int: The next identifier in the sequence.
    Example:
        >>> gen = id_generator(5)
        >>> next(gen)
        5
        >>> next(gen)
        6
        >>> next(gen)
        7
    """
    current = start
    while True:
        yield current
        current += 1


# id generators
customer_id_gen = id_generator()
date_id_gen = id_generator()
channel_id_gen = id_generator()
account_id_gen = id_generator()
transaction_type_id_gen = id_generator()
location_id_gen = id_generator()
currency_id_gen = id_generator()
investment_type_id_gen = id_generator()
loan_id_gen = id_generator()


def generate_dim_customer(num_records):
    """
    Generates a list of customer records with randomly generated data.
    Parameters:
        num_records (int): The number of customer records to generate.
    Returns:
        list: A list of dictionaries representing customer records. Each dictionary contains the following keys:
            - customer_id (int): The unique identifier for the customer.
            - first_name (str): The first name of the customer.
            - last_name (str): The last name of the customer.
            - email (str): The email address of the customer.
            - address (str): The address of the customer.
            - city (str): The city of the customer.
            - state (str): The state of the customer.
            - postal_code (str): The postal code of the customer.
            - phone_number (str): The phone number of the customer.
    """
    customers = []

    for _ in range(num_records):
        customer = {
            'customer_id': next(customer_id_gen),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'address': fake.address().replace('\n', ','),
            'city': fake.city(),
            'state': fake.state(),
            'postal_code': fake.postcode(),
            'phone_number': fake.phone_number(),
        }

        customers.append(customer)

    return customers

def generate_dim_date(start_year=2020, end_year=2024):
    """
    Generates a list of date records between the given start and end years.
    
    Args:
        start_year (int, optional): The starting year of the date range. Defaults to 2020.
        end_year (int, optional): The ending year of the date range. Defaults to 2024.
    
    Returns:
        list: A list of dictionaries representing date records. Each dictionary contains the following keys:
            - date_id (int): The unique identifier for the date.
            - date (str): The date in the format 'YYYY-MM-DD'.
            - day (int): The day of the month.
            - month (int): The month of the year.
            - year (int): The year.
            - week_day (int): The day of the week (1-7, where 1 is Monday and 7 is Sunday).
    """
    date_ls = []
    start_date = datetime(start_year, month=1, day=1)
    end_date = datetime(end_year, month=12, day=31)
    delta = timedelta(days=1)

    for i, day in enumerate(range((end_date - start_date).days+1), start=1):
        day_date = start_date + day * delta
        date_record = {
            'date_id': next(date_id_gen),
            'date': day_date.strftime('%Y-%m-%d'),
            'day': day_date.day,
            'month': day_date.month,
            'year': day_date.year,
            'week_day': day_date.weekday() + 1
        }

        date_ls.append(date_record)

    return date_ls

def generate_dim_channel():
    """
    Generates a list of channel records with unique identifiers and channel names.
    Returns:
        list: A list of dictionaries representing channel records. Each dictionary contains the following keys:
            - channel_id (int): The unique identifier for the channel.
            - channel_name (str): The name of the channel.
    """
    channels = []
    channel_names = ['Online', 'Mobile App', 'In-Store', 'ATM', 'Telephone']

    for name in channel_names:
        channel = {
            'channel_id': next(channel_id_gen),
            'channel_name': name
        }
        channels.append(channel)

    return channels

def generate_dim_account(num_records=100, customer_ids=None):
    accounts = []
    for _ in range(num_records):
        account = {
            'account_id': next(account_id_gen),
            'customer_id': random.choice(customer_ids),
            'account_number': fake.unique.random_int(min=1000000000, max=9999999999),
            'account_type': random.choice(['Savings', 'Checking', 'Investment']),
            'account_balance': round(random.uniform(0, 1000000), 2),
            'credit_score': random.randint(300, 850),
        }
        accounts.append(account)
    return accounts

def generate_dim_transaction_type():
    """
    Generates a list of transaction type records with unique identifiers and transaction type names.
    Returns:
        list: A list of dictionaries representing transaction type records. Each dictionary contains the following keys:
            - transaction_type_id (int): The unique identifier for the transaction type.
            - transaction_type_name (str): The name of the transaction type.
    Example:
        >>> generate_dim_transaction_type()
        [
            {
                'transaction_type_id': 1,
                'transaction_type_name': 'Deposit'
            },
            {
                'transaction_type_id': 2,
                'transaction_type_name': 'Withdrawal'
            },
            {
                'transaction_type_id': 3,
                'transaction_type_name': 'Transfer'
            },
            {
                'transaction_type_id': 4,
                'transaction_type_name': 'Payment'
            }
        ]
    """
    transaction_types = [
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Deposit'
        },
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Withdrawal'
        },
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Transfer'
        },
        {
            'transaction_type_id': next(transaction_type_id_gen),
            'transaction_type_name': 'Payment'
        }


    ]

    return transaction_types

def generate_dim_location(num_records=50):
    """
    Generates a list of location records with unique identifiers and location names.
    Returns:
        list: A list of dictionaries representing location records. Each dictionary contains the following keys:
            - location_id (int): The unique identifier for the location.
            - location_name (str): The name of the location.
    """
    locations = []
    for _ in range(num_records):
        location = {
            'location_id': next(location_id_gen),
            'city': fake.city(),
            'state': fake.state(),
            'country': fake.country(),
            'postal_code': fake.postcode()
        }
        locations.append(location)
    return locations

def generate_dim_currency():
    """
    Generates a list of currency records with unique identifiers and currency codes and names.
    
    Returns:
        list: A list of dictionaries representing currency records. Each dictionary contains the following keys:
            - currency_id (int): The unique identifier for the currency.
            - currency_code (str): The code of the currency.
            - currency_name (str): The name of the currency.
    """
    return [
        {
            'currency_id': next(currency_id_gen),
            'currency_code': 'USD',
            'currency_name': 'US Dollar'
        },
        {
            'currency_id': next(currency_id_gen),
            'currency_code': 'EUR',
            'currency_name': 'Euro'
        },
        {
            'currency_id': next(currency_id_gen),
            'currency_code': 'INR',
            'currency_name': 'Indian Rupee'
        }
    ]

def generate_dim_investment_type(num_records=5):
    """
    Generates a list of investment type records with unique identifiers and investment type names.
    
    Parameters:
        num_records (int, optional): The number of investment type records to generate. Defaults to 5.
    
    Returns:
        list: A list of dictionaries representing investment type records. Each dictionary contains the following keys:
            - investment_type_id (int): The unique identifier for the investment type.
            - investment_type_name (str): The name of the investment type.
    """
    investment_types = []

    for _ in range(num_records):
        investment_type = {
            'investment_type_id': next(investment_type_id_gen),
            'investment_type_name': fake.word().capitalize()+ 'Investment'
        }
        investment_types.append(investment_type)

    return investment_types

def generate_dim_loan(num_records=50): 
    """
    Generates a list of loan records.
    Args:
        num_records (int, optional): The number of loan records to generate. Defaults to 50.
    Returns:
        list: A list of loan records, where each record is a dictionary with the following keys:
            - 'loan_id' (int): The unique ID of the loan.
            - 'loan_type' (str): The type of the loan. Possible values are 'Mortgage', 'Personal', 'Auto', 'Student', 'Business', 'Other'.
            - 'loan_amount' (float): The amount of the loan.
            - 'interest_rate' (float): The interest rate of the loan.
    """
    loans = []

    for _ in range(num_records):
        loan = {
            'loan_id': next(loan_id_gen),
            'loan_type': random.choice(['Mortgage', 'Personal', 'Auto', 'Student', 'Business', 'Other']),
            'loan_amount': round(random.uniform(a=50, b=500000), 2),
            'interest_rate': round(random.uniform(a=1.5, b=10), 2),
        }
        loans.append(loan)

    return loans

def generate_fact_transaction(num_records, accounts, ls_dates, transactions_types, channels, locations, currencies):
    """
    Generates a list of fact transaction records with randomized values.
    Parameters:
        num_records (int): The number of fact transaction records to generate.
        accounts (list): A list of dictionaries representing account records.
        ls_dates (list): A list of dictionaries representing date records.
        transactions_types (list): A list of dictionaries representing transaction type records.
        channels (list): A list of dictionaries representing channel records.
        locations (list): A list of dictionaries representing location records.
        currencies (list): A list of dictionaries representing currency records.
    Returns:
        list: A list of dictionaries representing fact transaction records. Each dictionary contains the following keys:
            - transaction_id (int): The unique identifier for the transaction.
            - date_id (int): The identifier for the date of the transaction.
            - transaction_type_id (int): The identifier for the type of the transaction.
            - account_id (int): The identifier for the account associated with the transaction.
            - channel_id (int): The identifier for the channel through which the transaction occurred.
            - location_id (int): The identifier for the location associated with the transaction.
            - currency_id (int): The identifier for the currency used in the transaction.
            - transaction_amount (float): The amount of the transaction.
            - transaction_status (str): The status of the transaction. Possible values are 'Pending', 'Completed', or 'Failed'.
    """
    transactions = []
    for _ in range(num_records):
        transaction = {
            'transaction_id': fake.unique.random_int(min=1, max=100000),
            'date_id': random.choice(ls_dates)['date_id'],
            'transaction_type_id': random.choice(transactions_types)['transaction_type_id'],
            'account_id': random.choice(accounts)['account_id'],
            'channel_id': random.choice(channels)['channel_id'],
            'location_id': random.choice(locations)['location_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'transaction_amount': round(random.uniform(a=1.00, b=10000), 2),
            'transaction_status': random.choice(['Pending', 'Completed', 'Failed']),
        }
        transactions.append(transaction)
    return transactions

def generate_fact_investement(num_records, accounts, ls_dates, investment_types, locations, currencies):
    """
    Generates a list of investment records with randomized values.
    
    Parameters:
        num_records (int): The number of investment records to generate.
        accounts (list): A list of dictionaries representing account records.
        ls_dates (list): A list of dictionaries representing date records.
        investment_types (list): A list of dictionaries representing investment type records.
        locations (list): A list of dictionaries representing location records.
        currencies (list): A list of dictionaries representing currency records.
    
    Returns:
        list: A list of dictionaries representing investment records. Each dictionary contains the following keys:
            - investment_id (int): The unique identifier for the investment.
            - date_id (int): The identifier for the date of the investment.
            - investment_type_id (int): The identifier for the type of the investment.
            - account_id (int): The identifier for the account associated with the investment.
            - location_id (int): The identifier for the location associated with the investment.
            - currency_id (int): The identifier for the currency used in the investment.
            - investment_amount (float): The amount of the investment.
            - investment_return (float): The return of the investment.
    """
    investments = []
    for _ in range(num_records):
        investment = {
            'investment_id': fake.unique.random_int(min=1, max=100000),
            'date_id': random.choice(ls_dates)['date_id'],
            'investment_type_id': random.choice(investment_types)['investment_type_id'],
            'account_id': random.choice(accounts)['account_id'],
            'location_id': random.choice(locations)['location_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'investment_amount': round(random.uniform(a=1000.00, b=10000), 2),
            'investment_return': round(random.uniform(a=-5000, b=15000), 2)
        }
        investments.append(investment)
    return investments

def generate_fact_loan(num_records, accounts, ls_dates, loans, locations, currencies):
    """
    Generates a list of loan records with randomized values.
    Parameters:
        num_records (int): The number of loan records to generate.
        accounts (list): A list of dictionaries representing account records.
        ls_dates (list): A list of dictionaries representing date records.
        loans (list): A list of dictionaries representing loan records.
        locations (list): A list of dictionaries representing location records.
        currencies (list): A list of dictionaries representing currency records.
    Returns:
        list: A list of dictionaries representing loan records. Each dictionary contains the following keys:
            - loan_fact_id (int): The unique identifier for the loan.
            - date_id (int): The identifier for the date of the loan.
            - loan_id (int): The identifier for the loan type.
            - account_id (int): The identifier for the account associated with the loan.
            - location_id (int): The identifier for the location associated with the loan.
            - currency_id (int): The identifier for the currency used in the loan.
            - loan_amount (float): The amount of the loan.
            - loan_status (str): The status of the loan. Possible values are 'Pending', 'Approved', or 'Rejected'.
    """
    fact_loans = []
    for _ in range(num_records):
        loan = {
            'loan_fact_id': fake.unique.random_int(min=1, max=100000),
            'date_id': random.choice(ls_dates)['date_id'],
            'loan_id': random.choice(loans)['loan_id'],
            'account_id': random.choice(accounts)['account_id'],
            'location_id': random.choice(locations)['location_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'loan_amount': round(random.uniform(a=5000, b=500000), 2),
            'loan_status': random.choice(['Pending','Approved', 'Rejected'])
        }
        fact_loans.append(loan)
    return fact_loans

def generate_fact_customer_interactions(num_records, customers, ls_dates, channels, locations):
    """
    Generates a list of fact customer interaction records with randomized values.
    Parameters:
        num_records (int): The number of fact customer interaction records to generate.
        customers (list): A list of dictionaries representing customer records.
        ls_dates (list): A list of dictionaries representing date records.
        channels (list): A list of dictionaries representing channel records.
        locations (list): A list of dictionaries representing location records.
    Returns:
        list: A list of dictionaries representing fact customer interaction records. Each dictionary contains the following keys:
            - interaction_id (int): The unique identifier for the interaction.
            - date_id (int): The identifier for the date of the interaction.
            - customer_id (int): The identifier for the customer associated with the interaction.
            - channel_id (int): The identifier for the channel through which the interaction occurred.
            - location_id (int): The identifier for the location associated with the interaction.
            - interaction_type (str): The type of the interaction. Possible values are 'Phone', 'Email', 'Chat', 'Website', 'Social Media', or 'In-Person'.
            - interaction_rating (int): The rating of the interaction. Values range from 1 to 5.
    """
    interactions = []
    for _ in range(num_records):
        interaction = {
            'interaction_id': fake.unique.random_int(min=1, max=100000),
            'date_id': random.choice(ls_dates)['date_id'],
            'customer_id': random.choice(customers)['customer_id'],
            'channel_id': random.choice(channels)['channel_id'],
            'location_id': random.choice(locations)['location_id'],
            'interaction_type': random.choice(['Phone', 'Email', 'Chat', 'Website', 'Social Media', 'In-Person']),
            'interaction_rating': random.randint(a=1, b=5)
        }
        interactions.append(interaction)
    return interactions

def generate_fact_daily_balances(num_records, accounts, ls_dates, currencies):
    daily_balances = []
    for _ in range(num_records):
        daily_balance = {
            'balance_id': fake.unique.random_int(min=1, max=100000),
            'date_id': random.choice(ls_dates)['date_id'],
            'account_id': random.choice(accounts)['account_id'],
            'currency_id': random.choice(currencies)['currency_id'],
            'opening_balance': round(random.uniform(a=0, b=1000000), 2),
            'closing_balance': round(random.uniform(a=0, b=1000000), 2),
            'average_balance': round((random.uniform(0, 1000000) + random.uniform(0, 1000000)), 2) / 2
        }
        daily_balances.append(daily_balance)
    return daily_balances



# def write_to_csv(data, file_name):
#     if not data:
#         return #exit if data is empty
#     keys = data[0].keys()
#     with open(file_name, 'w', newline='', encoding='utf-8') as output_file:
#         dict_writer = csv.DictWriter(output_file, fieldnames=keys, delimiter='|')
#         dict_writer.writeheader()
#         dict_writer.writerows(data)
def write_to_csv(data, file_name, folder_name='data'):
    if not data:
        return  # exit if data is empty
    keys = data[0].keys()
    file_path = os.path.join(folder_name, file_name)
    os.makedirs(folder_name, exist_ok=True)  # Create the folder if it doesn't exist
    with open(file_path, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys, delimiter='|')
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main():
    customers = generate_dim_customer(100)
    ls_dates = generate_dim_date(2020, 2024)
    channels = generate_dim_channel()
    transactions_types = generate_dim_transaction_type()
    locations = generate_dim_location(50)
    currencies = generate_dim_currency()
    accounts = generate_dim_account(num_records=100, customer_ids=[customer['customer_id'] for customer in customers])
    investment_types = generate_dim_investment_type()
    loans = generate_dim_loan(50)

    #write to csv
    write_to_csv(customers, file_name='customers.csv')
    write_to_csv(ls_dates, file_name='dates.csv')
    write_to_csv(channels, file_name='channels.csv')
    write_to_csv(transactions_types, file_name='transaction_types.csv')
    write_to_csv(locations, file_name='locations.csv')
    write_to_csv(currencies, file_name='currencies.csv')
    write_to_csv(accounts, file_name='accounts.csv')
    write_to_csv(investment_types, file_name='investment_types.csv')
    write_to_csv(loans, 'loans.csv')

    #generate fact tables
    transactions = generate_fact_transaction(10000, accounts, ls_dates, transactions_types, channels, locations, currencies)
    investments = generate_fact_investement(10000, accounts, ls_dates, investment_types, locations, currencies)
    fact_loans = generate_fact_loan(10000, accounts, ls_dates, loans, locations, currencies)
    interactions = generate_fact_customer_interactions(10000, customers, ls_dates, channels, locations)
    daily_balances = generate_fact_daily_balances(10000, accounts, ls_dates, currencies)

    #write fact tables to csv
    write_to_csv(transactions, file_name='fact_transactions.csv')
    write_to_csv(investments, file_name='fact_investments.csv')
    write_to_csv(fact_loans, file_name='fact_loans.csv')
    write_to_csv(interactions, file_name='fact_customer_interactions.csv')
    write_to_csv(daily_balances, file_name='fact_daily_balances.csv')




if __name__ == "__main__":
    main()


