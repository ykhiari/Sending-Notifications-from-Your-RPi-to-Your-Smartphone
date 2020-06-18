from pyimagesearch.notifications import TwilioNotifier
from pyimagesearch.utils import Conf
import argparse


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c","--conf", required=True,help= "Path to the input configuration file")
args = vars(ap.parse_args())

# load the configuration file and initialize the Twilio notifier
conf = Conf(args["conf"])
tn = TwilioNotifier(conf)

# send a text message
print("[INFO] Sending TXT message...")
tn.send("Incoming message from RPI...")
print("[INFO] txt message send.")