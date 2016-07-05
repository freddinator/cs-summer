from Outcome import TextResult, Outcome
from Question import YesNoQuestion

results = {
	"replace": TextResult("You need to replace the device"),
	"charge": TextResult("Try charging the device up completely"),
	"update": TextResult("Please update your device to the latest OS"),
	"outside": TextResult("Try moving outside to get better signal"),
	"batteryreplace": TextResult("You need to replace the device's internal battery"),
	"network": TextResult("Please contact your mobile network's support"),
	"reinstall": TextResult("Please reinstall your device's operating system"),
	"fire": TextResult("The device is currently on fire. Please contact your local fire brigade on 999."),
	"find": TextResult("Please find the device, then try the troubleshooting process again"),
	"glue": TextResult("Please re-attach the components of your device using a glue product"),
	"fail": TextResult("The automated troubleshooting process was unable to find a problem. Please contact support on 01234 567890")
}

question10 = YesNoQuestion("Is the device whole?", [
	Outcome(True, results["fail"]),
	Outcome(False, results["glue"])
	])

question9 = YesNoQuestion("Is the device currently on fire?", [
	Outcome(True, results["fire"]),
	Outcome(False, question10)
	])

question8 = YesNoQuestion("Are you experiencing problems with the phone's Operating System?", [
	Outcome(True, results["reinstall"]),
	Outcome(False, question9)
	])

question7 = YesNoQuestion("Have you received errors about your connection to the mobile network?", [
	Outcome(True, results["network"]),
	Outcome(False, question8)
	])

question6 = YesNoQuestion("Is the battery discharging very quickly?", [
	Outcome(True, results["batteryreplace"]),
	Outcome(False, question7)
	])

question5 = YesNoQuestion("Does your phone have signal?", [
	Outcome(True, question6),
	Outcome(False, results["outside"])
	])

question4 = YesNoQuestion("Is the phone fully updated?", [
	Outcome(True, question5),
	Outcome(False, results["update"])
	])

question3 = YesNoQuestion("Is the phone fully charged?", [
	Outcome(True, question4),
	Outcome(False, results["charge"])
	])

question2 = YesNoQuestion("Have you dropped the phone?", [
	Outcome(True, results["glue"]),
	Outcome(False, question3)
	])

question1 = YesNoQuestion("Has the phone got wet?", [
	Outcome(True, results["replace"]),
	Outcome(False, question2)
	])

question1.ask()