from network.db.dal import check_db_connection

def health_check():
    return True

def health_database_check():
    response = check_db_connection()
    if (response == True):
        print("====> D.B. Check: > SUCCESS < ...")
    else:
        print("#### Error to connect to D.B.")
    return response