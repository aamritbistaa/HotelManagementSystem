A database project done with python and mysql.

Start with starting a mysql database

It should have host="localhost",user="root",password="",database="hotelmanagementsystem"
There should be 3 tables in a database

        customer
            it contains
            column name:        Datatype:
                ref             INT(11)[Primary key, Not null]
                name            VARCHAR(45)
                gender          VARCHAR(45)
                mobile          VARCHAR(45)
                nationality     VARCHAR(45)
                idproof         VARCHAR(45)
                idnumber        VARCHAR(45)
                email           VARCHAR(45)
                address         VARCHAR(45)
                postal          VARCHAR(45)

        details
            it contains
            column name:        Datatype:
                floor           VARCHAR(45)
                roomNo          VARCHAR(45)[Primary key, Not null]
                roomType        VARCHAR(45)


        room
            it contains
            column name:        Datatype:
                ref         VARCHAR(45)
                check_in        VARCHAR(45)
                check_out       VARCHAR(45)
                roomtype        VARCHAR(45)
                roomavailable   VARCHAR(45)[Primary key, Not null]
                meal            VARCHAR(45)
                noofdays        VARCHAR(45)

Start the code with login page[login.py]
[Admin,Admin]

then you will be navigated to main screen[main.py]
there you will be able to choose 3 options

1.Customer Window[customer.py]
a place to add remove update customer window

2.Room Window[room.py]
a place to book and clear room

3.Hotel[details.py]
a place where you can add,removeand modify room information

Meal detail:

- Breakfast
- Dinner
- Lunch
- All
