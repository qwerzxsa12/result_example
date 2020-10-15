global mcspecfit_Zhao_Lucas,mcspecfitfun_Zhao_Lucas
#from zbbpy import mcspecfitfun_cutoffpl
if(spec_mo == "mcspecfit_Zhao_Lucas"):
  setpar_arr=[\
    'mcspecfit_Zhao_Lucas.p1',\
    'mcspecfit_Zhao_Lucas.p2',\
    'mcspecfit_Zhao_Lucas.p3',\
    'mcspecfit_Zhao_Lucas.p4',\
    'mcspecfit_Zhao_Lucas.p5',\
    'mcspecfit_Zhao_Lucas.p6',\
    'mcspecfit_Zhao_Lucas.p7',\
    'mcspecfit_Zhao_Lucas.p8'\
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
    'components':['mcspecfitfun_Zhao_Lucas'],\
    'para_num':[8],\
    'yrange':[0.001,1.e15],\
    'xrange':[1.,1.e8],\
    'logflag':par_log_flag\
    }
  print("end of setting lucas_8par")

