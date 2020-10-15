def lucas_8par_mod(p,xlo,xhi=None):
    import numpy as np
    # from zbbpy import lucas_8par
    from zbbpy import zbblogen
    # from scipy.interpolate import InterpolatedUnivariateSpline 
    # P=[1.e3, 2.3,1.0,1.0,1.5,1.e17] ; typical P
    if(xhi != None):
        dx=np.array(xhi)-np.array(xlo)
        x=np.sqrt(np.array(xlo)*np.array(xhi))
    else:
        dx=np.array(xlo)**0.
        x=np.array(xlo)
    P=p[0:8]
    # print(x)
    flux_arr=np.ndarray(len(x))
    for i in range(len(x)):
        flux_arr[i]=lucas_8par(x[i],P)
    return flux_arr

def lucas_8par(E,P):
    # print(P)
    # print('len=',len(P))
    import numpy as np 
    # print(E)
    nu=np.log10(E*2.41789894010E17)
    Gamma=P[0]
    p_e=P[1]
    log10ginj=P[2]
    log10inj_rate_0=P[3]
    q=P[4]
    B0=P[5]
    b=P[6]
    t_obs=P[7]
    


    import subprocess
    # import numpy as np
    from decimal import Decimal
    
    p0_str=str(Decimal(Gamma))
    p1_str=str(Decimal(p_e))
    p2_str=str(Decimal(log10ginj))
    p3_str=str(Decimal(log10inj_rate_0))
    p4_str=str(Decimal(q))
    p5_str=str(Decimal(B0))
    p6_str=str(Decimal(b))
    p7_str=str(Decimal(t_obs))
    nu_str=str(Decimal(nu))
    
    #cmd_zxh='~/CloudStation/ZXH_Fortran_Code/zxhflux_quick2'
    cmd_zxh='~/CloudStation/Lucas_blackBox/lucas_flux_9_par.exe'
    # cmd_zxh='~/CloudStation/ZXH_Fortran_Code/zxhflux_bkpl'
    
    para_str=' '+p0_str+" "+p1_str+" "+p2_str+' '+\
        p3_str+' '+p4_str+' '+p5_str+' ' +p6_str+' '+p7_str+' '+\
        nu_str+' '
    whole_cmd=cmd_zxh+' '+para_str
    # print(whole_cmd)
    from subprocess import Popen, PIPE
    p = Popen(whole_cmd,stdout=PIPE,shell=True,stderr=PIPE)
    (out,err) = p.communicate()
    tmp_str_list=out.split()
    result_tmp=np.ndarray(len(out.split()))*0.
    for i in range(len(result_tmp)):
        result_tmp[i]=np.float(tmp_str_list[i])

    result_tmp=(2418.0/1.602)*result_tmp/(E)
    flux=1.0*np.array(result_tmp)
    return flux
def lucas_8par_test():
    def test_inside():
        print('inside')
    
    test_inside()
    E=10.
    p=[500.,2.8,5.,47.,0.,30.,1.,1.]
    from zbbpy import zbblogen
    a=lucas_8par(E,p)
    # print(a)
    # print('---------')
    # E2=[10,20,30,50,100]
    # E2=zbblogen()
    E2=zbblogen(1.1,1.e4,200.)
    b=lucas_8par_mod(p,E2)
    # print(b)
    import matplotlib.pyplot as plt
    plt.plot(E2,b)
    plt.yscale('log')
    plt.xscale('log')
    
    plt.show()
# lucas_8par_test()

def zbb_plot_obs_th_spec(pha,bak,rmf,arf,mo,par,xobs,setpar_arr):
    print('-----')
    def model(par,mo,pha,rmf,arf,xobs,setpar_arr):
      pha_file_arr=pha
      rmf_arr=rmf
      arf_arr=arf
      spec_mo=mo
      x_obs_arr=xobs
      from zbbpy import zbb_userconv
      global lucas_8par
      from zbbpy import lucas_8par
      from scipy.interpolate import InterpolatedUnivariateSpline 
      ndim=len(par)
      par_values=par[0:ndim:]
      ymo_arr=[None for x in range(len(pha_file_arr))]
      for i in range(len(pha_file_arr)):
        print('i=',i)
        ch_now,ct_now,e_mid_mod_now=zbb_userconv(rmf_arr[i],arf_arr[i],spec_mo,par_values,setpar_arr)
        print(ct_now)
        f_inter_now=InterpolatedUnivariateSpline(e_mid_mod_now, ct_now,k=1)
        ct_new_now = f_inter_now(x_obs_arr[i])
        ymo_now=ct_new_now
        ymo_arr[i]=ymo_now
      return  ymo_arr
    yth=model(par,mo,pha,rmf,arf,xobs,setpar_arr)
    return yth
def zbb_plot_obs_th_spec_test():
    
    mo='lucas_8par' 
    pha=['/Users/bz//Daily_TTE/alpha_evo_140901a/lc/int12//n9/spec/pha.fits']
    bak=['/Users/bz//Daily_TTE/alpha_evo_140901a/lc/int12/n9/spec/bak.fits']
    rmf=['/Volumes/bz_storage/DATA/Daily_TTE/alpha_evo_140901a/download/burst_data/glg_cspec_n9_bn140901821_v00.rsp']
    arf=['none']
    par=[ 500 ,2.79999999999999982236431605997495353221893310546875, 5 ,47, 0, 30 ,1 ,1 ]
    from zbbpy import zbblogen

    xobs=zbblogen(200.,1.e4,100.)
    setpar_arr=[\
    'lucas_8par.p0',\
    'lucas_8par.p1',\
    'lucas_8par.p2',\
    'lucas_8par.p3',\
    'lucas_8par.p4',\
    'lucas_8par.p5',\
    'lucas_8par.p6',\
    'lucas_8par.p7'\
    ]

    yth=zbb_plot_obs_th_spec(pha,bak,rmf,arf,mo,par,xobs,setpar_arr)
    # print(xobs,yth)
    import matplotlib.pyplot as plt
    plt.plot(xobs,yth)
    plt.yscale('log')
    plt.xscale('log')
    
    plt.show()
zbb_plot_obs_th_spec_test()
