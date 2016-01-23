import sneaze_pynotify
import re
from time import sleep
import json


def popup(title, message):

		pop = sneaze_pynotify.Notification(title, message)
		pop.show()
		return


popup("this is title", "this is message")