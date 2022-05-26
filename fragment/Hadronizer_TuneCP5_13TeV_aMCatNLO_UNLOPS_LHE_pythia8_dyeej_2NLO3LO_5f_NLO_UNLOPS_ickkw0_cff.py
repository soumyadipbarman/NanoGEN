import FWCore.ParameterSet.Config as cms
nlo_ids = [(0, 0), (1, 1), (2, 2)]
lo_ids = [(3, 1), (4, 2), (5, 3)]
nparton_mapping = [cms.PSet(idprup=cms.uint32(idprup), order=cms.string('NLO'), np=cms.uint32(np)) for idprup, np in nlo_ids]
nparton_mapping += [cms.PSet(idprup=cms.uint32(idprup), order=cms.string('LO'), np=cms.uint32(np)) for idprup, np in lo_ids]
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/s/sobarman/private/Generator/genproductions/bin/MadGraph5_aMCatNLO/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    ## new option ##
    nPartonMapping = cms.VPSet(*nparton_mapping)
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
