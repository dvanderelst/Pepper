from naoqi import ALProxy
from PepperLibrary import Misc, Settings
import time

tts = ALProxy("ALTextToSpeech", Settings.robot_ip, Settings.port)
tta = ALProxy("ALAnimatedSpeech", Settings.robot_ip, Settings.port)
tablet = ALProxy("ALTabletService", Settings.robot_ip, Settings.port)
alife = ALProxy("ALAutonomousLife", Settings.robot_ip, Settings.port)
tracker = ALProxy("ALTracker", Settings.robot_ip, Settings.port)

tablet.setBackgroundColor('#FFFFFF')

alife.setAutonomousAbilityEnabled('All', True)
alife.setAutonomousAbilityEnabled('BasicAwareness', False)

tts.resetSpeed()
tts.setParameter("speed", 60)


def animate(text, animation, imagefile, html_header=None, html_message=None, condition=None, description=None):
    if html_header is None:
        html_header = 'Message:'
        html_message = 'TEXT: '+ text + ', ' + animation

    text = text.replace('[condition]', condition)
    text = text.replace('[description]', description)

    message = Misc.html_message(header=html_header, message=html_message)
    text = Misc.annotate_text(text, animation)
    image = Misc.get_url(imagefile)

    tablet.showWebview(message)
    time.sleep(2)
    tracker.lookAt([1, 0, 0.5],0,1,True)
    tablet.showImageNoCache(image)
    time.sleep(2)
    tta.say(text)
    time.sleep(3)
