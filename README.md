# 📒 ContactBook CLI

A simple command-line contact book tool written in Python. Easily add, list, and delete contacts using a JSON file for persistent storage.

---

## 🚀 Features

- Add new contacts with name, phone number, and birthday.
- List all saved contacts in the contact book.
- Delete a contact by name.
- Persistent storage using a `contactbook.json` file.
- Runs from anywhere using standard CLI flags.

---

## 🛠 Requirements

- Python 3.6+

---

## 📦 Installation

Clone the repo and navigate into the project folder:

```bash
git clone https://github.com/yourusername/contactbook-cli.git
cd contactbook-cli
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

---

## 🗂 Data Storage

Contacts are stored in a `contactbook.json` file in the same directory. The file is automatically created on first run.

Each contact includes:
- `name`
- `phone`
- `birthday`

---

## 💡 Future Ideas

- Show upcoming birthdays.
- Edit contacts.
- Add contact groups or tags.
- Export to CSV.

---

## 👤 Author

Created by Caelan Roberge-Toll as a learning project.

---

## 📄 License

MIT License (or insert your preferred license).
