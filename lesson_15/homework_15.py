class Rhombus:
    def __init__(self, side, angle):
        # Initialize Rombus with a side and one angle
        self.side = side
        self.angle = angle

    def __setattr__(self, attribute, value):
        # Custom method for setting attributes values with validation
        if attribute == "side":
            if value > 0:
                super().__setattr__(attribute, value)
            else:
                raise ValueError("Side length must be greater than zero.")
        elif attribute == "angle":
            if 0 < value < 180:
                super().__setattr__(attribute, value)
            else:
                raise ValueError("Angle must be between 0 and 180 degrees.")
        else:
            # For any other attributes, use the default behavior
            super().__setattr__(attribute, value)

    def display_info(self):
        # Method displaying the Rhombus information
        print(f"Rhombus: Side = {self.side}, Angle = {self.angle}")

