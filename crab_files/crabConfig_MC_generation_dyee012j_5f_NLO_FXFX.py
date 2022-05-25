from CRABClient.UserUtilities import config 
config = config()

config.section_("General")
config.General.requestName = 'dyee012j_5f_NLO_FXFX_18112021'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/Hadronizer_TuneCP5_13TeV_aMCatNLO_FXFX_2p_LHE_pythia8_dyee012j_5f_NLO_FXFX_cfg.py'
config.JobType.scriptExe = 'heavygridpack_script.sh'  # For heavy tarball have to use script for coping tarball from T2 to worknode
#config.JobType.inputFiles = ['/afs/cern.ch/work/s/sobarman/private/MC@NLO/Gridpack/ttbar/date_07092020/ttbar_QCD_NLO_5f_MCNLO-delta_111_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']

config.section_("Data")
config.Data.outputPrimaryDataset = 'dyee012j_5f_NLO_FXFX_18112021'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/sobarman/UNLOPS'
config.Data.publication = False
config.Data.outputDatasetTag = 'UNLOPS_CMSSW'

config.section_("Site")
#config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH']
config.Site.storageSite = 'T2_IN_TIFR'
