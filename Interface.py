import datetime


# Welcome message displays total mileage and time the last truck returned to base.
# Also provides options for the user to check multiple packages at a specific time, specific packages at a specific time
# or view more details on each truck.
def welcome_message(total_miles, truck1, truck2, truck3, t1_package_list, t2_package_list, t3_package_list,
                    hash_table, distance_list):
    print("Welcome to the WGUPS Routing Program.")
    print(f"All packages were delivered in {total_miles:.2f} miles")
    print(f"The last truck returned to base at {get_last_truck_time(truck1, truck2, truck3)}")
    user_input = None
    while user_input != 'exit':
        user_input = input('''
Please enter 1 to view the status of ALL packages at a specific time.
Please enter 2 to view the status of a specific package at a specific time.
Please enter 3 to view total mileage of all trucks.
Please enter exit to exit.
''').lower()
        # Display all packages at a specific time.
        if user_input == '1':
            current_time = input("Please enter a time in the format of hh:mm:ss, i.e. 9:30"
                                 " would be 09:30:00.   ")

            # Determine elapsed time between trucks start time and users requested time.
            # uses the elapsed time to determine distance at 18 miles per hour
            elapsed_minutes = get_time_difference(current_time, truck1)
            h, m, s = current_time.split(':')
            current_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            current_distance = elapsed_minutes * 0.3

            # Resets each truck and the hash table to prepare to run it up the time requested by the user.
            hash_table.reset_packages()
            truck1.reset(t1_package_list, hash_table, distance_list)
            truck2.reset(t2_package_list, hash_table, distance_list)
            truck3.reset(t3_package_list, hash_table, distance_list)
            truck1.deliver(current_distance, current_time, hash_table)
            truck2.deliver(current_distance, current_time, hash_table)
            truck3.deliver(current_distance, current_time, hash_table)

            hash_table.list_packages()
        # Display specific package at a specific time.
        elif user_input == '2':
            pack_id = input("Please enter the package ID you'd like to view: ")
            current_time = input("Please enter a time in the format of hh:mm:ss, i.e. 9:30"
                                 " would be 09:30:00. ")
            # Determine elapsed time between trucks start time and users requested time.
            # uses the elapsed time to determine distance at 18 miles per hour
            elapsed_minutes = get_time_difference(current_time, truck1)
            h, m, s = current_time.split(':')
            current_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            current_distance = elapsed_minutes * 0.3

            # Resets each truck and the hash table to prepare to run it up the time requested by the user.
            hash_table.reset_packages()
            truck1.reset(t1_package_list, hash_table, distance_list)
            truck2.reset(t2_package_list, hash_table, distance_list)
            truck3.reset(t3_package_list, hash_table, distance_list)
            truck1.deliver(current_distance, current_time, hash_table)
            truck2.deliver(current_distance, current_time, hash_table)
            truck3.deliver(current_distance, current_time, hash_table)

            print(hash_table.search(int(pack_id)))
        # Displays each trucks total mileage, start time, and end time. Also displays the total mileage of all three
        # trucks combined.
        elif user_input == '3':
            hash_table.reset_packages()

            truck1.reset(t1_package_list, hash_table, distance_list)
            truck2.reset(t2_package_list, hash_table, distance_list)
            truck3.reset(t3_package_list, hash_table, distance_list)
            truck1.full_deliver(hash_table)
            truck2.full_deliver(hash_table)
            truck3.full_deliver(hash_table)

            print(f"Truck 1's Mileage: {truck1.total_distance}  Start Time: {truck1.start_time}   End Time: "
                  f"{truck1.end_time}")
            print(f"Truck 2's Mileage: {truck2.total_distance}  Start Time:{truck2.start_time}   End Time: "
                  f"{truck2.end_time}")
            print(f"Truck 3's Mileage: {truck3.total_distance}  Start Time: {truck3.start_time}   End Time: "
                  f"{truck3.end_time}")
            total = truck1.total_distance + truck2.total_distance + truck3.total_distance
            print(f"Total mileage for all trucks is {total:.2f}")


# Takes the trucks start time and the users requested time and returns a timedelta of the time between the two.
# O(1)
def get_time_difference(current_time, truck):
    (h, m, s) = current_time.split(':')
    current_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    start_time = truck.start_time
    elapsed_time = current_time - start_time

    # Converts the delta into elapsed minuts. This can be used todetermine how far the truck has driven by a certain
    # time.
    elapsed_seconds = elapsed_time.seconds
    elapsed_minutes = elapsed_seconds / 60
    return elapsed_minutes


# Converts the number of minutes to hours and minutes.
# O(n) Greedy Algorithm!
def get_time_delta(elapsed_minutes):
    h = 0
    m = 0
    while elapsed_minutes > 0:
        if elapsed_minutes > 60:
            elapsed_minutes -= 60
            h += 1
        else:
            elapsed_minutes -= 1
            m += 1
    return h, m


# Returns the time the final truck returns to base.
# O(1)
def get_last_truck_time(truck1, truck2, truck3):
    return max(truck1.end_time, truck2.end_time, truck3.end_time)
