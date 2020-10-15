#####################################
#Part1
load_user_model(mcspecfitfun_lucas, "mcspecfit_lucas")
add_user_pars(str("mcspecfit_lucas"), \
        [      "p0",   "p1",    "p2",   'p3',  'p4',  'p5',    'p6',    'p7'],\
        [       500. ,  2.8,     5.,    42 ,   0,   30,          1,       1  ],\
        parmins=[0.,    2.0,   0.,  30,     0.,     1.0e-5,      0.01,           0.001 ],\
        parmaxs=[100000, 100.0,    20,    100,    1.e20,   1.0e20,        200.5,        300.0 ])
mcspecfit_lucas.integrate=True
#Part1ends
#####################################
#Part2
global redshift_lucas
import os.path
from os import path
import numpy as np
if(path.exists("../../../INPUT_PARAMETERS/z.txt")):
    z_tmp = np.loadtxt('../../../INPUT_PARAMETERS/z.txt', usecols=[0])
    z=float(z_tmp)
else:
    z=1.0




redshift_lucas=z


def mcspecfitfun_lucas(p,xlo,xhi=None):
	global redshift_lucas
	import numpy as np
	from zbbpy import zbblogen
	if(np.array(xhi).any() != None):
		dx=np.array(xhi)-np.array(xlo)
		x=np.sqrt(np.array(xlo)*np.array(xhi))
	else:
		dx=np.array(xlo)**0.
		x=np.array(xlo)
	P=p[0:8]
	#print(len(P))
	flux_arr=np.ndarray(len(x))
	nu=np.log10(x*2.41789894010E17)
	nu_big_str=""
	from decimal import Decimal
	for i in range(len(nu)):
		nu_now=nu[i]
		nu_str_tmp=str(Decimal(nu_now))
		nu_big_str=nu_big_str+' '+nu_str_tmp
	import numpy as np 
	Gamma=P[0]
	p_e=P[1]
	log10ginj=P[2]
	log10inj_rate_0=P[3]
	q=P[4]
	B0=P[5]
	b=P[6]
	t_obs=P[7]
	import subprocess
	p0_str=str(Decimal(Gamma))
	p1_str=str(Decimal(p_e))
	p2_str=str(Decimal(log10ginj))
	p3_str=str(Decimal(log10inj_rate_0))
	p4_str=str(Decimal(q))
	p5_str=str(Decimal(B0))
	p6_str=str(Decimal(b))
	p7_str=str(Decimal(t_obs))
	redshift_str=str(Decimal(redshift_lucas))
	cmd_zxh='./lucas_sync_with_z_as_ninth_par_bbz_modified_oct_2017.exe'
	para_str=' '+p0_str+" "+p1_str+" "+p2_str+' '+\
		p3_str+' '+p4_str+' '+p5_str+' ' +p6_str+' '+p7_str+' '+redshift_str+' '+\
		nu_big_str+' '
	whole_cmd=cmd_zxh+' '+para_str
	from subprocess import Popen, PIPE
	p = Popen(whole_cmd,stdout=PIPE,shell=True,stderr=PIPE)
	(out,err) = p.communicate()
	tmp_str_list=out.split()
	result_tmp=np.ndarray(len(out.split()))*0.
	for i in range(len(result_tmp)):
		result_tmp[i]=np.float(tmp_str_list[i])
	result_tmp=(2418.0/1.602)*result_tmp/(x)
	flux=np.array(result_tmp)
	flux=flux*dx
	return flux
#Part2ends
#####################################
#Part3
global mcspecfit_lucas,mcspecfitfun_lucas
#from zbbpy import mcspecfitfun_cutoffpl
if(spec_mo == "mcspecfit_lucas"):
  setpar_arr=[\
    'mcspecfit_lucas.p0',\
    'mcspecfit_lucas.p1',\
    'mcspecfit_lucas.p2',\
    'mcspecfit_lucas.p3',\
    'mcspecfit_lucas.p4',\
    'mcspecfit_lucas.p5',\
    'mcspecfit_lucas.p6',\
    'mcspecfit_lucas.p7'\
    ]

  parameters=[\
    "log\\Gamma", \
    "p",\
    "log\\gamma_{inj}",\
    'logR_{inj}^0',\
    'q',\
    'logB_0',\
    'b',\
    "\\hat{t}"\
    #"t^\\prime"\
    ]
#     p0_str=str(Decimal(Gamma))
#     p1_str=str(Decimal(p_e))
#     p2_str=str(Decimal(log10ginj))
#     p3_str=str(Decimal(log10inj_rate_0))
#     p4_str=str(Decimal(q))
#     p5_str=str(Decimal(B0))
#     p6_str=str(Decimal(b))
#     p7_str=str(Decimal(t_obs))
   
  global prange
  print('begin prange')
  prange=[[1.0, 4.0], [2.001, 6.0], [3.0, 6.0], [44.0, 50.0], [0.01, 5.0], [0.9, 2.0], [0.01, 2.0], [0.01, 10.0]]
  print("~~~~~~~~~~")
 
  global par_log_flag
  par_log_flag=[1,0,0,0,0,1,0,0]
  global nufnu_setup
  nufnu_setup={\
    'components':['mcspecfitfun_lucas'],\
    'para_num':[8],\
    'yrange':[0.001,1.e15],\
    'xrange':[1.,1.e8],\
    'logflag':par_log_flag\
    }
  print("end of setting lucas_8par")

#Part3ends
#####################################
