class Hotel:
    def __init__(self):
        self.rooms = {}
        self.customers = {}
        self.employees = {}

    # ---------------- ROOM SECTION ----------------
    def add_room(self):
        room_no = int(input("Enter Room Number: "))
        price_1day = int(input("Enter Price for 1 Day: "))
        price_30day = int(input("Enter Price for 30 Days: "))

        self.rooms[room_no] = {
            "customer_id": None,
            "price_1day": price_1day,
            "price_30day": price_30day
        }
        print("Room Added Successfully!")

    def update_room(self):
        room_no = int(input("Enter Room Number to Update: "))
        if room_no in self.rooms:
            self.rooms[room_no]["price_1day"] = int(input("New 1 Day Price: "))
            self.rooms[room_no]["price_30day"] = int(input("New 30 Day Price: "))
            print("Room Updated!")
        else:
            print("Room Not Found!")

    def delete_room(self):
        room_no = int(input("Enter Room Number to Delete: "))
        if room_no in self.rooms:
            del self.rooms[room_no]
            print("Room Deleted!")
        else:
            print("Room Not Found!")

    def show_rooms(self):
        print("\nRoom Details:")
        for r, d in self.rooms.items():
            status = "Available" if d["customer_id"] is None else "Booked"
            print(f"Room {r} | {status} | 1 Day: {d['price_1day']} | 30 Days: {d['price_30day']}")

    # ---------------- CUSTOMER SECTION ----------------
    def add_customer(self):
        cid = input("Customer ID: ")
        name = input("Customer Name: ")
        city = input("City: ")
        business = input("Business: ")

        self.customers[cid] = {
            "name": name,
            "city": city,
            "business": business
        }
        print("Customer Added!")

    def show_customers(self):
        print("\nCustomer List:")
        for cid, c in self.customers.items():
            print(cid, c)

    # ---------------- EMPLOYEE SECTION ----------------
    def add_employee(self):
        eid = input("Employee ID: ")
        name = input("Employee Name: ")
        city = input("City: ")
        salary = int(input("Salary: "))

        self.employees[eid] = {
            "name": name,
            "city": city,
            "salary": salary
        }
        print("Employee Added!")

    def show_employees(self):
        print("\nEmployee List:")
        for eid, e in self.employees.items():
            print(eid, e)

    # ---------------- BOOKING SECTION ----------------
    def book_room(self):
        room_no = int(input("Enter Room Number: "))
        cid = input("Enter Customer ID: ")

        if room_no in self.rooms and cid in self.customers:
            if self.rooms[room_no]["customer_id"] is None:
                self.rooms[room_no]["customer_id"] = cid
                print("Room Booked Successfully!")
            else:
                print("Room Already Booked!")
        else:
            print("Invalid Room or Customer ID")

    def checkout(self):
        room_no = int(input("Enter Room Number: "))
        if room_no in self.rooms and self.rooms[room_no]["customer_id"]:
            days = int(input("Number of Days Stayed: "))
            if days >= 30:
                bill = self.rooms[room_no]["price_30day"]
            else:
                bill = days * self.rooms[room_no]["price_1day"]

            cid = self.rooms[room_no]["customer_id"]
            print(f"Customer: {self.customers[cid]['name']}")
            print(f"Total Bill: Rs {bill}")

            self.rooms[room_no]["customer_id"] = None
            print("Checkout Successful!")
        else:
            print("Room Empty or Invalid!")

# ---------------- MAIN PROGRAM ----------------
hotel = Hotel()

while True:
    print("\n---- HOTEL MANAGEMENT SYSTEM ----")
    print("1. Add Room")
    print("2. Update Room")
    print("3. Delete Room")
    print("4. Show Rooms")
    print("5. Add Customer")
    print("6. Show Customers")
    print("7. Add Employee")
    print("8. Show Employees")
    print("9. Book Room")
    print("10. Checkout")
    print("11. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        hotel.add_room()
    elif choice == "2":
        hotel.update_room()
    elif choice == "3":
        hotel.delete_room()
    elif choice == "4":
        hotel.show_rooms()
    elif choice == "5":
        hotel.add_customer()
    elif choice == "6":
        hotel.show_customers()
    elif choice == "7":
        hotel.add_employee()
    elif choice == "8":
        hotel.show_employees()
    elif choice == "9":
        hotel.book_room()
    elif choice == "10":
        hotel.checkout()
    elif choice == "11":
        print("Thank You! Project Closed.")
        break
    else:
        print("Invalid Choice!")
