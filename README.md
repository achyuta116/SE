# Team Tantrashabhiyantran's ATM Simulator




An automated teller machine (ATM) is an electronic banking outlet that allows customers to complete basic transactions without the aid of a branch representative or teller. Anyone with a credit card or debit card can access cash at most ATMs. They are available 24/7.  ATMs are convenient, allowing consumers to perform quick self-service transactions such as deposits, cash withdrawals, bill payments, and transfers between accounts and even reviewing their loan applications. 

The aim is to design and implement an ATM simulator that simulates the function of a real ATM. These features can be done securely, individually without the hassle of going to a bank and having a wait period.


The ATM Simulator application should be accessible on it’s allotted machine only, and will support username authentication, balance inquiry, cash deposit, cash withdrawal, cheque withdrawal, loan application, loan payment and review, viewing and generating bills to the customer. 

Operators can exercise their right to shut down, reboot, disable, block ATM functions in case of an emergency or flaw in the machine. They can also generate the login and logout times for customers within a range of dates.

## How To
 1. Clone this repository and install dependencies `pip3 install -r requirements.txt`.
 2.  Start JSON server by running `npx json-server --watch data/database.json --port=3000`
 3.  Run `python main.py`
 


Customer as User

<img width="468" alt="image" src="https://user-images.githubusercontent.com/67890839/204074001-8d61753e-4705-4201-9361-dcbf7a18eb7d.png">

<img width="468" alt="image" src="https://user-images.githubusercontent.com/67890839/204074011-011d13b0-4368-4e89-b132-a79a60ca5cc0.png">


Operator as User

<img width="468" alt="image" src="https://user-images.githubusercontent.com/67890839/204074036-97aaf6ac-73bf-449f-b70d-5c8dfd4e9ce1.png">



