'''
Program:
    used to analysis the my weichat data.
    Instution : https://itchat.readthedocs.io/zh/latest/
'''

import itchat
import numpy
import Friends
import Data_analysis
my_friends=Friends.Friends.get_data()
# Data_analysis.Gender_status(my_friends)
# Data_analysis.Places_stats(my_friends)
signatures=Data_analysis.Signature_data(my_friends)
Data_analysis.Create_wc(signatures)
