# Drebin Re-implementation

This repository contains our re-implementation of **Drebin** (*Drebin: Effective and Explainable Detection of Android Malware in Your Pocket*, NDSS 2014). The existing re-implementation versions of Drebin have some issues that prevent it from generating the expected results, so we rebuilt it again.

If you use this version in your project, please cite our paper:

**Jin Zhang, Chennan Zhang, Xiangyu Liu, Yuncheng Wang,** [**Wenrui Diao**](https://diaowenrui.github.io/), and **Shanqing Guo**.  
*"ShadowDroid: Practical Black-box Attack against ML-based Android Malware Detection."*  
The 27th IEEE International Conference on Parallel and Distributed Systems (ICPADS), Beijing, China, December 14–16, 2021.

## How to run this program?
### step 1:
Put the malware data set in the res/malware folder, and put the normal software data set in the res/benign folder.
### step 2:
python GetApkData.py
### step 3:
python train.py
