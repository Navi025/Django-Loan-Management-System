# Loan Management System

## Overview
The Loan Management System (LMS) is a web-based application for managing loans, from applications to repayments. It streamlines processes for administrators, employees, and users.

## Features
### User Roles
- **Admin**: Manages users, loans, assets, roles, products, wallets, messages.
- **Employee**: Manages loan applications, borrower info, repayments.
- **User**: Applies for loans, views status, manages info.

### Functionalities
1. **User Registration and Authentication**
   - Users register and log in.
   - Admins manage user accounts.
2. **Dashboard**
   - Displays open loans, collections, pending loans, clients.
   - Access to borrowers, assets, loans, roles, products, wallets, messages.
3. **Loan Management**
   - Users apply for loans.
   - Employees review, approve, manage disbursements.
   - Admins oversee all activities.
4. **Borrower Management**
   - Detailed borrower info.
   - CRUD operations.
5. **Assets Management**
   - Manage assets linked to loans.
6. **Role Management**
   - Define and assign roles.
7. **Product Management**
   - Manage loan products, terms.
8. **Wallet and Repayments**
   - Track repayments, manage wallets.
9. **Messaging System**
   - Built-in communication feature.

## Installation
### Prerequisites
- Python 3.x
- Django 3.x
- Dependencies in `requirements.txt`

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/loan-management-system.git
   cd loan-management-system
   ```
2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```sh
   python manage.py runserver
   ```
7. **Access the application**
   Navigate to `http://127.0.0.1:8000`

## Usage
### URLs for Key Pages
- **Registration**: `/accounts/register/`
- **User Dashboard**: `/dashboard/`
- **Loan Application**: `/loans/apply/`
- **Admin Dashboard**: `/admin/`
- **Loan Review**: `/loans/review/`

### Workflow
1. **User Registration**
   - Users register and log in.
2. **Loan Application**
   - Users apply for loans.
3. **Loan Review and Approval**
   - Employees review, approve/reject applications.
4. **Loan Disbursement**
   - Approved loans disbursed, users notified.
5. **Repayments and Collections**
   - Users repay loans, system tracks collections.

### Example Usage
- **Admin**: Manages users, loans, assets, roles.
- **Employee**: Processes applications, manages borrower info.
- **User**: Applies for loans, manages repayments.

## Contributing
Contributions welcome! Fork the repository and create a pull request.
