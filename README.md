# 📒 ContactBook CLI

A simple command-line contact book tool written in Python. Easily add, list, and delete contacts using a JSON file for persistent storage.

---

## 🚀 Features

- Add new contacts with name, phone number, and birthday.
- List all saved contacts in the contact book.
- Delete a contact by name.
- View upcoming birthdays within a specified number of days.
- Persistent storage using a `contactbook.json` file.
- Intelligent date parsing for birthdays.
- JSON-based data serialization and deserialization.

---

## 🛠 Requirements

- Python 3.6+
- `python-dateutil` library for advanced date parsing

---

## 📦 Installation

Clone the repo and navigate into the project folder:

```bash
git clone https://github.com/yourusername/contactbook-cli.git
cd contactbook-cli
```

Install the required dependency:

```bash
pip install python-dateutil
```

(If you're not using Git, just download the `.py` file.)

---

## 📖 Usage

Run the script using Python:

```bash
python3 contactbook.py <command> [options]
```

### ➕ Add a Contact

```bash
python3 contactbook.py add --name "Alice" --phone "123-456-7890" --birthday "1990-01-01"
```

### 📋 List All Contacts

```bash
python3 contactbook.py list
```

### ❌ Delete a Contact

```bash
python3 contactbook.py delete --name "Alice"
```

### 🎂 View Upcoming Birthdays

```bash
python3 contactbook.py nextbirthday --days 30
```

This will show all contacts with birthdays in the next 30 days.

---

## 🗂 Data Storage

Contacts are stored in a `contactbook.json` file in the same directory. The file is automatically created on first run.

Each contact includes:
- `name`
- `phone`
- `birthday`

---

## 💡 Future Ideas

- Edit contacts.
- Add contact groups or tags.
- Export to CSV.
- Birthday reminders and notifications.

---

## 👤 Author

Created by Caelan Roberge-Toll as a learning project.

---

## 📄 License

MIT License (or insert your preferred license).
