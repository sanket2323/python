from drone import Drone

d = Drone("ABC123")
d.get_status()

d.set_status("Flying")

print(d.get_status())

d.get_altitude()


d.set_altitude(100)

d.get_altitude()



d.get_battery()
