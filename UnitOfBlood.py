class UnitOfBlood():
    counter_blood_id = 0
    counter_blood_id_a = 0
    counter_blood_id_b = 0

    def __init__(self, bdp, temptime, blood_type_order, order_type):
        self.id = UnitOfBlood.counter_blood_id  # Licznik wszystkich jednostek krwi
        self.order_type = order_type
        self.blood_type = blood_type_order
        self.blood_time = bdp.system_time
        self.expiration_date = temptime
        UnitOfBlood.counter_blood_id += 1
        if(self.blood_type == "A"):
            UnitOfBlood.counter_blood_id_a += 1  # Licznik jednostek krwi grupy A
            # Dodatkowy identyfikator krwi grupy A
            self.id_a = UnitOfBlood.counter_blood_id_a
        else:
            UnitOfBlood.counter_blood_id_b += 1  # Licznik jednostek krwi grupy B
            # Dodatkowy identyfikator krwi grupy B
            self.id_b = UnitOfBlood.counter_blood_id_b
