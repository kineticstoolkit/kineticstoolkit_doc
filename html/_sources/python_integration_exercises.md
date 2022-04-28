# Integration exercises

{{ stub }}

These exercices will be repeated after seing numpy.

## Calculation of power based on force and velocity
We have a list of forces applied on a moving object by a dynamometer.
We also have a list of velocities for the moving object.
We want to calculate a list of power.
Without and with list comprehension.

## Calculation of power based on force and position
Same example, but with a list of positions instead of velocities. Velocity is calculated as (p(t+1) - p(t-1)) / (2 * sample_time).

## Force threshold
We have a list of forces and a corresponding list of times. We want to know at what time the force started to exceed a given threshold.

## Trajectory of a ball
We throw a 0.1 kg ball upward using a constant force of 50 N applied purely vertically during 0.5 second, then we release it.
- Create a list named `acceleration` that calculates the vertical acceleration of the ball at every 0.1 second during 0 to 2 seconds, 0.5 second being the release time.
- Create a list named `velocity` calculated from the `acceleration` list, using velocity[t] = velocity[t-1] + acceleration[t] * sample_time, knowing that the initial velocity of the ball is 0 m/s.
- Create a list named `position` calculated from the `velocity` list, using position[t] = position[t-1] + velocity[t] * sample_time, knowing that the initial position of the ball is 1 m.