#Expense Project

A simple data engineering pipeline built with Python, PostgreSQL, and Docker that ingests expense data from CSV files, validates it, stores it in a database, and allows querying through a CLI.


##Project Overview

This project demonstrates a basic data pipeline architecture:
Read expense data from CSV files
Validate records using Pydantic
Store data in PostgreSQL
Query and analyze data using CLI commands
Export data in tabular format


##Architecture

CSV Files
   │
   ▼
CSV Reader
   │
   ▼
Validation Layer (Pydantic)
   │
   ▼
PostgreSQL Database
   │
   ▼
CLI Commands
   │
   ▼
Tabular Output / Export


##Project Structure

expense_project
│
├── app
│   ├── cli.py
│   ├── ingestion
│   ├── validation
│   └── db
│   
│
├── data
│   └──expenses.csv
│
├── tests
│   ├──conftest.py
│   ├── test_csv_reader.py
│   └── test_validation.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── ARCHITECTURE.md
└── README.md


##Features

CSV data ingestion
Schema validation using Pydantic
Storage in PostgreSQL
CLI based analytics queries
Tabular output using tabulate
Containerized with Docker
Unit testing using pytest

