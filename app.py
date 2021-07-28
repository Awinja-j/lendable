import sys
import csv

def main(transactions_csv_file_path: str, n: int) -> list:
    best_customers = dict()
    all_customer = list()
    
    file_content = open(transactions_csv_file_path, 'r')
    file = csv.DictReader(file_content)

    for col in file:
        y = col['customer_id']

        all_customer.append(y)

    for customer in all_customer:
        count_customer = all_customer.count(customer)
        if count_customer not in best_customers.keys():
            best_customers[customer]=count_customer

    j = {k: v for k, v in sorted(best_customers.items(), key=lambda item: item[1], reverse=True)}

    best_customer_keys = list(j.keys())

    best_customer_keys = list(best_customer_keys[:n])

    return best_customer_keys

if __name__ == '__main__':
    print(main(str(sys.argv[1]), int(sys.argv[2])))