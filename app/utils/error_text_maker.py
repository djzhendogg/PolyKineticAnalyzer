def define_error_text(error_info, filename):
    if error_info == 'file_read_error':
        error_text = f"Unable to extract information from a file\nor broken file. Error in\n{filename}"
    elif error_info == 'define_inflections_error':
        error_text = f"Unable to find the extremes of\ncrystallization. Error in\n{filename}"
    elif error_info == 'define_area_error':
        error_text = f"Unable to to calculate the area bounded\nby the curve. Error in\n{filename}"
    elif error_info == 'define_kinetic_param_error':
        error_text = f"Error in final calculations\nof Avrami parmeters. Error in\n{filename}"
    elif error_info == 'fridman_error':
        error_text = f"Error in calculations of Fridman parmeters."
    else:
        error_text = "Unknown error in\n{filename}"
    return error_text
