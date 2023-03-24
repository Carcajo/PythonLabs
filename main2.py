import json
import users as us
import commands as com


try:
    while True:
        username = us.authorize()
        if username == False: quit()
        if com.do_commands(username) == False: quit()
except OSError:
    print("Problem with a data file")
    quit()
except json.decoder.JSONDecodeError:
    print("Problem with a data file")
    quit()