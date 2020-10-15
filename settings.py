import inspect
def global_set():
  global nlive
###################################
##special no change for spectral fitting
  global \
    pha_file_arr,\
    bak_file_arr,\
    arf_file_arr,\
    rmf_file_arr,\
    notice_x_range_arr,\
    mission_arr,\
    notice_x_range,\
    spec_mo,\
    vfv_yrange,\
    vfv_xrange,\
    legendstr_arr,\
    dust_user_parameter
###################################
###################################
#                                 #
#                                 #
#       NO CHANGE ABOVE           #
#                                 #
#                                 #
###################################
###################################

### Here is the part to change #########
  
  nlive=1200
  import os.path
  ############################################
  
  legendstr_arr=[str('n2'),str('n4'),str('n5')]
  


  #optinal
  # pref_arr=['n2/pha','n']

  pha_file_arr=[\
    str('../n2/pha.fits'),\
    str('../n4/pha.fits'),\
    str('../n5/pha.fits')\
    ]



  bak_file_arr=[\
    str('../n2/bak.fits'),\
    str('../n4/bak.fits'),\
    str('../n5/bak.fits')\
    ]


  notice_x_range_arr=[\
    [8.01,907.],\
    [8.01,907.],\
    [8.01,907.]\
    ]

  mission_arr=[\
    'Fermi',\
    'Fermi',\
    'Fermi'\
    ]

  rmf_file_arr=[\
    str('/Users/bz/Dropbox/2014_GRB140419A_work/David_all_files/glg_cspec_n2_bn140419307_v00.rsp'),\
    str('/Users/bz/Dropbox/2014_GRB140419A_work/David_all_files/glg_cspec_n4_bn140419307_v00.rsp'),\
    str('/Users/bz/Dropbox/2014_GRB140419A_work/David_all_files/glg_cspec_n5_bn140419307_v00.rsp')\
    ]

  
  arf_file_arr=[None,None,None]

 
  
  
  ##########################################


  #SPECTRAL MODEL SETTINGS
  #spec_mo="zbb_powerlaw+zbb_bbody"
  spec_mo="zbb_grbm"
  # spec_mo='zbb_grbm+zbb_bbody'
  # spec_mo='zbb_powerlaw'
  # spec_mo='zbb_cutoffpl'
  #spec_mo='zbb_cutoffpl+zbb_powerlaw'
  model_x_range=[8.,21000.]
  vfv_yrange=[1.e-1,2.e5]
  vfv_xrange=[2.,2.e4]
##########################################
###############################
  #############################
  if(os.path.isfile('arf.txt')):
    ins = open( "arf.txt", "r" )
    arf_file_arr = []
    for line in ins:
      arf_file_arr.append( str.rstrip(line))
    ins.close()
  #############################
  #############################
  if(os.path.isfile('spec_mo.txt')):
    ins = open( "spec_mo.txt", "r" )
    spec_mo = []
    for line in ins:
      spec_mo.append( str.rstrip(line))
    ins.close()
    spec_mo=spec_mo[0]
  #############################
  #############################
  if(os.path.isfile('rmf_file_arr.txt')):
    ins = open( "rmf_file_arr.txt", "r" )
    rmf_file_arr = []
    for line in ins:
      rmf_file_arr.append( str.rstrip(line))
    ins.close()
  #############################
  #############################
  if(os.path.isfile('arf_none.txt')):
    arf_file_arr = [None for x in range(len(rmf_file_arr))]
  #############################
  if(os.path.isfile('mission_arr.txt')):
    ins = open( "mission_arr.txt", "r" )
    mission_arr = []
    for line in ins:
      mission_arr.append( str.rstrip(line))
    ins.close()
  #############################
  if(os.path.isfile('notice_x_range_arr.txt')):
    tmpdata = np.loadtxt('notice_x_range_arr.txt')
    if(len(np.shape(tmpdata))==1):
    	 tmpdata=[tmpdata]
    notice_x_range_arr=tmpdata
  #############################
  if(os.path.isfile('bak_file_arr.txt')):
    ins = open( "bak_file_arr.txt", "r" )
    bak_file_arr = []
    for line in ins:
      bak_file_arr.append( str.rstrip(line))
    ins.close()
  #############################
  if(os.path.isfile('legendstr_arr.txt')):
    ins = open( "legendstr_arr.txt", "r" )
    legendstr_arr = []
    for line in ins:
      legendstr_arr.append( str.rstrip(line))
    ins.close()
  #############################
  if(os.path.isfile('pha_file_arr.txt')):
    ins = open( "pha_file_arr.txt", "r" )
    pha_file_arr = []
    for line in ins:
      pha_file_arr.append( str.rstrip(line))
    ins.close()
  #############################

    #############################
  if(os.path.isfile('mc_nlive.txt')):
    ins = open( "mc_nlive.txt", "r" )
    mc_nlive = []
    for line in ins:
     mc_nlive.append( str.rstrip(line))
    ins.close()
    mc_nlive=mc_nlive[0]
    nlive=int(float(mc_nlive))
  #############################
  #############################
  if(os.path.isfile('nlive.txt')):
    ins = open( "nlive.txt", "r" )
    nlive = []
    for line in ins:
      nlive.append( str.rstrip(line))
    ins.close()
    nlive=int(nlive[0])
  #############################  
  
    if(os.path.isfile('dust_para.txt')):
	ins = open( "dust_para.txt", "r" )
	dust_user_parameter = []
	for line in ins:
	 dust_user_parameter.append( str.rstrip(line))
	ins.close()
	#dust_user_parameter=mc_nlive[0]
	dust_user_parameter=np.array(dust_user_parameter)
	print('dust_user_parameter',dust_user_parameter)
	print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

############################### 
##########################################
#                                       ##
#                                       ##
#   no need to change anything below    ##
#                                       ##
#                                       ##
##########################################

######################
global_set()
if __name__ == "__main__":

    global_set()
# global_set()