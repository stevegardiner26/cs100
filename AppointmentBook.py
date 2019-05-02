class AppointmentBook:

    def __init__(self, appointments={}):
        self.appointments = appointments

    def addAppointment(self, day, description):
        if day in self.appointments:
            print("You already have an appointment booked this day")
        else:
            self.appointments[day] = description
            print('Successfully added appointment on ' + day)

    def isScheduled(self, description):
        if description in self.appointments:
            return True
        else:
            return False

