# For now, to be run in the terminal


# GLOBAL VARIABLES
temps_list = []

# stage 1: hot start

hot_start_bool = raw_input("Will there be a hot start stage? (Y/N) ")
if hot_start_bool == "Y":
	hot_start_temp = int(raw_input("What will be the hot start temperature (C)? "))
	hot_start_lid_temp = hot_start_temp + 5
	hot_start_runtime = int(raw_input("What will be the hot start runtime (seconds)? "))
else:
	hot_start_temp = 0
	hot_start_lid_temp = 0
	hot_start_runtime = 0
hot_start = (1, hot_start_lid_temp, hot_start_temp, hot_start_runtime)


# stage 2: main stage

num_of_steps = int(raw_input("How many steps? (3 or 6) "))

if num_of_steps == 3:
	cycles = int(raw_input("How many cycles or repeats? "))
	step_1_temp = int(raw_input("What is the temperature at step 1 (C)? "))
	step_1_runtime = int(raw_input("What is the runtime at step 1 (seconds)? "))
	step_2_temp = int(raw_input("What is the temperature at step 2 (C)? "))
	step_2_runtime = int(raw_input("What is the runtime at step 2 (seconds)? "))
	step_3_temp = int(raw_input("What is the temperature at step 3 (C)? "))
	step_3_runtime = int(raw_input("What is the runtime at step 3 (seconds)? "))
	temps_list.extend([step_1_temp, step_2_temp, step_3_temp])
	heated_lid = max(temps_list) + 5
	main_stage = (cycles, heated_lid, step_1_temp, step_1_runtime, step_2_temp, step_2_runtime, step_3_temp, step_3_runtime)

elif num_of_steps == 6:
	cycles = int(raw_input("How many cycles or repeats? "))
	step_1_temp = int(raw_input("What is the temperature at step 1 (C)? "))
	step_1_runtime = int(raw_input("What is the runtime at step 1 (seconds)? "))
	step_2_temp = int(raw_input("What is the temperature at step 2 (C)? "))
	step_2_runtime = int(raw_input("What is the runtime at step 2 (seconds)? "))
	step_3_temp = int(raw_input("What is the temperature at step 3 (C)? "))
	step_3_runtime = int(raw_input("What is the runtime at step 3 (seconds)? "))
	step_4_temp = int(raw_input("What is the temperature at step 4 (C)? "))
	step_4_runtime = int(raw_input("What is the runtime at step 4 (seconds)? "))
	step_5_temp = int(raw_input("What is the temperature at step 5 (C)? "))
	step_5_runtime = int(raw_input("What is the runtime at step 5 (seconds)? "))
	step_6_temp = int(raw_input("What is the temperature at step 6 (C)? "))
	step_6_runtime = int(raw_input("What is the runtime at step 6 (seconds)? "))
	temps_list.extend([step_1_temp, step_2_temp, step_3_temp, step_4_temp, step_5_temp, step_6_temp])
	heated_lid = max(temps_list) + 5
	main_stage = (cycles, heated_lid, step_1_temp, step_1_runtime, step_2_temp, step_2_runtime, step_3_temp, step_3_runtime, step_4_temp, step_4_runtime, step_5_temp, step_5_runtime, step_6_temp, step_6_runtime)

print hot_start
print main_stage