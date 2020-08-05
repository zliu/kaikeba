

class ParkLot():
    size: 'medium'
    unit_price: 1
    number: 0
    floor: 0
    car_plate: ''
    is_occupied: False
    entrance : 

class MgmtSystem():
    parking_lots = {}
    free_medium_slots = [] # should be full of slots at start
    free_large_slots = []
    free_parking_lots = {
        'medium': free_medium_slots,
        'large': free_large_slots
    }
    def assign_slot(car_size, car_plate):
        # find the first free slot object in the slot free list
        # then pop the slot
        free_slot_list = free_parking_lots[car_size]
        free_slot = free_slot_list.pop()
        free_slot.car_plate = car_plate
        free_slot.start_time= datetime.datetime.now()
        free_slot.is_occupied = True
        parking_lots[car_plate] = free_slot
        return free_slot.floor, free_slot.number

    def charge(car_plate):
        slot = parking_lots[car_plate]
        exit_time = datetime.datetime.now()
        price = slot.unit_price*( exit_time - slot.start_time )
        slot.is_occupied = False
        slot.car_plate = ''
        free_slot_list = free_parking_lots[free_slot.car_size]
        free_slot_list.append(free_slot)
        return price