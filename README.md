# CarMart - Pre-Owned Vehicle Marketplace & Rental Service

Welcome to **CarMart**, a comprehensive web application built with Flask that allows users to browse, search, and explore pre-owned cars for sale, as well as cab rentals and bus reservations. It aims to make buying, renting, and booking vehicles easy, transparent, and accessible.

---

## About The Project

CarMart is designed for users looking to purchase reliable pre-owned vehicles or book cabs and buses conveniently online. It offers:

- A curated list of verified pre-owned cars with detailed specs, photos, and pricing
- Cab rental options for local and outstation trips
- Bus reservation system for group travels and tours
- A simple, clean, and responsive UI to ensure smooth browsing on desktop and mobile
- Admin dashboard for easy vehicle inventory and rental management

This project uses:

- Flask framework with SQLAlchemy ORM and Flask-Migrate for database management
- SQLite for local development (or any SQL database for production)
- Python 3 with Bootstrap CSS for UI styling

---

## Features

### For Users

- Browse available pre-owned cars with photos, specifications, and prices
- Filter cars by brand, model, price, and more (planned)
- View cab rental packages, routes, and pricing
- Reserve cabs or buses by contacting via phone/WhatsApp links
- Read FAQs and customer reviews
- Contact support through a simple contact form

### For Admins

- Add, update, or delete vehicle listings easily via the admin dashboard
- Manage cab rental and bus reservation entries
- Monitor inquiries and customer messages
- Use Flask-Migrate for smooth database schema updates

---

## How It Works

1. **Explore Listings**: Users can view all available pre-owned cars or rental vehicles.
2. **Select Vehicle**: Click on any vehicle card for detailed info and contact options.
3. **Book/Enquire**: Users can call or message the number displayed to book or ask questions.
4. **Admin Management**: Admins log into the dashboard to update listings and respond to customers.

---

## Tech Stack

- Backend: Python, Flask, SQLAlchemy, Flask-Migrate
- Database: SQLite (local dev) / PostgreSQL (production-ready)
- Frontend: HTML, CSS, Bootstrap 5, Bootstrap Icons
- Deployment: Fly.io (recommended for persistence)
- Optional: Docker for containerization

---

## Installation and Setup

1. Clone the repo:

    ```bash
    git clone https://github.com/yourusername/carmart.git
    cd carmart
    ```

2. Create virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Initialize database and apply migrations:

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

4. Run the Flask app locally:

    ```bash
    flask run
    ```

5. Open `http://127.0.0.1:5000` in your browser.

---

## Future Plans

- Add user authentication & profiles  
- Implement advanced search and filter options  
- Integrate online booking/payment gateway  
- Add real-time availability for rentals  
- Support multi-language interface  
- Deploy on cloud with PostgreSQL for scalability

---

## Contributing

Contributions are welcome! Feel free to fork the repo, make improvements, and submit pull requests.

---

## Contact

Created and maintained by **Alakhya Sarkar**  
Email: alakhyasarkar735216@gmail.com
LinkedIn: [linkedin.com/in/alakhya-sarkar](https://linkedin.com/in/alakhya-sarkar)  

---

Thank you for checking out CarMart — your one-stop shop for used cars and rentals! 🚗🚌

