
import numpy as np

def IUH_comp(gamma, Ab, dt, dataiuh, deltaT):
    """
    %% % -------------------------------------------------------------------------------
    #% Calculation of the Instantaneous Unit Hydrograph
    #% ---------------------------------------------------------------------------------
    Ab basin area
    dt = time step (can be day, months or years)
    deltaT = computational time step in hours
    dataiuh # generated with https://github.com/benjiyamin/pyflo
    """
    Lag = (gamma * 1.19 * Ab ** 0.33) / deltaT #relationship of Melone et al. (2001)
    hp = 0.8 / Lag
    t = dataiuh[:, 0] * Lag
    IUH_0 = dataiuh[:, 1] * hp
    ti = np.arange(0, max(t), dt)
    IUH = np.interp(ti, t, IUH_0)
    return IUH

def IUH_NASH(n, gamma, Ab, dt, deltaT):
    """
    % -------------------------------------------------------------------------------
    % Calculation of Nash Instantaneous Unit Hydrograph
    % -------------------------------------------------------------------------------
    Ab basin area
    dt = time step (can be day, months or years)
    deltaT = computational time step in hours
    """
    K = (gamma * 1.19 * Ab ** .33) / deltaT #relationship of Melone et al. (2001)
    time = np.arange(0, 100, dt)
    return (time / K) ** (n - 1) * np.exp(-time / K) / factorial(n - 1) / K

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
