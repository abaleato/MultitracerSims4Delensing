# MultitracerSims4Delensing
Given theoretical auto- and cross-spectra (see [arXiv:1705.02332](https://arxiv.org/abs/1705.02332)), generate Gaussian simulations of LSS tracers which are appropriately correlated with each other and with an input convergence. Then compute and implement the optimal co-adding weights as derived in [arXiv:1502.05356](https://arxiv.org/abs/1502.05356)
 for the purpose of delensing.

### Installation
```
python setup.py install
```
### Usage
Granted the hard-coded bits in multsims.get_multitracer_phi() relating to the number and nature of tracers, multipole ranges, etc are correct, the code is to be used as simply as
```
import multsims

simid = 0 #Simulation number
multsims.get_multitracer_phi(simid)
```
