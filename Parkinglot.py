import Vehicle
import argparse
import sys

if sys.version_info[0] == 2:
    input1 = input()


class ParkingLot:
    def __init__(self):
        self.capacity = 0
        self.slotid = 0
        self.numOfOccupiedSlots = 0
        self.res_di = {}

    def createParkingLot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, regno, color, age):
        if self.numOfOccupiedSlots < self.capacity:
            slotid = self.getEmptySlot()
            self.slots[slotid] = Vehicle.Car(regno, color, age)
            print(self.slots[slotid])
            self.slotid = self.slotid + 1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
            return slotid + 1
        else:
            return -1

    def leave(self, slotid):
        if self.numOfOccupiedSlots > 0 and self.slots[slotid - 1] != -1:
            self.slots[slotid - 1] = -1
            self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
            return True
        else:
            return False

    def status(self):
        #res_di = dict()

        print("Slot No.\tRegistration No.\tColour.\t\tAge")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                li = []
                print(str(i + 1) + "\t\t" + str(self.slots[i].regno) + "\t\t" + str(self.slots[i].color)+"\t\t" + str(self.slots[i].age))
                li.append(str(self.slots[i].regno))
                li.append(str(self.slots[i].age))
            else:
                continue
            self.res_di[str(i+1)] = li
        print(self.res_di)

    def getRegNoFromColor(self, color):

        regnos = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                regnos.append(i.regno)
        return regnos

    def getSlotNoFromRegNo(self, regno):

        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                return i + 1
            else:
                continue
        return -1

    def getSlotNoFromColor(self, color):

        slotnos = []
        print(self.slots)
        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i + 1))
        return slotnos

# slot_no by age
    def slot_no_of_age(self, age):
        slotnos = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].age == age:
                slotnos.append(str(i + 1))
        return slotnos

#vehicle registration by Age

    def getRegNoFromAge(self, age):

        regnos = []
        for i in self.slots:

            if i == -1:
                continue
            if i.age == age:
                regnos.append(i.regno)
        return regnos



    def show(self, line):
        if line.startswith('Create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingLot(n)
            print('Created parking of ' + str(res) + ' slots')

        elif line.startswith('Park'):
            regno = line.split(' ')[1]
            color = line.split(' ')[2]
            age   = line.split(' ')[4]
            res = self.park(regno, color, age)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Car with Vehicle Registration Number '+ '"'+str(regno)+'"' +' has been parked at slot number ' + str(res))

        elif line.startswith('Leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                print("Slot number {0} vacated, the car with vehicle registration number {1} left the space, the driver of the car was of age {2}"
                    .format(leave_slotid, self.res_di[str(leave_slotid)][0], self.res_di[str(leave_slotid)][1]))

        elif line.startswith('Status'):
            self.status()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            regnos = self.getRegNoFromColor(color)
            print(', '.join(regnos))

        elif line.startswith('Slot_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getSlotNoFromColor(color)
            print(', '.join(slotnos))

        elif line.startswith('Slot_number_for_car_with_number'):
            regno = line.split(' ')[1]
            slotno = self.getSlotNoFromRegNo(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)

        elif line.startswith('Slot_numbers_for_driver_of_age'):
            age = line.split(' ')[1]
            slotno = self.slot_no_of_age(age)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)

        elif line.startswith('Vehicle_registration_number_for_driver_of_age 18'):
            color = line.split(' ')[1]
            regnos = self.getRegNoFromAge(color)
            print(', '.join(regnos))

        elif line.startswith('exit'):
            exit(0)


def main():
    parkinglot = ParkingLot()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    args = parser.parse_args()

    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)
    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)


if __name__ == '__main__':
    main()
