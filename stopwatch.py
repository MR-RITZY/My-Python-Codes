import time, datetime, keyboard, os
def clear_screen():

    """
    Clears the terminal screen. Works for both Windows and Unix-like systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def timeformat(time_diff):

    """
    Converts a timedelta object to a formatted string.

    Args:
        time_diff (timedelta): The time difference to format.

    Returns:
        str: A string representation of the time difference in HH:MM:SS.milliseconds format.
    """

    diff = str(time_diff)
    if '.' in diff:
        dif = diff.partition('.')
        diff = ''.join(dif[0:2]) + str(int(dif[-1])//10000)
    return diff

def Stopwatch():
    """
    A simple stopwatch program with lap recording functionality.

    Features:
    - Press Enter to start the stopwatch and record laps.
    - Press the Space bar to pause and resume the stopwatch.
    - Press Escape or Ctrl+C to exit.

    Displays the total elapsed time and lap times.
    """
    print('Press Enter key to Start.\n\nAfterwards, press Enter key to record a Lap.\n\n\
Space bar to Pause and press it again to Resume from pause\n\nEscape Key or ctrl+C to Exit')

    # Wait for the user to start the stopwatch
    keyboard.wait('enter')
    clear_screen()
    print('Started')
    time.sleep(0.5)
    start = time.time()
    prev = datetime.timedelta(seconds = 0)
    str_current = timeformat(prev)
    lap_num = 0
    lap = ''
    ever_pause = False
    pause_time = 0
    try:
        # Main loop to handle stopwatch functionality
        while not keyboard.is_pressed('esc'):
            current_time = time.time()
            if ever_pause:
                # Adjusting for pause duration
                current = datetime.timedelta(seconds = current_time - start - pause_time )
            else:
                current = datetime.timedelta(seconds = current_time - start)
            str_current = timeformat(current)
            clear_screen()
            print(str_current)
            print(lap)
            time.sleep(0.2)
            if keyboard.is_pressed('enter'):
                # Recording a lap
                lap_num += 1
                change = current - prev
                prev = current
                if lap_num < 10:
                    lap = f'0{lap_num}\t\t{str_current}\t\t{timeformat(change)}\n' + lap
                else:
                    lap = f'{lap_num}\t\t{str_current}\t\t{timeformat(change)}\n' + lap
                clear_screen()
                print(str_current)
                print(lap)
                time.sleep(0.2)
            if keyboard.is_pressed('space'):
                # Pause and resume functionality
                ever_pause = True
                clear_screen()
                print('Paused')
                pause_start = time.time()
                print(str_current)
                print(lap)
                keyboard.wait('space')
                pause_time += time.time() - pause_start
                clear_screen()
                print('Resumed')
                time.sleep(0.2)
                clear_screen()

        # Exit and display final times
        clear_screen()
        print(str_current)
        print(lap)

    except KeyboardInterrupt:
        # Handling Ctrl+C gracefully
        clear_screen()
        print(str_current)
        print(lap)

# Entry point of the program
if __name__ == '__main__':
    Stopwatch()
