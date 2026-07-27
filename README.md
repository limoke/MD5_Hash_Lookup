## MD5 Hash Lookup Utility

A lightweight, full-stack web application designed for high-efficiency MD5 hash verification and relational data lookup.

## Project Overview

This application serves as a practical implementation of backend routing, database management, and client-server architecture. Developed to explore cryptographic hashing mechanisms and relational database querying, the system allows users to interactively query pre-indexed MD5 hash values through a structured web interface.

### Key Technical Components

* **Backend Core (`app.py`):** Built using Python and the Flask micro-framework to manage HTTP requests, routing, and server-side logic.
* **Database Management (`database.py` & `database.db`):** Implements SQLite for structured data persistence, optimized for rapid relational lookups and record retrieval.
* **Frontend Architecture (`templates/` & `static/`):** Utilizes HTML, CSS, and client-side assets to deliver a clean, responsive user interface.

---

## Technical Architecture

```text
MD5_Hash_Lookup/
│
├── app.py              # Flask server instance and route controllers
├── database.py         # Database connection logic and query execution
├── database.db         # SQLite relational data store
├── requirements.txt    # Project dependencies and environment specifications
├── static/             # Client-side stylesheets and UI assets
└── templates/          # HTML presentation templates

```

---

## Local Installation & Setup

To run this application locally, ensure you have Python installed, then follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/your-username/MD5_Hash_Lookup.git
cd MD5_Hash_Lookup

```


2. Install the required dependencies:
```bash
pip install -r requirements.txt

```


3. Initialize and run the application:
```bash
python app.py

```


4. Open your browser and navigate to `[http://127.0.0.1:5000](http://127.0.0.1:5000)`.
