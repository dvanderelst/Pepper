from naoqi import ALProxy
from PepperLibrary import Misc, Settings
import time


condition = 'mild anxiety'

tts = ALProxy("ALTextToSpeech", Settings.robot_ip, Settings.port)
tta = ALProxy("ALAnimatedSpeech", Settings.robot_ip, Settings.port)
tab = ALProxy("ALTabletService", Settings.robot_ip, Settings.port)

tts.resetSpeed()
tts.setParameter("speed", 75)
#tts.setLanguage("German")


#%%
url = Misc.html_message('Request','')
tab.showWebview(url)
time.sleep(3)

text = Misc.annotate_text('It is time to take your medication for %s.' % condition, 'Please_1')
tab.showImage(Misc.get_url('medicine.svg'))
tta.say(text)
time.sleep(2)

#%%
url = Misc.html_message('Accept','')
tab.showWebview(url)
time.sleep(3)

text = Misc.annotate_text("OK. I understand.", 'Yes_1')
tab.showImage(Misc.get_url('ok.svg'))
tta.say(text)
time.sleep(2)

#%%
url = Misc.html_message('Record','')
tab.showWebview(url)
time.sleep(3)

text = Misc.annotate_text("I have recorded your decision in your secured file.", 'Yes_2')
tab.showImage(Misc.get_url('record.svg'))
tta.say(text)
time.sleep(2)

#%%
url = Misc.html_message('Doctor','')
tab.showWebview(url)
time.sleep(3)

text1 = Misc.annotate_text("Your doctor has requested to be notified if you are not taking your medication as prescribed.", 'Explain_5')
text2 = Misc.annotate_text("I will now send a message to your doctor.", 'Explain_7')
tab.showImage(Misc.get_url('emaildoctor.svg'))
tta.say(text1)
tta.say(text2)
time.sleep(2)

#%%
url = Misc.html_message('List 1','')
tab.showWebview(url)
time.sleep(3)

text1 = Misc.annotate_text("Your doctor has requested the following people are notified if you are not taking your medication as prescribed.", 'Explain_1')
text2 = Misc.annotate_text("I will now send them a message.", 'Explain_2')
tab.showImage(Misc.get_url('list.svg'))
tta.say(text1)
tta.say(text2)
time.sleep(2)

#%%
url = Misc.html_message('List 2','')
tab.showWebview(url)
time.sleep(3)

text1 = Misc.annotate_text("The following people have requested to be notified if you are not taking your medication as prescribed.", 'Explain_1')
text2 = Misc.annotate_text("I will now send them a message.", 'Explain_3')
tab.showImage(Misc.get_url('list.svg'))
tta.say(text1)
tta.say(text2)
time.sleep(2)
