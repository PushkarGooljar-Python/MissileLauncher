import time


def output_animation(msg, delay=0.25):
    """Animates output"""
    for letter in msg:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()


def hash_(to_hash):
    # Hashes input to make it unintelligible by naked eye
    import hashlib
    result = hashlib.sha256(to_hash.encode())
    return result.hexdigest()


def change_launch_code():
    """Allows user to change launch code"""

    # Gets the current launch code from the 'launchCodeHash.txt' file
    with open('launchCodeHash.txt', 'r') as f:
        correct_launch_code_hash = f.read()

    # Gets and hashes user submitted launch code
    submitted_launch_code = input('Enter current launch code: ')
    submitted_launch_code_hash = hash_(submitted_launch_code)

    # Checks if user submitted correct launch code
    if submitted_launch_code_hash == correct_launch_code_hash:

        # If yes, asks for and hashes new launch code
        new_launch_code = input('Enter new launch code: ')
        new_launch_code_hash = hash_(new_launch_code)

        # Writes new launch code hash to 'launchCodeHash.txt'
        with open('launchCodeHash.txt', 'w') as f:
            f.write(new_launch_code_hash)

        # Informs user that launch code was changed and asks for other command
        print('Launch code saved')
        key_press()

    # If incorrect launch code submitted, tells user and asks for other command
    else:
        print('Incorrect launch code')
        key_press()


def arm_system():
    """Arms the system if it is unarmed"""

    # Gets the state of the system
    with open('systemState.txt', 'r') as f:
        s = f.read()

    if s == 'True':
        system_armed = True
    else:
        system_armed = False

    # Gets the correct launch code from the 'launchCodeHash.txt' file
    with open('launchCodeHash.txt', 'r') as f:
        correct_launch_code_hash = f.read()

    # If system already armed, tells user
    if system_armed:
        print('System already armed')
        key_press()

    # If system not armed, allows user to try to arm it
    else:
        launch_code = input('Enter launch code to arm system: ')
        launch_code_hash = hash_(launch_code)

        # If user inputs correct launch code, system state is true, therefore
        # system is armed
        if launch_code_hash == correct_launch_code_hash:
            with open('systemState.txt', 'w') as f:
                f.write('True')
            print('Correct launch code, system armed')
            key_press()

        # If user inputs incorrect launch code they are informed and system remains disarmed
        else:
            print('Incorrect launch code, system disarmed')
            key_press()


def disarm_system():
    """Disarms the system if it is unarmed"""

    # Gets the state of the system
    with open('systemState.txt', 'r') as f:
        s = f.read()

    if s == 'True':
        system_armed = True
    else:
        system_armed = False

    # Gets the correct launch code from the 'launchCodeHash.txt' file
    with open('launchCodeHash.txt', 'r') as f:
        correct_launch_code_hash = f.read()

    # If system not disarmed, allows user to try to disarm it
    if system_armed:
        launch_code = input('Enter launch code to disarm system: ')
        launch_code_hash = hash_(launch_code)

        # If user inputs correct launch code, system state is false, therefore
        # system is disarmed
        if launch_code_hash == correct_launch_code_hash:
            with open('systemState.txt', 'w') as f:
                f.write('False')
            print('Correct launch code, system disarmed')
            key_press()

        # If user inputs incorrect launch code they are informed and system remains armed
        else:
            print('Incorrect launch code, system armed')
            key_press()

        print('System already armed')
        key_press()

    # If system already armed, tells user
    else:
        print('System already disarmed')
        key_press()


def unrecognised_command(command_):
    """Informs user they inputted an unrecognised command and tells them
    which commands are recognised and what they do"""

    print(f"Unrecognised command: '{command_}'\n"
          f"Here are commands you can use:\n"
          f"'A': Arm system\n"
          f"'D': Disarm system\n"
          f"'L': Launch missile\n"
          f"'C': Change launch code")
    key_press()


def launch_sequence(duration, show_seconds=True):
    """Launches missile"""

    # Gets the state of the system
    with open('systemState.txt', 'r') as f:
        s = f.read()

    if s == 'True':
        system_armed = True
    else:
        system_armed = False

    # If the system is armed, missile is launched
    if system_armed:
        msg = 'Launching in: '
        for letter in msg:
            print(letter, end='', flush=True)
            time.sleep(0.25)
        for second in reversed(range(duration + 1)):
            if show_seconds:
                print(f"\rLaunching in: {second} seconds", end='')
                time.sleep(1)
            else:
                print(f"\rLaunching in: {second}", end='')
                time.sleep(1)
        print()
        print('Ignition...')
        time.sleep(1)
        print('Liftoff!')
        key_press()

    # If the system is disarmed, tells user to arm before launching
    else:
        print('System disarmed, arm system before launching')
        key_press()


def key_press():
    """Gets the user inputted command and calls for functions accordingly"""

    # Prompt to input command
    command = input('>>> ')

    # Calls respective functions according to command
    if command.lower() == 'c':
        change_launch_code()

    elif command.lower() == 'a':
        arm_system()

    elif command.lower() == 'd':
        disarm_system()

    elif command.lower() == 'l':
        launch_sequence(10)

    # If the user inputs an unrecognised command, calls the
    # Unrecognised command function
    else:
        unrecognised_command(command)


if __name__ == '__main__':
    output_animation('Welcome to Missile Launcher...')
    key_press()
