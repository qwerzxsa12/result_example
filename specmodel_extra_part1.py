load_user_model(mcspecfitfun_Zhao_Lucas, "mcspecfit_Zhao_Lucas")
add_user_pars(str("mcspecfit_Zhao_Lucas"), \
        [   "p0"   "p1",   "p2",    "p3",   'p4',  'p5',  'p6',    'p7',    'p8'],\
        [    1,   500. ,  2.8,     5.,    42 ,   0,   30,          1,       1  ],\
        parmins=[0.,    2.0,   0.,  30,     0.,     1.0e-5,      0.01,           0.001 ],\
        parmaxs=[100000, 100.0,    20,    100,    1.e20,   1.0e20,        200.5,        300.0 ])
mcspecfit_Zhao_Lucas.integrate=True
