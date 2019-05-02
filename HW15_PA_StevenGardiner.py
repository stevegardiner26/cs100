import AppointmentBook

book = AppointmentBook.AppointmentBook()
book.addAppointment('Monday', 'Dentist')
book.addAppointment('Saturday', 'Personal Trainer')

book.isScheduled('Physician')