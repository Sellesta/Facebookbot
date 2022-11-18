# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:46:26 2022

@author: chege
"""

import fbchat 
from fbchat.models import *

class EchoBot(fbchat.Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsRead(author_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = EchoBot("<email>", "<password>")
client.listen()