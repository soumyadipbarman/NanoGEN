import FWCore.ParameterSet.Config as cms
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/s/sobarman/private/Gridpack/UNLOPS_CMSSW/date_26102021/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8aMCatNLOSettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
		'Merging:TMS = 10.',                         # merging scale value same as ptj in the MG runcard
		'Merging:nJetMax = 3',                       # maximal number of additional LO jets
	        'Merging:nJetMaxNLO = 2',                    # maximal number of additional NLO jets
     		'Merging:Process = pp>LEPTONS,NEUTRINOS',    # define process 
                'Merging:doUNLOPSLoop = on',                 # UNLOPS merging
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8aMCatNLOSettings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
                                    )
    )
)

