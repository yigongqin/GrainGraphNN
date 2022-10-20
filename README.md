# GrainNN2: A dynamic heterogeneous graph neural network for large-scale 3D grain microstructure evolution.

## Build
use the local CUDA version
```
export TORCH=1.11.0+cu102
export CUDA=cu102
pip3 install -r requirements.txt
```

## Usage
training
```
python3 grainNN2.py train --mode=train
```

testing

```
python3 grainNN2.py test --mode=test
```
