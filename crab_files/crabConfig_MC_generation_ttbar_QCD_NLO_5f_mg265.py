from CRABClient.UserUtilities import config 
config = config()

config.section_("General")
config.General.requestName = 'ttbar_QCD_NLO_5f_mg265-v2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../configs/Hadronizer_TuneCP5_13TeV_aMCatNLO_2p_LHE_pythia8_ttbar_QCD_NLO_5f_mg265_v2_cfg.py'
config.JobType.inputFiles = ['/afs/cern.ch/work/s/sobarman/private/Gridpack/MC@NLO-delta/date_17052021/ttbar_QCD_NLO_5f_mg265_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz']

config.section_("Data")
config.Data.outputPrimaryDataset = 'ttbar_QCD_NLO_5f_mg265-v2'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/sobarman/MC_NLO/'
config.Data.publication = False
config.Data.outputDatasetTag = 'Generator_Negative_weight'

config.section_("Site")
#config.Site.whitelist = ['T2_CH_CERN', 'T2_IT_Pisa', 'T2_RU_JINR','T2_DE_RWTH']
config.Site.storageSite = 'T2_IN_TIFR'
