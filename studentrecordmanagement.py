# Student Record Management System using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add Student
    def add(self):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        new = Node(roll, name, marks)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

        print("Student added successfully.")

    # Delete Student
    def delete(self):
        roll = int(input("Enter Roll No to delete: "))

        temp = self.head
        prev = None

        while temp:
            if temp.roll == roll:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Student deleted successfully.")
                return

            prev = temp
            temp = temp.next

        print("Student not found.")

    # Update Student
    def update(self):
        roll = int(input("Enter Roll No to update: "))

        temp = self.head

        while temp:
            if temp.roll == roll:
                temp.name = input("Enter New Name: ")
                temp.marks = float(input("Enter New Marks: "))
                print("Student updated successfully.")
                return

            temp = temp.next

        print("Student not found.")

    # Search Student
    def search(self):
        roll = int(input("Enter Roll No to search: "))

        temp = self.head

        while temp:
            if temp.roll == roll:
                print("\nStudent Found!")
                print("Roll No:", temp.roll)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return

            temp = temp.next

        print("Student not found.")

    # Display Students
    def display(self):
        if self.head is None:
            print("No student records.")
            return

        print("\nRoll No\tName\tMarks")
        print("-------------------------")

        temp = self.head

        while temp:
            print(temp.roll, "\t", temp.name, "\t", temp.marks)
            temp = temp.next

    # Sort Students
    def sort(self):
        if self.head is None:
            print("No records to sort.")
            return

        print("\nSort By:")
        print("1. Roll Number")
        print("2. Marks")

        choice = int(input("Enter choice: "))

        print("\nOrder:")
        print("1. Ascending")
        print("2. Descending")

        order = int(input("Enter order: "))

        # Compare and swap data
        p = self.head

        while p:
            q = p.next

            while q:
                if choice == 1:
                    a = p.roll
                    b = q.roll
                else:
                    a = p.marks
                    b = q.marks

                if (order == 1 and a > b) or (order == 2 and a < b):
                    p.roll, q.roll = q.roll, p.roll
                    p.name, q.name = q.name, p.name
                    p.marks, q.marks = q.marks, p.marks

                q = q.next

            p = p.next

        print("Records sorted successfully.")


# Main Program
s = StudentList()

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Sort Students")
    print("7. Exit")

    ch = int(input("\nEnter your choice: "))

    if ch == 1:
        s.add()

    elif ch == 2:
        s.delete()

    elif ch == 3:
        s.update()

    elif ch == 4:
        s.search()

    elif ch == 5:
        s.display()

    elif ch == 6:
        s.sort()

    elif ch == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")