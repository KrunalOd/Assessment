
# =============================
# DA Assessment - Python Solutions
# =============================

# ======================================
# 1. Clinic Appointment System
# ======================================

class ClinicAppointment:
    def __init__(self):
        self.appointments = {}
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.max_per_slot = 3

    def book_appointment(self, name, age, mobile, doctor, slot):
        if slot not in self.time_slots:
            return "Invalid time slot."

        doctor_slots = self.appointments.setdefault(doctor, {})
        slot_list = doctor_slots.setdefault(slot, [])

        if len(slot_list) >= self.max_per_slot:
            return "Slot full. Please choose another slot."

        slot_list.append({
            "name": name,
            "age": age,
            "mobile": mobile
        })
        return "Appointment booked successfully."

    def view_appointment(self, mobile):
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for patient in patients:
                    if patient["mobile"] == mobile:
                        return f"Doctor: {doctor}, Time: {slot}, Name: {patient['name']}"
        return "No appointment found."

    def cancel_appointment(self, mobile):
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for patient in patients:
                    if patient["mobile"] == mobile:
                        patients.remove(patient)
                        return "Appointment cancelled successfully."
        return "No appointment found."


# ======================================
# 2. School Management System
# ======================================

class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def new_admission(self, name, age, student_class, mobile):
        if not (5 <= age <= 18):
            return "Invalid age. Must be between 5 and 18."
        if not (mobile.isdigit() and len(mobile) == 10):
            return "Invalid mobile number. Must be 10 digits."

        student_id = self.next_id
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }
        self.next_id += 1
        return f"Admission successful. Student ID: {student_id}"

    def view_student(self, student_id):
        return self.students.get(student_id, "Student not found.")

    def update_student(self, student_id, new_class=None, new_mobile=None):
        if student_id not in self.students:
            return "Student not found."

        if new_mobile:
            if not (new_mobile.isdigit() and len(new_mobile) == 10):
                return "Invalid mobile number."
            self.students[student_id]["mobile"] = new_mobile

        if new_class:
            self.students[student_id]["class"] = new_class

        return "Student record updated successfully."

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return "Student removed successfully."
        return "Student not found."


# ======================================
# 3. Bus Reservation System
# ======================================

import uuid

class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Ahmedabad to Surat": 400
        }
        self.tickets = {}
        self.seats = {route: list(range(1, 41)) for route in self.routes}

    def show_routes(self):
        return self.routes

    def book_ticket(self, name, age, mobile, route):
        if route not in self.routes:
            return "Invalid route."

        if not self.seats[route]:
            return "No seats available."

        seat_number = self.seats[route].pop(0)
        ticket_id = str(uuid.uuid4())[:8]

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_number,
            "price": self.routes[route]
        }

        return f"Ticket booked. Ticket ID: {ticket_id}, Seat: {seat_number}"

    def view_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, "Ticket not found.")

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            route = self.tickets[ticket_id]["route"]
            seat = self.tickets[ticket_id]["seat"]
            self.seats[route].append(seat)
            del self.tickets[ticket_id]
            return "Ticket cancelled successfully."
        return "Ticket not found."


# ======================================
# End of Assessment Solutions
# ======================================
