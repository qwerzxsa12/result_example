#####################################
#Part1
load_user_model(mcspecfitfun_blackbody, "mcspecfit_blackbody")
add_user_pars(str("mcspecfit_blackbody"), \
	[      "kT",   "norm"],\
	[       10. ,  1. ],\
	parmins=[1.e-1,1.e-20 ],\
	parmaxs=[1.e5,1.e20])
mcspecfit_blackbody.integrate=True
#Part1ends
#####################################
#Part2
global mcspecfit_blackbody,mcspecfitfun_blackbody
def mcspecfitfun_blackbody(p,xlo,xhi=None):
    import numpy as np
    if(xhi != None):
        dx=xhi-xlo
        x=np.sqrt(xlo*xhi)
    else:
        dx=xlo**0.
        x=xlo
    
    kT=p[0]
    z=0.0
    k=p[1]
    f=k*8.0525*(x*(1.0+z))**2./(kT**4.0)/(np.exp((x*(1.0+z))/kT)-1.) 
    f=f*dx
    return f
#Part2ends
#####################################
#Part3
if(1 == 1):
  setpar_arr=[\
    'mcspecfit_blackbody.kT',\
    'mcspecfit_blackbody.norm'\
    ]
  parameters=[\
    "kT",\
    'logNorm2']
  global prange
  prange=[\
    [1.,300],\
    [-3,5]\
    ]
  global par_log_flag
  par_log_flag=[0,1]
  global nufnu_setup,vfv_yrange,vfv_xrange
  nufnu_setup={\
    'components':['mcspecfitfun_blackbody'],\
    'para_num':[2],\
    'yrange':vfv_yrange,\
    'xrange':vfv_xrange,\
    'logflag':par_log_flag\
    }
#Part3ends
#####################################
