import datetime


def welcome_message(total_miles, truck1, truck2, truck3, t1_package_list, t2_package_list, t3_package_list,
                    hash_table, distance_list):
    print("Welcome to the WGUPS Routing Program.")
    print(f"All packages were delivered in {total_miles} miles")
    user_input = None
    while user_input != 'exit':
        user_input = input('''
Please enter 1 to view the status of ALL packages at a specific time.
Please enter 2 to view the current mileage of each truck at a specific time.
Please enter exit to exit.
''')
        if user_input == '1':
            current_time = input("Please enter a time in the format of hh:mm:ss. For example, 10:30"
                                 " would be 10:30:00: ")
            elapsed_minutes = get_time_difference(current_time, truck1)
            # print(elapsed_minutes)
            current_distance = elapsed_minutes * 0.3
            print(f"current_distance: {current_distance}")
            truck1.reset(t1_package_list, hash_table, distance_list)
            truck2.reset(t2_package_list, hash_table, distance_list)
            truck3.reset(t3_package_list, hash_table, distance_list)
            truck1.deliver(current_distance)
            truck2.deliver(current_distance)
            truck3.deliver(current_distance)

            # truck1.list_packages()
            # truck2.list_packages()
            # truck3.list_packages()
        elif user_input == '2':
            print(f"Truck One's Mileage: {truck1.total_distance}")
            print(f"Truck Two's Mileage: {truck2.total_distance}")
            print(f"Truck Three's Mileage: {truck3.total_distance}")


def get_time_difference(current_time, truck):
    (h, m, s) = current_time.split(':')
    current_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    print(f"TIME DELTA = {current_time}")
    start_time = truck.start_time
    elapsed_time = current_time - start_time
    elapsed_seconds = elapsed_time.seconds
    elapsed_minutes = elapsed_seconds / 60
    print(f"ELAPSED_MINUTES {elapsed_minutes}")
    return elapsed_minutes


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
