import pyodbc

conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\18649\Documents\Database1.accdb;')
cursor = conn.cursor()

action = input('What are you attempting to do?[Update, Add]')

while True:
    
    if action.upper() == 'ADD':
        
        Continue = input('do you have another class to enter?[Y/N]')
        Continue = Continue.upper()
        if Continue == 'Y':
            Year = input('What year was the class?\n')
            Semester = input('Spring or Fall semester? [S/F]\n')
            Class = input('What was the name of the class?\n')
            NumGrade = int(input('What was the grade in the class? [number]\n'))
            Credits = int(input('How many credit hours was teh class?\n'))

            if NumGrade >= 90:
                LetGrade = 'A'
                GPA = 4
            elif NumGrade >= 80:
                LetGrade = 'B'
                GPA = 3
            elif NumGrade >= 70:
                LetGrade = 'C'
                GPA = 2
            elif NumGrade >= 60:
                LetGrade = 'D'
                GPA = 1
            else:
                LetGrade = 'F'
                GPA = 0
                
            # Insert a record into Table2
            cursor.execute("INSERT INTO Table2 (ClassYear, Semester, Class, [Number Grade], [Letter Grade], Gpa, CreditHours) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (Year, Semester.upper(), Class.upper(), NumGrade, LetGrade, GPA, Credits))

            # Commit the transaction
            conn.commit()
            
        else:
            break
    elif action.upper() == 'UPDATE':
        col = input('What column would you like to update?[year/semester/class/number grade]')
        Course = input('what is the course code? [ie. MECH 101]')
        Value = input('What would you like to set it to?')
        cursor.execute(f"UPDATE Table2 SET {col} = ? WHERE [Class] = ?", (Value, Course))
        conn.commit()
        break
    
    elif action.upper() == 'NEWCOLUMN':

        # Ask the user for the name of the new column
        new_col = input("Enter the name of the new column: ")

        # Add the new column to the table
        cursor.execute(f"ALTER TABLE Table2 ADD COLUMN {new_col} TEXT")

        # Fetch all the Class values from the table
        cursor.execute("SELECT [Class] FROM Table2")
        classes = cursor.fetchall()

        # Update the new column with the user-specified values for each Class
        for class_ in classes:
            Class = class_[0]
            Value = input(f"Enter the value for the new column for Class {Class}: \n")
            cursor.execute(f"UPDATE Table2 SET {new_col} = ? WHERE [Class] = ?", (Value, Class))
            conn.commit()
        break

# Commit the changes to the database
conn.commit()


    
    # Close the cursor and connection
cursor.close()
conn.close()




