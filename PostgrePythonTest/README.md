# PostgreSQL Connection Example

This repository contains a simple Python script that demonstrates how to connect to a PostgreSQL database using the psycopg2 library. The script fetches the first user from a table named users in the DBSchema schema and prints the result.

## Prerequisites
Python 3.6 or later installed on your system.
Access to a PostgreSQL database.
psycopg2 library installed. You can install it using pip:

```bash
pip install psycopg2
```
Alternatively, for the binary version, which includes necessary binary dependencies:

```bash
pip install psycopg2-binary
```

## Installation
Clone this repository to your local machine.
Navigate to the project directory.
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
Before running the script, ensure you have the proper database connection details in the config.py file. This includes the host, user, password, port, and database name.
In the config.py file replace password with the actual password of your database.

