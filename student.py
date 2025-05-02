import sqlite3

class StudentDatabase:

    def __init__(self, db_name='student.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()



    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           age INTEGER,
           grade TEXT 
         )
        """ )
        self.conn.commit()



    def add_student(self, name, age, grade):
        self.cursor.execute("INSERT INTO students (name, age, grade) VALUES (?,?,?)",(name, age, grade))
        self.conn.commit()
        print("Student added successfully. \n")



    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()
    

    
    def search_student(self, name):
        name = name.strip()
        self.cursor.execute("SELECT * FROM students WHERE name LIKE ?",(f"%{name}%",))
        return self.cursor.fetchall()
    

    def update_student(self,student_id, name, age, grade):
        self.cursor.execute("UPDATE students SET name = ?, age =?, grade = ? WHERE id = ?", (name, age, grade, student_id))
        self.conn.commit()
        print("Student updated successfully")


    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?",(student_id))
        self.conn.commit()
        print("Student deleted successfully. \n")


    def close(self):
        self.conn.close()


        
    




    

        





