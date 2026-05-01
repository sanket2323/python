class Drone:
    """Represents a delivery drone in a coordinate-based environment."""

    def __init__(self, drone_id: str):
        """Initialise the drone with a unique ID.

        Parameters:
            drone_id: A unique identifier for the drone.
        """
        self._drone_id = drone_id
        self.status = 'idle'
        self.battery = 100
        self.altitude = 0
        # getter method
    def get_drone_id(self) -> str:
        """Return the drone's unique identifier."""
        return self._drone_id

    def get_status(self) -> str:
        """Return the status of the drone."""
        return self.status

    def get_altitude(self) -> int:
        """Return the altitude of the drone."""
        return self.altitude

    def get_battery(self) -> int:
        """Return the battery level of the drone."""
        return self.battery

    #setter method
    def set_drone_id(self, drone_id: str):
        """Set the drone's unique identifier."""
        self._drone_id = drone_id

    def set_status(self, status: str):
        """Set the status of the drone."""
        self.status = status

    def set_altitude(self, altitude: int):
        """Set the altitude of the drone."""
        self.altitude = altitude

    def set_battery(self, battery: int):
        """Set the battery level of the drone."""
        self.battery = battery