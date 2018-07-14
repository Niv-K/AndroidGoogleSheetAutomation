import pygsheets
from Pages.constants import *
#Client seceret created manually for Google drive (Its created by Google API)



def convert_sheet_to_dict(file_name,sheet_name):
    """


    :param file_name: Name of file in which data is stored
    :param sheet_name: Object Repository or Data Repository
    :return: Record
    """
    #location of Google API Client_secret

    gc = pygsheets.authorize(outh_file=GC)
    sh = gc.open(file_name)

    wks = sh.worksheet_by_title(sheet_name)
    print("________Test__________")
    records = wks.get_all_records()
    print(wks.get_all_records())  # get_all_records get only non empty records
    rec_dict = {}
    if(sheet_name =='ObjectRepository'):
      for i, record in enumerate(records):
        print("This Record is {} :  {} ".format(i, record))
        print(record['Object Name'])
        if record['Object Name']:
            btn_name = record['Object Name']
            print(record['Locator Type'])
            print(record['Locator Value'])
            # if record[1] == 'Locator Type' and  record[2] == 'Locator Value':
            rec_dict[btn_name] = (record['Locator Type'], record['Locator Value'])
    elif(sheet_name == 'DataRepository'):
        for record in records:
           print(record['Data_id']+"--------------"+record['Data'])
           if(record['Data_id'] and record['Data']):
             rec_dict[record['Data_id']] = record['Data']
        print(rec_dict)
    else:
        rec_dict = records
    return rec_dict
