from pyrigee import *

body = Body("Earth", 5.9722e24, 6378, "cornflowerblue")
craft = Craft("Satellite", "lime")

# Create an initial orbit to start at
initial_orbit = Orbit(400, 400, 0)

# Create a target orbit to maneuver to
target_orbit = Orbit(6000, 6000, 0)
transfer_orbit = Orbit(6000, 400, 0)
# Create a maneuver object by passing the target orbit and color of manuever
maneuver = Maneuver(target_orbit, "firebrick")

p = OrbitPlotter(body)

# Pass maneuver to the plot function
p.plot(initial_orbit, craft, maneuver)
p.plot(transfer_orbit, craft)
p.visualize()
