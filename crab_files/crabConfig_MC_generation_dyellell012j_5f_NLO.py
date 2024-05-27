from CRABClient.UserUtilities import config 
config = config()

config.section_("General")
config.General.requestName = 'dyellell012j_5f_NLO_FXFX'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/Hadronizer_TuneCP5_13TeV_aMCatNLO_FXFX_dyellell012j_5f_NLO_cfg.py'
config.JobType.inputFiles = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc700/13TeV/madgraph/V5_2.6.5/dy_fxfx_incl/dyellell012j_5f_NLO_FXFX_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz']

config.section_("Data")
config.Data.outputPrimaryDataset = 'dyellell012j_5f_NLO_FXFX'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/sobarman/MC_NLO/'
config.Data.publication = False
config.Data.outputDatasetTag = 'dyellell012j'

config.section_("Site")
#config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH']
config.Site.storageSite = 'T2_IN_TIFR'
