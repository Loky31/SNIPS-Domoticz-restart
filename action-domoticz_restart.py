#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import subprocess
import json
import configparser
import io
import requests
import random
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology.feedback import SiteMessage
from collections import defaultdict


class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {
            section: {
                option_name: option
                for option_name, option in self.items(section)
            }
            for section in self.sections()
        }
        
    
def intent_callback(hermes, intent_message):
    intent_name = intent_message.intent.intent_name.replace("Loky31:", "")
    result = None
    print("{}".format(intent_name))
    if intent_name == "Redemarre":
        subprocess.call("start python turnOFFprise2.py")
        time.sleep( 5 )
        subprocess.call("start python turnONprise2.py")
        result = "Pas de problème, je redémarre Domoticz sur le champ"
    if result is not None:
        hermes.publish_end_session(intent_message.session_id, result)
    
if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intents(intent_callback).start()
        #h.disable_sound_feedback(SiteMessage("default"))
        #h.subscribe_enable_sound_feedback(SiteMessage("default"))