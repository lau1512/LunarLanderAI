from LunarLander import *
import math
import numpy as np

n_sims = 1000
fuel = np.array([])
sim = LunarLander()
successful_attempts = 0
failed_attempts = 0
while successful_attempts < n_sims:
    sim.reset()
    done = False
    while not done:
        (x, y, xspeed, yspeed), reward, done = sim.step((boost, left, right))
        if x > 15:
            right = True
        if abs(xspeed)/abs(x)>0.1:
            right = False

        if x < -15:
            left = True
        if abs(xspeed)/abs(x)>0.1:
            left = False


        
        if yspeed>18:
            boost = True
        if yspeed<12:
            boost = False
        if y>170:
            boost = False


        if y < 100:
            if x > 10 or xspeed > 10:
                right = True
            if x < -10 or xspeed < -10:
                left = True  
            if abs(x)<15 and abs(xspeed)<=1:
                left = right = False

        if left and right:
            left = right = False
    # if not reward:
    #     print((x, y, xspeed, yspeed), reward, done)
    if reward:
        fuel = np.append(fuel, reward)
        successful_attempts += 1
    else:
        failed_attempts += 1
    sim.reset()
z = 2.58
m_x = np.mean(fuel)
s_x = math.sqrt(1/(n_sims-1)*sum((fuel-m_x)**2))
v_m_x = s_x/math.sqrt(n_sims)
print("Data for",successful_attempts+failed_attempts,"simulations:")
print("m_x: ",m_x)
print("s_x: ",s_x)
print("v_m_x: ",v_m_x)
print("99% konfidensinterval: ({:.4f} +- {:.4f}), [{:.4f},{:.4f}]".format(m_x,z*v_m_x,m_x-z*v_m_x,m_x+z*v_m_x))
print("Failed attemps:",failed_attempts)