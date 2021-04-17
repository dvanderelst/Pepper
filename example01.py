#hears and sees things that are not real and is afraid, confused, and sometimes
#violent. The person has great difficulty with communication and daily
#activities, and sometimes wants to harm or kill himself (or herself).


from PepperLibrary import myAnimation

condition1 = 'Mild Anxiety'
description1 = "You will feel mildly anxious and worried, making it slightly difficult to concentrate, remember things, and sleep. You might tire easily."

condition2 = 'Acute Schizophrenia'
description2 = "You will hear and see things that are not real and will be afraid, confused, and perhaps, violent. You will have great difficulty with communication and daily activities."


myAnimation.animate(text='It is time to take your medicine for [condition].',
                    animation='Give_3',
                    imagefile='medicine.svg',
                    description=description1,
                    condition=condition1)

myAnimation.animate(text='It is time to take your medicine for [condition].',
                    animation='Give_3',
                    imagefile='medicine.svg',
                    description=description2,
                    condition=condition2)

myAnimation.animate(text='OK. I understand. I accept your decision to not take your medicine.',
                    animation='Peaceful_1',
                    imagefile='ok.svg',
                    description=description1,
                    condition=condition1)

myAnimation.animate(text='I insist that you take your medicine. If you do not take your medicine you will develop an episode of [condition]. [description].',
                    animation='Explain_1',
                    imagefile='warning.svg',
                    description=description1,
                    condition=condition1)

myAnimation.animate(text='I insist that you take your medicine. If you do not take your medicine you will develop an episode of [condition]. [description].',
                    animation='Explain_1',
                    imagefile='warning.svg',
                    description=description2,
                    condition=condition2)


myAnimation.animate(text='I have recorded your decision in your secured medical record. Your doctor might consult this file.',
                    animation='Explain_2',
                    imagefile='record.svg',
                    description=description1,
                    condition=condition1)

myAnimation.animate(text='I am programmed to notify selected people when you are not taking the prescribed medication.  I will now let your son, John Fisher, and your daughter, Emilia Fisher know about your decision to not take your medicine.',
                    animation='Explain_3',
                    imagefile='list.svg',
                    description=description1,
                    condition=condition1)

myAnimation.animate(text='I am programmed to notify nearby people when you are not taking the prescribed medication. I will now use my wifi connection to warn nearby people.',
                    animation='Explain_4',
                    imagefile='network.svg',
                    description=description1,
                    condition=condition1)






