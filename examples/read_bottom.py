# -*- coding: utf-8 -*-
"""

"""

#from matplotlib.pyplot import figure, show, subplots_adjust
from echolab2.instruments import EK60
#from echolab2.plotting.matplotlib import echogram
#from echolab2.processing import mask

##########################################################
###          THIS EXAMPLE IS NOT COMPLETE
##########################################################


#  create a list of .raw files
rawfiles = ['./data/EK60/DY1706_EK60-D20170625-T061707.raw']
#  and a list of .bot files
botfiles = ['./data/EK60/DY1706_EK60-D20170625-T061707.bot']

#  create an instance of ER60
ek60 = EK60.EK60()

#  read the .raw files
ek60.read_raw(rawfiles, frequencies=[38000,120000])

#  read the .bot files
ek60.read_bot(botfiles)

#  get a reference to the raw_data object
raw_data_38 = ek60.get_raw_data(channel_number=1)
raw_data_120 = ek60.get_raw_data(channel_number=2)

print(raw_data_38)
print(raw_data_120)

bottom_38 = raw_data_38.get_bottom_depths()
bottom_120 = raw_data_120.get_bottom_depths()

#TODO: PLOT ECHOGRAMS AND BOTTOM LINES

#  create a list of .raw files
rawfiles = ['./data/ES60/L0226-D20170624-T143908-ES60.raw',
            './data/ES60/L0226-D20170624-T155849-ES60.raw']
#  and a list of .bot files
botfiles = ['./data/ES60/L0226-D20170624-T143908-ES60.out']

#  create an instance of ER60
ek60 = EK60.EK60()

#  read the .raw files
ek60.read_raw(rawfiles)

#  read the .bot files
ek60.read_bot(botfiles)

#  get a reference to the raw_data object
raw_data_38 = ek60.get_raw_data(channel_number=1)
print(raw_data_38)


bottom_38 = raw_data_38.get_bottom_depths()

#TODO: PLOT ECHOGRAMS AND BOTTOM LINES



#  get a processed_data object containing Sv
Sv = raw_data_38.get_Sv()
print(Sv)



pass