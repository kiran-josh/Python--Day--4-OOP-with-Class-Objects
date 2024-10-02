"""
Name: Kiran G
Program:using OOPS concept convert below UML diagram into a python class and its methods. 

TV class
TVClass - Base class
LedTV class
PlasmaTV class
Part - A

1. Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. 
Channel should be 1 by default. Volume should be 50 by default. 
2. Add methods to increase and decrease volume. Volume can't never be below 0 or above 100. 
3. Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel. 
4. Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor). 
5. It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75". 

Part - B : LED , Plasma

1. Inherit a TV class add additional properties like
 screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , 
 which displays the detailed features of the TV


"""


class TV:
    def __init__(self, brand):
        """Initialize the TV with brand, channel, volume, and other properties."""
        self.brand = brand
        self.channel = 1  # Default channel
        self.volume = 50   # Default volume
        self.on = False    # TV is initially off
        self.price = 0     # Price can be set later
        self.inches = 0    # Size can be set later

    def power(self):
        """Toggle the TV's power status."""
        self.on = not self.on
        state = "on" if self.on else "off"
        print(f"{self.brand} TV is now {state}.")

    def increase_volume(self):
        """Increase the volume, ensuring it does not exceed 100."""
        if self.on and self.volume < 100:
            self.volume += 1
        print(f"{self.brand} TV volume: {self.volume}")

    def decrease_volume(self):
        """Decrease the volume, ensuring it does not go below 0."""
        if self.on and self.volume > 0:
            self.volume -= 1
        print(f"{self.brand} TV volume: {self.volume}")

    def set_channel(self, channel):
        """Set the channel if it's within the valid range (1-50)."""
        if self.on and 1 <= channel <= 50:
            self.channel = channel
        print(f"{self.brand} TV channel: {self.channel}")

    def reset(self):
        """Reset the TV to default settings."""
        self.channel = 1
        self.volume = 50
        print(f"{self.brand} TV has been reset to channel {self.channel} and volume {self.volume}.")

    def status(self):
        """Return the current status of the TV."""
        return f"{self.brand} at channel {self.channel}, volume {self.volume}."


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        """Initialize the LED TV with additional properties."""
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        """Method to show viewing angle."""
        print(f"{self.brand} LED TV viewing angle: 178 degrees.")

    def backlight(self):
        """Method to display backlight information."""
        print(f"{self.brand} LED TV has dynamic backlight features.")

    def display_details(self):
        """Display detailed features of the LED TV."""
        details = (
            f"{self.brand} LED TV Details:\n"
            f"Screen Thickness: {self.screen_thickness} cm\n"
            f"Energy Usage: {self.energy_usage} W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz"
        )
        print(details)


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        """Initialize the Plasma TV with additional properties."""
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        """Method to show viewing angle."""
        print(f"{self.brand} Plasma TV viewing angle: 160 degrees.")

    def backlight(self):
        """Method to display backlight information."""
        print(f"{self.brand} Plasma TV has a consistent backlight.")

    def display_details(self):
        """Display detailed features of the Plasma TV."""
        details = (
            f"{self.brand} Plasma TV Details:\n"
            f"Screen Thickness: {self.screen_thickness} cm\n"
            f"Energy Usage: {self.energy_usage} W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz"
        )
        print(details)


# Example usage
if __name__ == "__main__":
    led_tv = LedTV("Samsung", 5, 100, 50000, 120)
    plasma_tv = PlasmaTV("Panasonic", 10, 150, 60000, 60)

    led_tv.power()
    led_tv.set_channel(5)
    led_tv.increase_volume()
    led_tv.display_details()
    print(led_tv.status())
    
    plasma_tv.power()
    plasma_tv.set_channel(3)
    plasma_tv.decrease_volume()
    plasma_tv.display_details()
    print(plasma_tv.status())

    # Resetting the LED TV
    led_tv.reset()
