import csv

def read_csv_as_dict(file_path):
    result = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, fieldnames=["company_code", "company_name", "market_cap", "price", "high", "low", "industry"])
        for row in csv_reader:
            result.append({
                "company_code": row["company_code"],
                "company_name": row["company_name"]
            })
    return result

# ファイルパスを指定
file_path = 'company_codes.csv'
data = read_csv_as_dict(file_path)
print(data)