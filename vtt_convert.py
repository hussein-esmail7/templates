"""
.vtt Subtitle File Time-shift Conversion Program
Hussein Esmail
Created: 2021 01 12
Updated: 2021 02 05
Description: This program inputs a .vtt subtitle file, 
    and asks for a time delay: HH:MM:SS:MS and outputs
    a new .vtt file with the time delay factored into every line.
"""

import os, sys, re

def conv_int_single_digit(item):
    if int(item) < 10:
        return str(int(item))

def check_int(sentence):
    while True:
        number = input(sentence)
        try:
            number = int(number)
            return number
        except:
            print("ERROR: Please input a valid number.")

def conv_int_str(number, length):
    if length == 3 and len(str(number)):
        to_return = str(number)
        for i in range(len(str(number)), length):
            to_return += "0"
        return to_return
    elif len(str(number)) < length:
        if len(str(number)) == 2:
            return str(number)
        elif len(str(number)) == 1:
            return "0" + str(number)
        elif len(str(number)) == 0:
            return "00"
        else: # > 2 digits
            return str(number)
    else:
        return str(number)

def check_None(var):
    if var == None:
        return "00"
    else:
        return var

def main():
    while True:
        file_directory = input("Please input the directory the subtitle files are in: ")
        try:
            os.chdir(file_directory)
            break
        except:
            print("Not a valid directory. Please enter again.")
    files = sorted(os.listdir())
    separator = "==============="
    if file_type == "vtt":
        regex_pattern = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
    elif file_type == "sbv":
        regex_pattern = "[0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9],[0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]"
    else:
        regex_pattern = ""
    bool_print_lines = False
    bool_output_file = True
    input_lines = []
    output_lines = []
    print(separator)
    for i in range(len(files)):
        print(f"{i+1}. {files[i]}")
    input_file_num = check_int("What is the number of the input file: ")
    print(separator)
    file_type = files[input_file_num-1].split(".")[-1]
    with open(files[input_file_num-1], "r") as f:
        input_lines = "".join(f.readlines()).split("\n")
    if len(input_lines) == 0:
        print("File is empty!")
        sys.exit()
    # Ask for time inputs here
    print("Please input the time delays (integers only):")
    shift_hour =    conv_int_str(check_int("__:00:00:000 - Hours: "), 2)
    shift_min =     conv_int_str(check_int("00:__:00:000 - Minutes: "), 2)
    shift_sec =     conv_int_str(check_int("00:00:__:000 - Seconds: "), 2)
    shift_ms =      conv_int_str(check_int("00:00:00:___ - Milliseconds: "), 3)
    # print(f"{shift_hour}, {shift_min}, {shift_sec}, {shift_ms}")
    # print(separator)
    for line in input_lines:
        line_edited = line
        if re.match(regex_pattern, line):
            start_times = []
            end_times = []
            start_times.append(line_edited[0:2])                                        # Start Hour
            start_times.append(line_edited[3:5])                                        # Start Min
            start_times.append(line_edited[6:8])                                        # Start Sec
            start_times.append(line_edited[9:12])                                       # Start Ms
            end_times.append(line_edited[17:19])                                        # End Hour
            end_times.append(line_edited[20:22])                                        # End Min
            end_times.append(line_edited[23:25])                                        # End Sec
            end_times.append(line_edited[26:30])                                        # End Ms
            start_times[0] = conv_int_str(int(start_times[0]) + int(shift_hour), 2)     # Start hour shift
            end_times[0] = conv_int_str(int(end_times[0]) + int(shift_hour), 2)         # End hour shift
            start_times[1] = conv_int_str(int(str(start_times[1])) + int(shift_min), 2) # Start min shift
            end_times[1] = conv_int_str(int(end_times[1]) + int(shift_min), 2)          # End min shift
            shift_hour = check_None(shift_hour)                                         # Error handling, set to 00
            shift_min = check_None(shift_min)                                           # Error handling, set to 00
            shift_sec = check_None(shift_sec)                                           # Error handling, set to 00
            if shift_ms == None or shift_ms == "":                                      # Didn't use the function because this needs 3 digits
                shift_ms = "000"
            start_times[2] = conv_int_str(int(start_times[2]) + int(shift_sec), 2)      # Start sec shift
            end_times[2] = conv_int_str(int(end_times[2]) + int(shift_sec), 2)          # End sec shift
            start_times[3] = conv_int_str(int(start_times[3]) + int(shift_ms), 3)       # Start ms shift
            end_times[3] = conv_int_str(int(end_times[3]) + int(shift_ms), 3)           # End ms shift
            if file_type == "vtt":
                line_edited = start_times[0] + ":" + start_times[1] + ":" + start_times[2] + "." + start_times[3] + " --> " + end_times[0] + ":" + end_times[1] + ":" + end_times[2] + "." + end_times[3]
            elif file_type == "sbv":
                line_edited = conv_int_single_digit(start_times[0]) + ":" + start_times[1] + ":" + start_times[2] + "." + start_times[3] + "," + conv_int_single_digit(end_times[0]) + ":" + end_times[1] + ":" + end_times[2] + "." + end_times[3]
        output_lines.append(line_edited)
        if bool_print_lines:
            print(line_edited)                                                          # So the user can copy the output to a new file
    if bool_output_file:
        output_filename = "output"
        output_filename_count = 1
        while True:
            if output_filename + ".vtt" not in files:
                output_filename += ".vtt"
                break
            else:
                if output_filename + " (" + str(output_filename_count) + ").vtt" not in files:
                    output_filename = output_filename + " (" + str(output_filename_count) + ").vtt"
                    break
                else:
                    output_filename_count += 1
        with open(output_filename, "w") as f:
            f.writelines(output_lines)
        print("Output file is: " + output_filename)
    sys.exit()

if __name__ == "__main__":
    main()
