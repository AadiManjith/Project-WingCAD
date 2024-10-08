import numpy as np

def cfd():
    return
 
# Define the evalutation function
def evaluate_cd(s, c, t, alpha): 
    # Constants
    rho = 1.225  # air density (kg/m^3)
    v = 50  # velocity (m/s)
    Cl = 1.5  # lift coefficient (placeholder)
    Cd = 0.5  # drag coefficient (placeholder)
    # Calculate wing area
    A = s * t
    # Calculate downforce and drag
    F_d = 0.5 * rho * v**2 * Cl * A
    F_r = 0.5 * rho * v**2 * Cd * A
    # Return the downforce to drag ratio
    return F_d / F_r
 
# Define the steepest ascent hill climbing algorithm
def hillClimb(bounds):  # max_iter included as a failsafe
    
    # Create the wing dimensions to a random value within the boundaries
    c = np.random.uniform(bounds[0][0], bounds[0][1]) # Returns a random value with uniform distribution
    s = np.random.uniform(bounds[1][0], bounds[1][1])
    t = np.random.uniform(bounds[2][0], bounds[2][1])
    a = np.random.uniform(bounds[3][0], bounds[3][1])

    # Evaluate the initial downforce/drag value
    best_value = evaluate_cd(s, c, t, a)

    # Change the wing dimensions
    d = 1
    d_1 = -1

    optimised = False
    # Evaluate the new downforce/drag value
    while not optimised:
        new_value_ds = evaluate_cd(s + d, c, t, a)
        new_value_dc = evaluate_cd(s, c + d, t, a)
        new_value_dt = evaluate_cd(s, c, t + d, a)
        new_value_da = evaluate_cd(s, c, t, a + d)
        new_value_ds_1 = evaluate_cd(s + d_1, c, t, a)
        new_value_dc_1 = evaluate_cd(s, c + d_1, t, a)
        new_value_dt_1 = evaluate_cd(s, c, t + d_1, a)
        new_value_da_1 = evaluate_cd(s, c, t, a + d_1)

        optimised_s = False
        optimised_c = False
        optimised_t = False
        optimised_a = False

        # Accept the new wing dimensions if the downforce/drag value is better
        # Check that there is an increase in efficiency and what direction it is in
        if new_value_ds - best_value > new_value_ds_1 - best_value and new_value_ds - best_value > 0: 
            s += d # Increments s by increase in correct direction
        elif new_value_ds_1 - best_value > 0:
            s += d_1
        else:
            optimised_s = True

        if new_value_dc - best_value > new_value_dc_1 - best_value and new_value_dc - best_value > 0:
            c += d # Increments c by changed value
        elif new_value_dc_1 - best_value > 0:
            c += d_1
        else:
            optimised_c = True

        if new_value_dt - best_value > new_value_dt_1 - best_value and new_value_dt - best_value > 0:
            t += d # Increments t by changed value
        elif new_value_dt_1 - best_value > 0:
            t += d_1
        else: 
            optimised_t = True

        if new_value_da - best_value > new_value_da_1 - best_value and new_value_da - best_value > 0:
            a += d # Increments a by changed value
        elif new_value_da_1 - best_value > 0:
            a += d_1
        else:
            optimised_a = True

        best_value = evaluate_cd(s, c, t, a)

        if optimised_s == True and optimised_c == True and optimised_t ==  True and optimised_a == True:
            optimised = True
        else:
            optimised = False

    # Return the optimized wing dimensions
    return s, c, t, a, best_value

def check_hillClimb(max_iter): 
    s_opt, c_opt,  t_opt, a_opt, opt_cd = hillClimb(bounds)
    break_count = 0
    for i in range(max_iter):
        s_cur, c_cur,  t_cur, a_cur, cur_cd = hillClimb(bounds)
        if cur_cd > opt_cd:
            s_opt = s_cur
            c_opt = c_cur
            t_opt = t_cur
            a_opt = a_cur
        else:
            break_count += 1
        if break_count > 200:
            break
   

    return s_opt, c_opt, t_opt, a_opt

# Define the boundaries
bounds = [(int(input("Enter min chord: ")), int(input("Enter max chord: "))), (int(input("Enter min span: ")), int(input("Enter max span: "))), (int(input("Enter min thickness: ")), int(input("Enter max thickness: "))), (int(input("Enter min angle: ")), int(input("Enter max angle: ")))]

# Create the wing dimensions to a random value within the boundaries


# Run the hill climbing algorithm
# s_opt, c_opt,  t_opt, alpha_opt, opt_cd = hillClimb(bounds)

s_opt, c_opt, t_opt, a_opt = check_hillClimb(max_iter = int(input("Enter maximum number of iterations to check hill climb")))

# Print the optimized wing dimensions
print("Optimal wing dimensions:")
print(f"Wing span (s): {s_opt:.2f} mm")
print(f"Wing chord (c): {c_opt:.2f} mm")
print(f"Wing thickness (t): {t_opt:.2f} mm")
print(f"Wing angle of attack (α): {a_opt:.2f}°")
 