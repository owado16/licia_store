<<<<<<< HEAD
# Licia's Store

Welcome to the Licia's Store repository! This is an e-commerce platform for Greek yogurt and granola, offering a variety of features such as product listings, admin management, and more.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3
- pip
- Virtual environment (optional but recommended)

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. **Clone the Repository**
   git clone https://github.com/thisishaykins/licia_store.git

# Get Started
To setup the PyShop project, here is the following guidelines:
* Clone the repository <code>git clone https://github.com/owado16/licia_store.git</code>
* Open Project folder on terminal 
* Prepare your virtual environment <code>python3 -m venv venv</code> 
* Activate your virtual environment <code>source env/bin/activate</code>
* Install your requirements.txt file <code>pip install -r requirements.txt</code>
* Create migrations using <code>python3 manage.py makemigrations</code> 
* Run migrations <code>python3 manage.py migrate</code>
* Start your dev server with <code>python3 manage.py runserver</code>
* Visit your App using <code>http://127.0.0.1:8000/</code>
* Create super user to access admin dashboard using <code> python3 manage.py createsuperuser</code>
* Follow the prompts after <code>Username: , Email address: , Password: , Password (again): </code>
* Visit Admin Page using <code>http://127.0.0.1:8000/admin</code> and login with the credentials created above.
* Add Products under the <b>Products</b> Menu, Add Offers also.
* Visit Products Page using <code>http://127.0.0.1:8000/products/</code>
* Visit New Arrival (Products) Page using <code>http://127.0.0.1:8000/products/new</code>




2. **Navigate to Project Directory**
   cd licia_store
3. **Prepare Your Virtual Environment**
   python3 -m venv venv
   
4. **Activate Your Virtual Environment**
- For Unix or MacOS:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  .\venv\Scripts\activate
  ```

5. **Install Requirements**
pip install -r requirements.txt


6. **Create Migrations**
python3 manage.py makemigrations


7. **Run Migrations**
python3 manage.py migrate


8. **Create Superuser**
python3 manage.py createsuperuser

Follow the prompts to create an admin user.

9. **Start Development Server**
python3 manage.py runserver


10. **Visit the Application**
 - Home Page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
 - Admin Dashboard: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

 Log in with the superuser credentials to access the admin dashboard.

### Using the Application

- **Add Products**: Navigate to the admin dashboard and select the Products menu to add products.
- **Add Offers**: In the admin dashboard, you can also add promotional offers.
- **View Products**: Access the products page at [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/)
- **View New Arrivals**: See new products at [http://127.0.0.1:8000/products/new](http://127.0.0.1:8000/products/new)

### Extending the Codebase

If you wish to extend or contribute to the project, please ensure you adhere to the following guidelines:
- Fork the repository
- Create a new branch for your feature (`git checkout -b feature/AmazingFeature`)
- Commit your changes (`git commit -am 'Add some AmazingFeature'`)
- Push to the branch (`git push origin feature/AmazingFeature`)
- Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
   

## Live demo of the app can be see 
here https://licia-store.onrender.com



# licia_store
>>>>>>> 24d2450c805adfad4463dd07fd69e0e3263a82db