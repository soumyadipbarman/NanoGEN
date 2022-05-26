# Setup

```
cmsrel CMSSW_12_0_4 
cd CMSSW_12_0_4/src
cmsenv
mkdir Configuration
cd Configuration
git clone git@github.com:soumyadipbarman/NanoGEN.git
scram b
```
For Pythia8.306 CMSSW_12_0_4 \
For Pythia8.2XX CMSSW_10_6_19

# Making configs and running
First create a config fragment in python subdirectory or copy fragment from [official genproduction repository](https://github.com/cms-sw/genproductions/tree/master/genfragments). All your fragment files must be placed in Configuration/NanoGEN/python directory. Configs, crab_files must be placed in Configuration/NanoGEN folder.

Generate config for NanoGen with cmsDriver. If you want gridpack --> NanoGen, you can use the script [runCmsDriverNanoGen.sh](runCmsDriverNanoGen.sh). To generate a full config from your fragment and run:

```
scram b
./runCmsDriverNanoGen.sh <fragmentName_cff.py> <outputFile.root>
cmsRun fragmentName_cfg.py
```

Example crab submit files are in the crab_files directory. Note that you need to copy the gridpacks to a location readable from crab for this to work.

# Heavy Gridpack
For heavy size gridpack crab jobs can't be submitted as regular procedure. The gridpack have to be uploaded to T2 or eos feom where xrootd service can be attend. First upload the gridpack to T2 or eos, then use crab script feature to submit the jobs. For that process [heavygridpack_script.sh](crab_files/heavygridpack_script.sh) can be used. It copy the gridpack from T2 or eos to each worknode before the crab job starts.

# More Info
This repository customized from [Kenneth Long's repository](https://github.com/kdlong/WMassNanoGen) \
Official NanoGEN [Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/NanoGen) \
Validation [Twiki](https://twiki.cern.ch/twiki/bin/view/CMS/GeneratorValidation#Validation_Workflow)

