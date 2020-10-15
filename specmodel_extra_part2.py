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


def mcspecfitfun_Zhao_Lucas(p,xlo,xhi=None):
	global redshift_lucas
	import numpy as np
	from zbbpy import zbblogen
	if(np.array(xhi).any() != None):
		dx=np.array(xhi)-np.array(xlo)
		x=np.sqrt(np.array(xlo)*np.array(xhi))
	else:
		dx=np.array(xlo)**0.
		x=np.array(xlo)
	P=p[0:9]
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
        model_Kind = P[0]
	Gamma=P[1]
	p_e=P[2]
	log10ginj=P[3]
	log10inj_rate_0=P[4]
	q=P[5]
	B0=P[6]
	b=P[7]
	t_obs=P[8]
	import subprocess
        p0_str=str(Decimal(model_Kind))
	p1_str=str(Decimal(Gamma))
	p2_str=str(Decimal(p_e))
	p3_str=str(Decimal(log10ginj))
	p4_str=str(Decimal(log10inj_rate_0))
	p5_str=str(Decimal(q))
	p6_str=str(Decimal(B0))
	p7_str=str(Decimal(b))
	p8_str=str(Decimal(t_obs))
	redshift_str=str(Decimal(redshift_lucas))
        if(p0_str == 1):
                p0_str = "Lucas"
	cmd_zxh='./Zhao_Zhang_blackbox_v3.exe'
	para_str=' '+p0_str+" "+p1_str+" "+p2_str+' '+\
		p3_str+' '+p4_str+' '+p5_str+' ' +p6_str+' '+p7_str+' '+ p8_str+' '+\
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
