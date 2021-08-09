import socket
import threading
import DataBaseConnection
import TablesObj
import pandas as pd
import communication_file


def handle_client(conn, addr, cf):
    """
    :type cf: communication_file.ServerCommunication
    """
    connected = True
    try:
        while connected:
                msg = cf.received(conn)
                if msg:
                    print(msg)
                    if msg == DISCONNECT_MESSAGE:
                        connected = False
                        cf.send("Lets close the connection", conn)
                    elif msg == "creat table":
                        cf.send("please insert the name", conn)
                        name = cf.received(conn)
                        cf.send("please insert the columns", conn)
                        columns = cf.received(conn).split(",")
                        try:
                            tbl = db.add_table(name, pd.DataFrame(columns=columns))
                            cf.send("The table created successfully", conn)
                            tbl.save()
                        except Exception:
                            cf.send("The table Not created", conn)
                    else:
                        cf.send("I dont understand", conn)
        conn.close()
    except Exception:
        print(f"something went wrong with {addr}")
        conn.close()


if __name__ == "__main__":
    db = DataBaseConnection.SqlConnection()
    DISCONNECT_MESSAGE = "!DISCONNECT"
    on_air = True
    PORT = 5050
    HEADER = 64
    FORMAT = "utf-8"
    SERVER = ''
    # cf = communication_file.ServerCommunication(PORT, FORMAT, HEADER, SERVER)
    # cf.start(handle_client)
    ls = db.get_tables_names()
    tbl = db.get_table(ls[0])
    lst = tbl.rows_list()
    lst[0].change("Color", "yellow")
    tbl.save()
