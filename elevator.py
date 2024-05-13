import threading
import time

class Elevator():

    def __init__(self, floors: int):
        self.floors = floors-1 #[0, 1, 2, ... , n-1]
        self.current_floor = 0
        self.going_up = True
        self.requests_up = []
        self.requests_down = []

    def request(self):
        while True:
            requested_floor = int(input("Type a floor:\n"))
            if (requested_floor < 0) or (requested_floor > self.floors): #floor out of bounds
                continue 
            elif self.current_floor == requested_floor: #elevator is already at the requested floor
                continue
            elif requested_floor > self.current_floor: #upper floors where requested
                if requested_floor in self.requests_up: #floor already requested
                    continue 
                new_req_up = [x for x in self.requests_up if x < requested_floor] + [requested_floor] + [x for x in self.requests_up if x > requested_floor] #insert floor and keep an ascending order
                self.requests_up = new_req_up
            elif requested_floor < self.current_floor: #lower floors where requested
                if requested_floor in self.requests_down: #floor already requested
                    continue 
                new_req_down = [x for x in self.requests_down if x > requested_floor] + [requested_floor] + [x for x in self.requests_down if x < requested_floor] #insert floor and keep a descending order
                self.requests_down = new_req_down

    def move(self):
        while True:
            time.sleep(5)
            if (len(self.requests_up) == 0) and (len(self.requests_down) == 0): #no requests
                print("Waiting requests...\n")
                continue
            else:
                print(f"Next requests up: {self.requests_up}")
                print(f"Next requests down: {self.requests_down}\n")
            if self.going_up:
                if len(self.requests_up) > 0: #upper floors where requested
                    if self.current_floor == self.requests_up[0]: #if the current floor is the first in the requests list...
                        print(f"Elevator is visiting requested floor {self.requests_up.pop(0)}\n") #...visit the floor and remove it from the requests...
                    else: #...if not, increase the current floor until requested floor is reached
                        print(f"Elevator is in floor {self.current_floor}\n") 
                        self.current_floor += 1
                        if self.current_floor > self.floors: #reached the top
                            self.current_floor = self.floors #prevents overflow
                            self.going_up = False #reverse the elevator
                else: #no more upper floors where requested
                    self.going_up = False #reverse the elevator
            elif not self.going_up:
                if len(self.requests_down) > 0: #lower floors where requested
                    if self.current_floor == self.requests_down[0]: #if the current floor is the first in the requests list...
                        print(f"Elevator is visiting requested floor {self.requests_down.pop(0)}\n") #...visit the floor and remove it from the requests...
                    else: #...if not, decrease the current floor until requested floor is reached
                        print(f"Elevator is in floor {self.current_floor}\n") 
                        self.current_floor -= 1
                        if self.current_floor < 0: #reached the bottom
                            self.current_floor = 0 #prevents overflow
                            self.going_up = True #reverse the elevator
                else: #no more lower floors where requested
                    self.going_up = True #reverse the elevator

if __name__ == "__main__":
    elevator = Elevator(8)

    floor_requests = threading.Thread(target=elevator.request)
    elevator_engine = threading.Thread(target=elevator.move)

    floor_requests.start()
    elevator_engine.start()