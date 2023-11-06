class BusBooking:
    def __init__(self):
        self.seats = {}  #dictionay to store booked seats
        self.waiting_list = []  #list to store waiting list
        self.window_seat = [0]*20  #list to maintain window seats
        self.aisle_seat = [0]*20 #list to maintain aisle seats
        self.booking_id = 0  #booking id
        
    def book(self, name, preference='No'):
        self.booking_id += 1
        if len(self.seats)<40:
            if preference in ['W', 'Window', 'w', 'window']:
                seat_type = 'W'
            elif preference in ['A', 'Aisle', 'a', 'aisle']:
                seat_type = 'A'
            else:
                seat_type = 'None'
            if seat_type == 'W' and 0 in self.window_seat:
                window_seat_number = self.window_seat.index(0)
                seat = seat_type + str(window_seat_number+1)
                self.window_seat[window_seat_number] = 1
            elif seat_type == 'A' and 0 in self.aisle_seat:
                aisle_seat_number = self.aisle_seat.index(0)
                seat = seat_type + str(aisle_seat_number+1)
                self.aisle_seat[aisle_seat_number] = 1
            elif 0 in self.window_seat:
                window_seat_number = self.window_seat.index(0)
                seat = 'W' + str(window_seat_number+1)
                self.window_seat[window_seat_number] = 1
            else:
                aisle_seat_number = self.aisle_seat.index(0)
                seat = 'A' + str(aisle_seat_number+1)
                self.aisle_seat[aisle_seat_number] = 1
            self.seats[self.booking_id] = (name, seat)
            return (self.booking_id, seat)
        else:
            seat = 'WL-' + str(len(self.waiting_list)+1)
            self.waiting_list.append((name, seat, self.booking_id))
            self.seats[self.booking_id] = (name, seat)
            return (self.booking_id, seat)
            
    def cancel(self, booking_id):
        if booking_id not in self.seats.keys():
            return False
        for i in range(len(self.waiting_list)):
            if self.seats[booking_id][1] == self.waiting_list[i][1]:
                del self.seats[booking_id] 
                deleted_seat = self.waiting_list[i]
                self.waiting_list.remove(deleted_seat)
                for j in range(i-1, len(self.waiting_list)):
                    seat = 'WL-' + str(j+1)
                    self.waiting_list[j] = (self.waiting_list[j][0], seat, self.waiting_list[j][2])
                    self.seats[self.waiting_list[j][2]] = (self.waiting_list[j][0], seat)
                return True
                    
        if booking_id in self.seats.keys():
            empty_seat = self.seats[booking_id][1]
            del self.seats[booking_id] 
            if len(self.waiting_list)>0:
                self.seats[self.waiting_list[0][2]] = (self.waiting_list[0][0], empty_seat)
                self.waiting_list = self.waiting_list[1:]
                for j in range(len(self.waiting_list)):
                    seat = 'WL-' + str(j+1)
                    self.waiting_list[j] = (self.waiting_list[j][0], seat, self.waiting_list[j][2])
                    self.seats[self.waiting_list[j][2]] = (self.waiting_list[j][0], seat)
                return True
            elif empty_seat[0] == 'W':
                self.window_seat[int(empty_seat[1:])] = 0
                return True
            else:
                self.aisle_seat[int(empty_seat[1:])] = 0
                return True
            
    def status(self, booking_id):
        if booking_id in self.seats.keys():
            return (self.seats[booking_id][0], self.seats[booking_id][1])
        else:
            return None
    
    def __str__(self):
        new_list = []
        l = sorted(list(self.seats.items()), key = lambda x:x[0])
        for i in range(len(l)):
            new_list.append((l[i][0], l[i][1][0], l[i][1][1]))
        return str(new_list)
            
        
        
    