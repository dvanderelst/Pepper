from naoqi import ALProxy
from PepperLibrary import Settings, Messages, Logger
import qi
import time
from os import path
import paramiko
import threading


def tablet_callback(button_id, input_text):
    if button_id == 1:
        print "'OK' button is pressed."
        print "Input text: " + input_text
    if button_id == 0:
        print "'Cancel' button is pressed"


def process_face_detection_value(value, threshold):
    recognized = []
    if len(value) == 0: return []
    faces = value[1][:-1]
    for face in faces:
        extra_info = face[1]
        id = extra_info[0]
        score = extra_info[1]
        label = extra_info[2]
        if score >= threshold: recognized.append([label, id, score])
    return recognized


class Robot:
    def __init__(self):
        self.verbose = 1
        self.logger = Logger.Logger()
        connection_url = "tcp://{}:{}".format(Settings.robot_ip, Settings.port)
        self.application = qi.Application(url=connection_url)
        self.application.start()
        self.session = self.application.session

        #self.tablet = self.session.service("ALTabletService")
        self.face = self.session.service("ALFaceDetection")
        self.memory = self.session.service("ALMemory")
        self.dialog = self.session.service("ALDialog")
        self.life = self.session.service("ALAutonomousLife")

        self.life.setState('solitary')

        #self.tablet.resetTablet()

        self.tablet_input = []
        self.dialog_history = []

    def send_sftp_file(self, filename):
        remote_path = path.join(Settings.robot_home_folder, filename)
        transport = paramiko.Transport((Settings.robot_ip, 22))
        transport.connect(username='nao', password='nao')
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(filename, remote_path)
        sftp.close()
        transport.close()

    def get_tablet_text_input(self, title='input', blocking=True):
        # What to do on input
        self.signal_id1 = 0
        def handle_dialog_input(button_id, input_text):
            if button_id == 1: self.tablet_input = [True, input_text]
            if button_id == 0: self.tablet_input[False, None]
            self.tablet.onInputText.disconnect(self.signal_id1)

        # Show dialog
        self.tablet_input = []
        self.tablet.showInputDialog('text', title, 'OK', 'Cancel')
        # Connect tablet signal to handling function
        self.signal_id1 = self.tablet.onInputText.connect(handle_dialog_input)
        while self.tablet_input == [] and blocking: time.sleep(0.1)
        self.log(self.tablet_input)

    def look_for_faces(self, threshold=0, number=1, blocking=True):
        recognized = []
        while len(recognized) != number:
            value = self.memory.getData('FaceDetected')
            recognized = process_face_detection_value(value, threshold)
            if not blocking: break
        return recognized

    def learn_face(self, name):
        self.look_for_faces(threshold=0)
        self.face.learnFace(name)
        face_list = self.face.getLearnedFacesList()
        return face_list

    def log(self, text, level='i'):
        console_text = time.asctime() + ':' + str(text)
        if self.verbose: print console_text
        self.logger.add(text, level)
        self.logger.write('log.html')

    def show_message(self, a, b):

        # I think the next line caused the issue with the tablet.
        # The function show_message creates an html page that is saved in a local folder on my laptop. I run a http server in that folder
        # That allows me to show the webpage on the robot's tablet.


        self.tablet._enableResetTablet(0)
        url = Messages.html_message(a, b)
        self.tablet.showWebview(url)

    def handle_dialog(self, text):
        entry = [text, time.asctime()]
        self.dialog_history.append(entry)
        self.log(entry)

    def get_topics(self):
        activated = self.dialog.getActivatedTopics()
        loaded = self.dialog.getLoadedTopics('enu')
        return activated, loaded

    def stop_dialog(self):
        activated, loaded = self.get_topics()
        self.log(activated)
        for x in activated: self.dialog.deactivateTopic(x)
        if 'lexicon' in loaded: loaded.remove('lexicon')
        for x in loaded: self.dialog.unloadTopic(x)

    def start_dialog(self, filename):
        self.stop_dialog()
        topic_name = self.dialog.loadTopic(filename)
        self.dialog.activateTopic(topic_name)

        self.subscriber1 = self.memory.subscriber("Dialog/LastInput")
        self.subscriber1.signal.connect(self.handle_dialog)

        self.subscriber2 = self.memory.subscriber("Dialog/Answered")
        self.subscriber2.signal.connect(self.handle_dialog)


R = Robot()
# R.send_sftp_file('basic.top')
#R.show_message("Hello.","Say hello to me to sign in.")
# R.start_dialog('/home/nao/basic.top')
# x = R.get_topics()
# print(x)
# for x in range(100):
#     time.sleep(1)