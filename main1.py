import mysql.connector
import streamlit as st

# establish connection to SQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="BankManager"
)

mycursor = mydb.cursor()
print("connection established")

valid_username = "bank_manager"
valid_password = "bank_password"

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def authenticate(username, password):
    if username!=valid_username and password!=valid_password:
        st.warning("Invalid Login Credentials")
    elif username!=valid_username:
        st.warning("Invalid Username")
    elif password!=valid_password:
        st.warning("Invalid Password")
    else:
        return username == valid_username and password == valid_password

def display_bank_management_options(session_state):
        # Display choices to the user
        option = st.sidebar.selectbox("Select an option", ("Customer", "Branch", "Loan", "Transaction", "Accounts", "Employee", "Mobile"))
    #---------------------------------------------------------------------------------------

        # Perform selected CRUD operations or other operations
        if option == "Customer":
            st.subheader("Customer CRUD Operations")
            operation = st.radio("Select Operation", ("Create Customer", "Read Customers", "Update Customer", "Delete Customer"))

            if operation == "Create Customer":
                customer_id = st.text_input("Enter Customer ID")
                customer_name = st.text_input("Enter Customer Name")
                customer_address = st.text_input("Enter Customer Address")
                customer_email = st.text_input("Enter Customer Email")

                if st.button("Create Customer"):
                    # Create a new customer
                    sql = "INSERT INTO Customer (CID, Cname, Address, Email) VALUES (%s, %s, %s, %s)"
                    val = (customer_id, customer_name, customer_address, customer_email)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Customer record has been inserted successfully")

            elif operation == "Read Customers":
                # Read all customers
                mycursor.execute("SELECT * FROM Customer")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Customer":
                # Update a customer by ID
                customer_id_to_update = st.text_input("Enter Customer ID to update")
                new_customer_name = st.text_input("Enter new Customer Name")
                new_customer_address = st.text_input("Enter new Customer Address")
                new_customer_email = st.text_input("Enter new Customer Email")

                if st.button("Update Customer"):
                    # Check if any field is updated
                    if new_customer_name or new_customer_address or new_customer_email:
                        # Update a customer by ID
                        sql = "UPDATE Customer SET Cname=%s, Address=%s, Email=%s WHERE CID=%s"
                        val = (new_customer_name, new_customer_address, new_customer_email, int(customer_id_to_update))
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Customer record has been updated successfully")
                    else:
                        st.warning("No updates provided. Please enter new values.")

            elif operation == "Delete Customer":
                # Delete a customer by ID
                customer_id_to_delete = st.text_input("Enter Customer ID to delete")

                if st.button("Delete Customer"):
                    sql = "DELETE FROM Customer WHERE CID=%s"
                    val = (int(customer_id_to_delete),)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Customer record has been deleted successfully")

    #------------------------------------------------------------------------------
    # Bank CRUD Operations
        elif option == "Bank":
            st.subheader("Bank CRUD Operations")
            
            operation = st.radio("Select Operation", ("Create Bank", "Read Banks", "Update Bank", "Delete Bank"))

            if operation == "Create Bank":
                # Create a new bank
                bank_id = st.text_input("Enter Bank ID")
                bank_name = st.text_input("Enter Bank Name")
                bank_location = st.text_input("Enter Bank Location")

                if st.button("Create Bank"):
                    # Create a new bank
                    sql = "INSERT INTO Bank (ID, Bname, Location) VALUES (%s, %s, %s)"
                    val = (bank_id, bank_name, bank_location)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Bank record has been inserted successfully")

                    # Trigger for logging the create operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Bank', 'Create')")
                    # mydb.commit()

            elif operation == "Read Banks":
                # Read all banks
                mycursor.execute("SELECT * FROM Bank")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Bank":
                # Update a bank by ID
                bank_id_to_update = st.text_input("Enter Bank ID to update")
                new_bank_name = st.text_input("Enter new Bank Name")
                new_bank_location = st.text_input("Enter new Bank Location")

                if st.button("Update Bank"):
                    # Update a bank by ID
                    sql = "UPDATE Bank SET Bname=%s, Location=%s WHERE ID=%s"
                    val = (new_bank_name, new_bank_location, bank_id_to_update)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Bank record has been updated successfully")

                    # Trigger for logging the update operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Bank', 'Update')")
                    # mydb.commit()

            elif operation == "Delete Bank":
                # Delete a bank by ID
                bank_id_to_delete = st.text_input("Enter Bank ID to delete")

                if st.button("Delete Bank"):
                    sql = "DELETE FROM Bank WHERE ID=%s"
                    val = (bank_id_to_delete,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Bank record has been deleted successfully")

                    # Trigger for logging the delete operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Bank', 'Delete')")
                    # mydb.commit()
    #------------------------------------------------------------------------------------------------
        # Loan CRUD Operations
        elif option == "Loan":
            st.subheader("Loan CRUD Operations")

            operation = st.radio("Select Operation", ("Create Loan", "Read Loans", "Update Loan", "Delete Loan"))

            if operation == "Create Loan":
                # Create a new loan
                loan_id = st.text_input("Enter Loan ID")
                customer_id = st.text_input("Enter Customer ID")
                loan_amount = st.text_input("Enter Loan Amount")
                loan_type = st.text_input("Enter Loan Type")

                if st.button("Create Loan"):
                    # Create a new loan
                    sql = "INSERT INTO Loan (LID, CID, Amount, L_Type) VALUES (%s, %s, %s, %s)"
                    val = (loan_id, customer_id, loan_amount, loan_type)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Loan record has been inserted successfully")

                    # Trigger for logging the create operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Loan', 'Create')")
                    # mydb.commit()

            elif operation == "Read Loans":
                # Read all loans
                mycursor.execute("SELECT * FROM Loan")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Loan":
                # Update a loan by ID
                loan_id_to_update = st.text_input("Enter Loan ID to update")
                new_loan_amount = st.text_input("Enter new Loan Amount")
                new_loan_type = st.text_input("Enter new Loan Type")

                if st.button("Update Loan"):
                    # Update a loan by ID
                    sql = "UPDATE Loan SET Amount=%s, L_Type=%s WHERE LID=%s"
                    val = (new_loan_amount, new_loan_type, loan_id_to_update)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Loan record has been updated successfully")

                    # Trigger for logging the update operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Loan', 'Update')")
                    # mydb.commit()

            elif operation == "Delete Loan":
                # Delete a loan by ID
                loan_id_to_delete = st.text_input("Enter Loan ID to delete")

                if st.button("Delete Loan"):
                    sql = "DELETE FROM Loan WHERE LID=%s"
                    val = (loan_id_to_delete,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Loan record has been deleted successfully")

                    # Trigger for logging the delete operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Loan', 'Delete')")
                    # mydb.commit()
    #------------------------------------------------------------------------------------------------
        # Transaction CRUD Operations
        elif option == "Transaction":
            st.subheader("Transaction CRUD Operations")

            operation = st.radio("Select Operation", ("Create Transaction", "Read Transactions", "Update Transaction", "Delete Transaction"))

            if operation == "Create Transaction":
                # Create a new transaction
                transaction_id = st.text_input("Enter Transaction ID")
                amount = st.text_input("Enter Transaction Amount")
                account_number = st.text_input("Enter Account Number")

                # Use a radio button for transaction type
                transaction_type = st.radio("Select Transaction Type", ('REM', 'INS'))

                if st.button("Create Transaction"):
                    # Create a new transaction
                    sql = "INSERT INTO Transactions (TID, Amount, ANO, T_Type) VALUES (%s, %s, %s, %s)"
                    val = (transaction_id, amount, account_number, transaction_type)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Transaction record has been inserted successfully")

                    # Trigger for logging the create operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Transaction', 'Create')")
                    # mydb.commit()

            elif operation == "Read Transactions":
                # Read all transactions
                mycursor.execute("SELECT * FROM Transactions")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Transaction":
                # Update a transaction by ID
                transaction_id_to_update = st.text_input("Enter Transaction ID to update")
                new_amount = st.text_input("Enter new Transaction Amount")
                new_account_number = st.text_input("Enter new Account Number")
                
                # Use a radio button for new transaction type
                new_transaction_type = st.radio("Select new Transaction Type", ('REM', 'INS'))

                if st.button("Update Transaction"):
                    # Update a transaction by ID
                    sql = "UPDATE Transactions SET Amount=%s, ANO=%s, T_Type=%s WHERE TID=%s"
                    val = (new_amount, new_account_number, new_transaction_type, transaction_id_to_update)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Transaction record has been updated successfully")

                    # Trigger for logging the update operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Transaction', 'Update')")
                    # mydb.commit()

            elif operation == "Delete Transaction":
                # Delete a transaction by ID
                transaction_id_to_delete = st.text_input("Enter Transaction ID to delete")

                if st.button("Delete Transaction"):
                    # Delete a transaction by ID
                    sql = "DELETE FROM Transactions WHERE TID=%s"
                    val = (transaction_id_to_delete,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Transaction record has been deleted successfully")

                    # Trigger for logging the delete operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Transaction', 'Delete')")
                    # mydb.commit()



    #---------------------------------------------------------------------------------------------
        # Account CRUD Operations
        elif option == "Accounts":
            st.subheader("Account CRUD Operations")

            operation = st.radio("Select Operation", ("Create Account", "Read Accounts", "Update Account", "Delete Account"))

            if operation == "Create Account":
                # Create a new account
                account_number = st.text_input("Enter Account Number")
                account_type = st.text_input("Enter Account Type")
                account_balance = st.text_input("Enter Account Balance")
                customer_id = st.text_input("Enter Customer ID")
                branch_id = st.text_input("Enter Branch ID")

                # Check if the referenced Customer and Branch IDs exist before creating the account
                mycursor.execute("SELECT COUNT(*) FROM Customer WHERE CID = %s", (customer_id,))
                customer_exists = mycursor.fetchone()[0]

                mycursor.execute("SELECT COUNT(*) FROM Branch WHERE BID = %s", (branch_id,))
                branch_exists = mycursor.fetchone()[0]

                if customer_exists > 0 and branch_exists > 0:
                    if st.button("Create Account"):
                        # Create a new account
                        sql = "INSERT INTO Accounts (ANO, A_Type, Balance, CID, BID) VALUES (%s, %s, %s, %s, %s)"
                        val = (account_number, account_type, account_balance, customer_id, branch_id)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Account record has been inserted successfully")

                        # Trigger for logging the create operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Accounts', 'Create')")
                        # mydb.commit()
                else:
                    st.error("Invalid Customer or Branch ID. Please check the provided IDs.")

            elif operation == "Read Accounts":
                # Read all accounts
                mycursor.execute("SELECT * FROM Accounts")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Account":
                # Update an account by ID
                account_number_to_update = st.text_input("Enter Account Number to update")
                new_account_type = st.text_input("Enter new Account Type")
                new_account_balance = st.text_input("Enter new Account Balance")
                new_customer_id = st.text_input("Enter new Customer ID")
                new_branch_id = st.text_input("Enter new Branch ID")

                # Check if the referenced Customer and Branch IDs exist before updating the account
                mycursor.execute("SELECT COUNT(*) FROM Customer WHERE CID = %s", (new_customer_id,))
                customer_exists = mycursor.fetchone()[0]

                mycursor.execute("SELECT COUNT(*) FROM Branch WHERE BID = %s", (new_branch_id,))
                branch_exists = mycursor.fetchone()[0]

                if customer_exists > 0 and branch_exists > 0:
                    if st.button("Update Account"):
                        # Update an account by ID
                        sql = "UPDATE Accounts SET A_Type=%s, Balance=%s, CID=%s, BID=%s WHERE ANO=%s"
                        val = (new_account_type, new_account_balance, new_customer_id, new_branch_id, account_number_to_update)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Account record has been updated successfully")

                        # Trigger for logging the update operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Accounts', 'Update')")
                        # mydb.commit()
                else:
                    st.error("Invalid new Customer or Branch ID. Please check the provided IDs.")

            elif operation == "Delete Account":
                # Delete an account by ID
                account_number_to_delete = st.text_input("Enter Account Number to delete")

                if st.button("Delete Account"):
                    sql = "DELETE FROM Accounts WHERE ANO=%s"
                    val = (account_number_to_delete,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Account record has been deleted successfully")

                    # Trigger for logging the delete operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Accounts', 'Delete')")
                    # mydb.commit()
    #----------------------------------------------------------------------------------
        # Mobile CRUD Operations
        elif option == "Mobile":
            st.subheader("Mobile CRUD Operations")

            operation = st.radio("Select Operation", ("Create Mobile", "Read Mobiles", "Update Mobile", "Delete Mobile"))

            if operation == "Create Mobile":
                # Create a new mobile record
                customer_id = st.text_input("Enter Customer ID")
                mobile_number = st.text_input("Enter Mobile Number")

                # Always display the "Create Mobile" button
                if st.button("Create Mobile"):
                    # Check if the referenced Customer ID exists before creating the mobile record
                    mycursor.execute("SELECT COUNT(*) FROM Customer WHERE CID = %s", (customer_id,))
                    customer_exists = mycursor.fetchone()[0]

                    if customer_exists > 0:
                        # Create a new mobile record
                        sql = "INSERT INTO Mobiles (CID, MobileNumber) VALUES (%s, %s)"
                        val = (customer_id, mobile_number)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Mobile record has been inserted successfully")

                        # Trigger for logging the create operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Mobile', 'Create')")
                        # mydb.commit()
                    else:
                        st.error("Invalid Customer ID. Please check the provided ID before creating a mobile record.")

            elif operation == "Read Mobiles":
                # Read all mobile records
                mycursor.execute("SELECT * FROM Mobiles")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Mobile":
                # Update a mobile record by Customer ID
                customer_id_to_update = st.text_input("Enter Customer ID to update mobile")
                new_mobile_number = st.text_input("Enter new Mobile Number")

                # Always display the "Update Mobile" button
                if st.button("Update Mobile"):
                    # Check if the referenced Customer ID exists before updating the mobile record
                    mycursor.execute("SELECT COUNT(*) FROM Customer WHERE CID = %s", (customer_id_to_update,))
                    customer_exists = mycursor.fetchone()[0]

                    if customer_exists > 0:
                        # Update a mobile record by Customer ID
                        sql = "UPDATE Mobiles SET MobileNumber=%s WHERE CID=%s"
                        val = (new_mobile_number, customer_id_to_update)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Mobile record has been updated successfully")

                        # Trigger for logging the update operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Mobile', 'Update')")
                        # mydb.commit()
                    else:
                        st.error("Invalid Customer ID. Please check the provided ID before updating the mobile record.")

            elif operation == "Delete Mobile":
                # Delete a mobile record by Customer ID
                customer_id_to_delete = st.text_input("Enter Customer ID to delete mobile")

                # Always display the "Delete Mobile" button
                if st.button("Delete Mobile"):
                    # Check if the referenced Customer ID exists before deleting the mobile record
                    mycursor.execute("SELECT COUNT(*) FROM Customer WHERE CID = %s", (customer_id_to_delete,))
                    customer_exists = mycursor.fetchone()[0]

                    if customer_exists > 0:
                        # Delete a mobile record by Customer ID
                        sql = "DELETE FROM Mobiles WHERE CID=%s"
                        val = (customer_id_to_delete,)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Mobile record has been deleted successfully")

                        # Trigger for logging the delete operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Mobile', 'Delete')")
                        # mydb.commit()
                    else:
                        st.error("Invalid Customer ID. Please check the provided ID before deleting the mobile record.")

    #-----------------------------------------------------------------------------
        # Employee CRUD Operations
        elif option == "Employee":
            st.subheader("Employee CRUD Operations")

            operation = st.radio("Select Operation", ("Create Employee", "Read Employees", "Update Employee", "Delete Employee"))

            if operation == "Create Employee":
                # Create a new employee record
                employee_id = st.text_input("Enter Employee ID")
                join_date = st.text_input("Enter Date of Joining (YYYY-MM-DD)")
                leave_date = st.text_input("Enter Date of Leaving (YYYY-MM-DD) (leave blank if still employed)")
                employee_name = st.text_input("Enter Employee Name")
                phone = st.text_input("Enter Phone Number")
                address = st.text_input("Enter Employee Address")
                salary = st.text_input("Enter Salary")
                branch_id = st.text_input("Enter Branch ID")

                # Always display the "Create Employee" button
                if st.button("Create Employee"):
                    # Check if the referenced Branch ID exists before creating the employee record
                    mycursor.execute("SELECT COUNT(*) FROM Branch WHERE BID = %s", (branch_id,))
                    branch_exists = mycursor.fetchone()[0]

                    if branch_exists > 0:
                        # Create a new employee record
                        sql = "INSERT INTO Employee (EID, DateofJoin, DateofLeave, Ename, Phone, Eaddress, Salary, BID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (employee_id, join_date, leave_date, employee_name, phone, address, salary, branch_id)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Employee record has been inserted successfully")

                        # Trigger for logging the create operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Employee', 'Create')")
                        # mydb.commit()
                    else:
                        st.error("Invalid Branch ID. Please check the provided ID before creating an employee record.")

            elif operation == "Read Employees":
                # Read all employee records
                mycursor.execute("SELECT * FROM Employee")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Employee":
                # Update an employee record by ID
                employee_id_to_update = st.text_input("Enter Employee ID to update")
                new_join_date = st.text_input("Enter new Date of Joining (YYYY-MM-DD)")
                new_leave_date = st.text_input("Enter new Date of Leaving (YYYY-MM-DD) (leave blank if still employed)")
                new_employee_name = st.text_input("Enter new Employee Name")
                new_phone = st.text_input("Enter new Phone Number")
                new_address = st.text_input("Enter new Employee Address")
                new_salary = st.text_input("Enter new Salary")
                new_branch_id = st.text_input("Enter new Branch ID")

                # Always display the "Update Employee" button
                if st.button("Update Employee"):
                    # Check if the referenced Branch ID exists before updating the employee record
                    mycursor.execute("SELECT COUNT(*) FROM Branch WHERE BID = %s", (new_branch_id,))
                    branch_exists = mycursor.fetchone()[0]

                    if branch_exists > 0:
                        # Update an employee record by ID
                        sql = "UPDATE Employee SET DateofJoin=%s, DateofLeave=%s, Ename=%s, Phone=%s, Eaddress=%s, Salary=%s, BID=%s WHERE EID=%s"
                        val = (new_join_date, new_leave_date, new_employee_name, new_phone, new_address, new_salary, new_branch_id, employee_id_to_update)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        st.success("Employee record has been updated successfully")

                        # Trigger for logging the update operation
                        # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Employee', 'Update')")
                        # mydb.commit()
                    else:
                        st.error("Invalid new Branch ID. Please check the provided ID before updating an employee record.")

            elif operation == "Delete Employee":
                # Delete an employee record by ID
                employee_id_to_delete = st.text_input("Enter Employee ID to delete")

                # Always display the "Delete Employee" button
                if st.button("Delete Employee"):
                    sql = "DELETE FROM Employee WHERE EID=%s"
                    val = (employee_id_to_delete,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Employee record has been deleted successfully")

                    # Trigger for logging the delete operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Employee', 'Delete')")
                    # mydb.commit()
    #------------------------------------------------------------------------------------
        # Branch CRUD Operations
        elif option == "Branch":
            st.subheader("Branch CRUD Operations")

            operation = st.radio("Select Operation", ("Create Branch", "Read Branches", "Update Branch", "Delete Branch"))

            if operation == "Create Branch":
                # Create a new branch
                branch_id = st.text_input("Enter Branch ID")
                branch_name = st.text_input("Enter Branch Name")
                branch_location = st.text_input("Enter Branch Location")

                if st.button("Create Branch"):
                    # Create a new branch
                    sql = "INSERT INTO Branch (BID, BranchName, Blocation) VALUES (%s, %s, %s)"
                    val = (branch_id, branch_name, branch_location)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Branch record has been inserted successfully")

                    # Trigger for logging the create operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Branch', 'Create')")
                    # mydb.commit()

            elif operation == "Read Branches":
                # Read all branches
                mycursor.execute("SELECT * FROM Branch")
                result = mycursor.fetchall()
                for row in result:
                    st.write(row)

            elif operation == "Update Branch":
                # Update a branch by ID
                branch_id_to_update = st.text_input("Enter Branch ID to update")
                new_branch_name = st.text_input("Enter new Branch Name")
                new_branch_location = st.text_input("Enter new Branch Location")

                if st.button("Update Branch"):
                    # Update a branch by ID
                    sql = "UPDATE Branch SET BranchName=%s, Blocation=%s WHERE BID=%s"
                    val = (new_branch_name, new_branch_location, branch_id_to_update)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Branch record has been updated successfully")

                    # Trigger for logging the update operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Branch', 'Update')")
                    # mydb.commit()

            elif operation == "Delete Branch":
                # Delete a branch by ID
                branch_id_to_delete = st.text_input("Enter Branch ID to delete")

                if st.button("Delete Branch"):
                    sql = "DELETE FROM Branch WHERE BID=%s"
                    val = (branch_id_to_delete,)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    st.success("Branch record has been deleted successfully")

                    # Trigger for logging the delete operation
                    # mycursor.execute("INSERT INTO BankManagerLog (TableName, Action) VALUES ('Branch', 'Delete')")
                    # mydb.commit()

def main():
    st.title("Transactify")

    # Use Streamlit's session_state to maintain login state
    session_state = st.session_state
    if 'logged_in' not in session_state:
        session_state.logged_in = False

    if not session_state.logged_in:
        login_username = st.text_input("Enter username")
        login_password = st.text_input("Enter password", type="password")

        login_button_clicked = st.button("Login")

        if login_button_clicked and authenticate(login_username, login_password):
            session_state.logged_in = True

    if session_state.logged_in:
        display_bank_management_options(session_state)

if __name__ == "__main__":
    main()