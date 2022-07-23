# pico_lasertoy

 raspbery pico based laser toy to keep cats entertained

- Raspberry Pi Pico
- 2 servos, one attached directly onto the other to create a simple gimble system
- a touch switch to start the action
- cheap laser diode, switched on and off by transistor attached to a pico pin output and the 5v supply for more power. The laser is attached to the second servo, with flexible wiring to allow free movement in all directions by the two servos.

After activating the switch, the laser is turned on and the servos mark out the maximum range of movement, then the system goes into a random cycle of moving to a random position, for a random amount of time, with a 5% chance that the laser will be turned off (you've got to keep them on their toes)... this repeats for 10min before the system goes dormant again and waits for the switch to be activated again.

Keeps cats busy for a while, experience shows that they get tired of this game after about 2 runs. Note that the lens on the laser diode can be adjusted to cause a larger spot, so far the 5v supply hasn't burned out the diode. The max/min settings for each servo need to be defined to avoid collisions, and to fit the floorplan of the play area. The range of movement for the servos ends up making a trapezoid form on the floor, eventually I would like to include a coordinate translation system to make this more square on the floor, but for now this was the simplest way to program the movement, and it's scalable depending on how high the unit is placed on a shelf above the floor.
