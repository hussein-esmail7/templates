"""
Subtitle File Time-shift Conversion Program
Hussein Esmail
Created: 2021 01 12
Updated: 2021 02 10
Description: This program inputs a .vtt/.sbv subtitle file, 
    and asks for a time delay: HH:MM:SS:MS and outputs
    a new .vtt/.sbv file with the time delay factored into every line.
"""

import os, sys, re, math, time
try:
    from pick import pick
except:
    print("Installing 'pick' library...")
    time.sleep(0.5)
    os.system("pip install pick")
    os.system("pip3 install pick")
    from pick import pick


def input_to_int(string_to_ask):
    while True:
        var = input(string_to_ask)
        try:
            var = int(var)
            break
        except:
            print("Please input an integer number.")
    return var
    
def int_length(num_to_convert, length):
    num_to_convert_str = str(num_to_convert).replace(".", "")
    print(f"Converting: {num_to_convert_str} to length {length}")
    if len(num_to_convert_str) == length:
        return num_to_convert_str
    elif len(num_to_convert_str) > length:
        return str(int_length(num_to_convert_str[:-1], length))
    elif len(num_to_convert_str) < length:
        return str(int_length("0" + num_to_convert_str, length))
    else:
        print("Idk what to do here")


def main():
    while True:
        file_directory = input("Please input the directory the subtitle files are in: ")
        try:
            os.chdir(file_directory)
            break
        except:
            print("Not a valid directory. Please enter again.")
    separator = "==============="
    input_lines = []
    output_lines = []
    print(separator)
    file_choice, _ = pick(sorted([f for f in os.listdir() if not f.startswith('.') and (f.endswith('.vtt') or f.endswith('.sbv'))]), "Pick the subtitle file you want to edit.")
    # print(separator)
    file_type = file_choice.split(".")[-1]
    if file_type == "vtt":
        regex_pattern = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
    elif file_type == "sbv":
        regex_pattern = "[0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9],[0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
    else:
        regex_pattern = ""
        print("This file type is not supported.")
        sys.exit()
    with open(file_choice, "r") as f:
        input_lines = "".join(f.readlines()).split("\n")
    if len(input_lines) == 0:
        print("File is empty!")
        sys.exit()
    # Ask for time inputs here
    print("Please input the time delays (integers only):")
    shift_hour =    input_to_int("__:00:00:000 - Hours: ")
    shift_min =     input_to_int("00:__:00:000 - Minutes: ")
    shift_sec =     input_to_int("00:00:__:000 - Seconds: ")
    shift_ms =      input_to_int("00:00:00:___ - Milliseconds: ")
    # print(f"{shift_hour}, {shift_min}, {shift_sec}, {shift_ms}")
    # print(separator)
    for line in input_lines:
        if re.match(regex_pattern, line):
            ms_total_convert = (shift_hour * 3600000) + (shift_min + 60000) + (shift_sec * 1000) + shift_ms
            ms_current_start = (int(line[0:2]) * 3600000) + (int(line[3:5]) * 60000) + (int(line[6:8]) * 1000) + int(line[9:12])
            ms_current_end   = (int(line[17:19]) * 3600000) + (int(line[20:22]) * 60000) + (int(line[23:25]) * 1000) + int(line[26:30])
            ms_current_start += ms_total_convert
            ms_current_end += ms_total_convert
            start_hour = math.floor(ms_current_start/3600000)
            remain = ms_current_start % 3600000
            start_min = remain / 60000
            remain = remain % 60000
            start_sec = remain / 1000
            start_ms = remain % 1000

            end_hour = math.floor(ms_current_end/3600000)
            remain = ms_current_end % 3600000
            end_min = remain / 60000
            remain = remain % 60000
            end_sec = remain / 1000
            end_ms = remain % 1000

            if file_type == "vtt":
                # regex_pattern = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
                new_line = f"{int_length(start_hour, 2)}:{int_length(start_min, 2)}:{int_length(start_sec, 2)}:{int_length(start_ms, 3)} --> {int_length(end_hour, 2)}:{int_length(end_min, 2)}:{int_length(end_sec, 2)}:{int_length(end_ms, 3)}"
            elif file_type == "sbv":
                # regex_pattern = "[0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9],[0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
                new_line = f"{int_length(start_hour, 1)}:{int_length(start_min, 2)}:{int_length(start_sec, 2)}.{int_length(start_ms, 3)},{int_length(end_hour, 1)}:{int_length(end_min, 2)}:{int_length(end_sec, 2)}.{int_length(end_ms, 3)}"
            else:
                new_line = line
                print(f"This file type is not supported: {file_type}")
                sys.exit()
            output_lines.append(new_line)
    output_filename = "output"
    output_filename_count = 1
    while True:
        if output_filename + "." + file_type not in os.listdir():
            output_filename += "." + file_type
            break
        else:
            if output_filename + " (" + str(output_filename_count) + ")." + file_type not in os.listdir():
                output_filename = output_filename + " (" + str(output_filename_count) + ")." + file_type
                break
            else:
                output_filename_count += 1
    with open(output_filename, "w") as f:
        f.writelines(output_lines)
    print("Output file is: " + output_filename)
    sys.exit()



if __name__ == "__main__":
    main()