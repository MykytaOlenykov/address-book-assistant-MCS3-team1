class InvalidPhone(Exception):
    def __init__(self, phone, *args):
        super().__init__(*args)
        self.message = f"Phone {phone} is invalid. The phone number must be in the format (XXX)-XXX-XXXX."


class PhoneNotFound(Exception):
    def __init__(self, name, phone, *args):
        super().__init__(*args)
        self.message = f"{name}`s record doesn`t contain {phone} phone number."


class PhoneConflict(Exception):
    def __init__(self, name, phone, *args):
        super().__init__(*args)
        self.message = f"{name}`s record contains {phone} phone number."
