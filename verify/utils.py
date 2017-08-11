
# For logging purposes
# Need to make a copy as not to alter the actual data
def scrub_ssn(clean_data):
    try:
        data_copy = clean_data.copy()
        if data_copy['ssn']:
            data_copy['ssn'] = 'xxxx'
    except:
        return clean_data

    return data_copy
