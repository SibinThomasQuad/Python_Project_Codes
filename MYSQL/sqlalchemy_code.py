from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
password = ""
db_url = "mysql+pymysql://root:"+password+"@localhost/ms"

# Create the database engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Define a base class for declarative models
Base = declarative_base()

# Define a model representing a table in the database
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    salary = Column(Integer, nullable=False)

# Check if the table exists and create it if not
if not engine.dialect.has_table(engine, Employee.__tablename__):
    Base.metadata.create_all(engine)
    print("Table created successfully")

# Insert data into the table
def insert_data(name, age, salary):
    employee = Employee(name=name, age=age, salary=salary)
    session.add(employee)
    session.commit()
    print("Data inserted successfully")

# Update data in the table
def update_data(employee_id, new_salary):
    employee = session.query(Employee).filter_by(id=employee_id).first()
    employee.salary = new_salary
    session.commit()
    print("Data updated successfully")

# Delete data from the table
def delete_data(employee_id):
    employee = session.query(Employee).filter_by(id=employee_id).first()
    session.delete(employee)
    session.commit()
    print("Data deleted successfully")

# Retrieve data from the table
def select_data():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

# Example usage
insert_data("John Doe", 30, 5000)
update_data(1, 6000)
delete_data(1)
select_data()

# Close the session
session.close()
