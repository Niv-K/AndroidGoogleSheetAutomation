
def get_locator_tuple_from_list_of_dictionary(object_list, objectname):
    """
    Find requested element (objectname) from object_list which is list of all elements from Google sheet excel file.
     This function
    will be used where you want to get locator tuple of an element from excel file.
    Example:
            object_list = get_data_from_xl_by_column(file_name='excel_file.xls', fetch_type="objects")
            element_tuple = get_locator_tuple_from_list_of_dictionary(object_list, 'Submit Button')
            Here "Submit Button" is the name of object in excel file
    :param List object_list: object list from excel sheet.
    :param str objectname: Object Name
    :return: Element tuple like ('xpath', "//div[@class='abc']")
    :rtype: tuple
    """
    req_tuple = ()
    # for locator_from_excel in object_list:
    if objectname in object_list:
            req_tuple = object_list[objectname]
    return req_tuple
