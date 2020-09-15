# MC_NLO-delta
Madgraph fragments for MC@NLO-delta scheme

# Setup

```
cmsrel CMSSW_11_0_2
cd CMSSW_11_0_2/src
cmsenv
git cms-init
git cms-merge-topic kdlong:NanoGen_11_0_2
scram b -j 5

mkdir -p Configuration/GenProduction/
git clone git@github.com:cms-sw/genproductions.git Configuration/GenProduction/
cd Configuration
git clone git@github.com:kdlong/WMassNanoGen.git 
cd GenProduction/python
git clone git@github.com:soumyadipbarman/MC_NLO-delta.git
scram b
```

# Making configs and running
First create a config fragment in python subdirectory. All your config and fragment files must be placed in Configuration/GenProduction/python directory. Move all the config, fragment, crab_files from the folder MC_NLO-delta to Configuration/GenProduction/python and delete MC_NLO-delta folder.

generate the config for NanoGen with cmsDriver. If you want gridpack --> NanoGen, you can use the script [runCmsDriverNanoGen.sh](runCmsDriverNanoGen.sh). To generate a full config from your fragment and run:

```
scram b
./runCmsDriverNanoGen.sh <fragmentName_cff.py> <outputFile.root>
cmsRun fragmentName_cfg.py
```

Example crab submit files are in the crab_files directory. Note that you need to copy the gridpacks to a location readable from crab for this to work.

# Heavy Gridpack
For heavy size gridpack crab jobs will can't be submitted as regular procedure. The gridpack have to be uploaded to T2 or eos feom where xrootd service can be attend. First upload the gridpack to T2 or eos, then use crab script feature to submit the jobs. For that process [heavygridpack_script.sh](heavygridpack_script.sh) can be used. It copy the gridpack from T2 or eos to each worknode before the crab job starts. 
