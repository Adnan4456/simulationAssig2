#start from 0 seconds
sec = 0
#  Currentsignal is string value it changes from { Red , Green, Yellow and Pending }
Currentsignal = "red"
# time when the  last signal was changed
durationOfSignal = 0
# time for  pedestrian . when press button this value is given
pedestrianPresent = 70
# check  pedestrian is present
pedestrian = True

for sec in range(200):
    #start from red signal value
    if Currentsignal == "red":
        if sec - durationOfSignal >= 60:  # Red to be changed to green after 60 seconds
            # Currentsignal is equal  to green
            Currentsignal = "green"
            durationOfSignal = sec
            print(sec, "sec", " now light is green now")
        else:
            print(sec, "sec", " light is red now")
    elif Currentsignal == "green":
        # Green to be changed to pending when  pedestrian press button
        if sec - durationOfSignal < 60 and pedestrian and pedestrianPresent <= sec:
            # changing to pending

            Currentsignal = "pending"
            pedestrian = False
            print(sec, "sec", "  light in pending state")
            print("it will pending for 1 min")
        # Green to be changed to yellow after 60 seconds
        elif sec - durationOfSignal >= 60 and pedestrian and pedestrianPresent <= sec:
            # Currentsignal is equal to  yellow
            Currentsignal = "yellow"
            pedestrian = False
            changeOfSignal = sec
            print(sec, "sec", " light is yellow now")

        else:
            print(sec, "sec", " light is green now")

    elif Currentsignal == "pending":
        if sec - durationOfSignal >= 60:
            # Currentsignal is equal to yellow
            Currentsignal = "yellow"
            changeOfSignal = sec
            print(sec, "sec", " light is yellow now")
        else:
            print(sec, "sec", " light in pending state ")
    elif Currentsignal == "yellow":
        # yellow to be changed after 5sec
        if sec - durationOfSignal >= 5:
            # Currentsignal is equal  to red
            Currentsignal = "red"
            durationOfSignal = sec

            print(sec, "sec", " light is red now")
        else:
            print(sec, "sec", " light is yellow now")
