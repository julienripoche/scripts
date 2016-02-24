#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Spam spam spam !!!
"""

import smtplib
#from email.mime.text import MIMEText
fruits = ['abricot','amande','ananas','avocat','banane','brugnon','cassis','cerise','citron','clementine','coing','datte','figue','fraise','framboise','grenade','groseille','kiwi','mandarine','marron','melon','mirabelle','noisette','noix','olive','orange','patate','pamplemousse','pistache','poire','pomme','raisin','Melissa Ridel']
s = smtplib.SMTP('smtp.live.com')
# 'smtp.laposte.net', 'zimbra.u-psud.fr' not working...
s.starttls()
s.ehlo()
s.login('julian.ripoche@hotmail.fr','***')
me = 'julian.ripoche@hotmail.fr'
you = 'ripochejulien@laposte.net'
s.sendmail(me, you, "test")
#for fruit in fruits:
#    s.sendmail(me, you, "%s" % (fruit))
