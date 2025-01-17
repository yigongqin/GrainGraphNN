

class Updater(object):
    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

class Param(Updater):
    def __init__(self, iterable=(), **kwargs):
       super().__init__(iterable, **kwargs)



def regressor(model_id):


    Ct = 1
        
    hp_grid = {'lr':[50e-4, 10e-4, 20e-4],\
               'layer_size':[96, 64, 32],\
               'batch_size':[4, 2, 8, 16],\
               'decay_step':[10, 5, 20]}
        
    
    hp_size = [(len(v),k) for k, v in hp_grid.items()]
    hp_order = [0, 1, 2, 3]
    hp_size = [hp_size[i] for i in hp_order]

    param_dict = {}
    prev_dim = 1
    
    for grid_dim, param in hp_size:
        
        cur_dim = prev_dim*grid_dim
        
        
        param_idx = (model_id%cur_dim)//prev_dim
        param_dict.update({param:hp_grid[param][param_idx]})
        
        prev_dim = cur_dim
        

        
       
    param_dict['frames'] = 20   
    param_dict['frames'] = param_dict['frames']*Ct+1



    param_dict.update({'window':1, 'out_win':1, 'weight_decay':0, 'layers':1, \
                       'kernel_size':(3,), 'epoch':50, 'bias':True, 'model_list':[0]})


    return Param(param_dict)




def classifier(model_id):


        
    hp_grid = {'weight':[1, 2, 4, 8],\
               'batch_size':[2, 4, 8, 16],\
               'lr':[100e-4, 25e-4, 50e-4], \
               'decay_step':[10, 5, 20],\
               'hidden':[32, 24, 16]}
        
    
    hp_size = [(len(v),k) for k, v in hp_grid.items()]
    hp_order = [0, 1, 2, 3, 4]
    hp_size = [hp_size[i] for i in hp_order]

    param_dict = {}
    prev_dim = 1
    
    for grid_dim, param in hp_size:
        
        cur_dim = prev_dim*grid_dim
        
        
        param_idx = (model_id%cur_dim)//prev_dim
        param_dict.update({param:hp_grid[param][param_idx]})
        
        prev_dim = cur_dim
 
       
       
    param_dict['frames'] = 13

    param_dict.update({'window':1, 'out_win':1, 'layers':1,  'weight_decay':0, \
                       'layer_size':32, 'kernel_size':(3,), 'epoch':60, 'bias':True, 'model_list':[0]})


    return Param(param_dict)


def classifier_transfered(model_id):

    hp_grid = {'weight':[1],\
               'batch_size':[32],\
               'lr':[100e-4, 25e-4, 5e-4]}
                   
    """    
    hp_grid = {'lr_1':[0.01, 0.1, 1],\
               'lr_2':[0.01, 0.1, 1],\
               'lr':[5e-4, 20e-4, 100e-4, 400e-4]}
    """    
    
    hp_size = [(len(v),k) for k, v in hp_grid.items()]
    hp_order = [0, 1, 2]
    hp_size = [hp_size[i] for i in hp_order]

    param_dict = {}
    prev_dim = 1
    
    for grid_dim, param in hp_size:
        
        cur_dim = prev_dim*grid_dim
        
        
        param_idx = (model_id%cur_dim)//prev_dim
        param_dict.update({param:hp_grid[param][param_idx]})
        
        prev_dim = cur_dim
 
       
       
    param_dict['frames'] = 13

    param_dict.update({'window':3, 'out_win':1, 'layers':1,  'weight_decay':0, 'decay_step':10, \
                       'layer_size':96, 'kernel_size':(3,), 'epoch':20, 'bias':True, 'model_list':[0]})

    param_dict.update({'lr_1':1, 'lr_2':1}) 
    return Param(param_dict)

"""
frames_id = all_id//81
lr_id = (all_id%81)//27
layers_id = (all_id%27)//9
hd_id = (all_id%9)//3
owin_id = all_id%3
"""


