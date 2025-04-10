from faker import Faker
import json
fake = Faker()

all_fields = {
    "name": fake.name,
    "first_name": fake.first_name,
    "last_name": fake.last_name,
    "prefix": fake.prefix,
    "suffix": fake.suffix,
    "email": fake.email,
    "username": fake.user_name,
    "password": fake.password,
    "phone": fake.phone_number,
    "address": fake.address,
    "city": fake.city,
    "country": fake.country,
    "country_code": fake.country_code,
    "postcode": fake.postcode,
    "dob": lambda: fake.date_of_birth().isoformat(),
    "job": fake.job,
    "company": fake.company,
    "company_email": fake.company_email,
    "catch_phrase": fake.catch_phrase,
    "text": fake.text,
    "sentence": fake.sentence,
    "paragraph": fake.paragraph,
    "ipv4": fake.ipv4,
    "ipv6": fake.ipv6,
    "mac_address": fake.mac_address,
    "url": fake.url,
    "uri": fake.uri,
    "domain_name": fake.domain_name,
    "uuid": fake.uuid4,
    "color": fake.color_name,
    "hex_color": fake.hex_color,
    "rgb_color": fake.rgb_color,
    "safe_color": fake.safe_color_name,
    "credit_card_number": fake.credit_card_number,
    "credit_card_expire": fake.credit_card_expire,
    "credit_card_provider": fake.credit_card_provider,
    "ean13": lambda: fake.ean(length=13),
    "iban": fake.iban,
    "locale": fake.locale,
    "language_code": fake.language_code,
    "currency": fake.currency,
    "currency_code": fake.currency_code,
    "isbn10": fake.isbn10,
    "isbn13": fake.isbn13,
    "file_name": fake.file_name,
    "mime_type": fake.mime_type,
    "timezone": fake.timezone,
    "chrome_user_agent": fake.chrome,
    "firefox_user_agent": fake.firefox,
    "safari_user_agent": fake.safari,
    "user_agent": fake.user_agent,
    "ssn": fake.ssn,
    "license_plate": fake.license_plate,
    "latitude": fake.latitude,
    "longitude": fake.longitude,
}

def show_fields():
    print("\n Available fields:")
    print(",".join(sorted(all_fields.keys())))
    print("Type 'all' to select everyhting ro 'exist' to quit. \n")

def generated_data(selected_fields, count):
    data = []
    for _ in range(count):
        record = {field: all_fields[field]() for field in selected_fields}
        data.append(record)
    return data

def main():
    print("Welcome to the Fake Data Generator!")

    while True:
        show_fields()
        fields_input = input("Enter the fields you want to generate comma-separated, 'all' or 'exit'): ").strip().lower()

        if fields_input == "exit":
            print("Exiting the program.")
            break
        if fields_input == 'all':
            selected_fields = list(all_fields.keys())
        else:
            selected_fields = [f.strip() for f in fields_input.split(",") if f.strip() in all_fields]

        if not selected_fields:
            print("No valid fields selected. Try again. \n")
            continue

        try:
            count = int(input("How many records do you want ?"))
        except ValueError:
            print("That's not a number . Try again. \n")
            continue

        data = generated_data(selected_fields, count)
        print("\n Yourfake data: \n")
        print(json.dumps(data, indent=4))
        print("\n🚀 Ready for another round!\n" + "-" * 40)

if __name__ == "__main__":
    main()