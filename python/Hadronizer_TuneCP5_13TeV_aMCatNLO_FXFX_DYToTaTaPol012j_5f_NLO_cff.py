import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/s/sobarman/public/forUlrich/dytautau012j_5f_NLO_FXFX_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#GS fragment

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
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 999.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 30.', #this is the actual merging scale
            'JetMatching:doFxFx = on',
            'JetMatching:qCutME = 10.',#this must match the ptj cut in the lhe generation step
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            'TimeShower:mMaxGamma = 4.0',
	    'TauDecays:externalMode = 0',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'pythia8aMCatNLOSettings',
                                    'processParameters',
                                    )
    ),
        ExternalDecays = cms.PSet(
        Photospp = cms.untracked.PSet(
            parameterSets = cms.vstring("setExponentiation", "setInfraredCutOff", "setCorrectionWtForW", "setMeCorrectionWtForW", "setMeCorrectionWtForZ", "setMomentumConservationThreshold", "setPairEmission", "setPhotonEmission", "setStopAtCriticalError", "suppressAll", "forceBremForDecay"),
            setExponentiation = cms.bool(True),
            setCorrectionWtForW = cms.bool(False),
            setMeCorrectionWtForW = cms.bool(False),
            setMeCorrectionWtForZ = cms.bool(False),
            setInfraredCutOff = cms.double(0.0000001),
            setMomentumConservationThreshold = cms.double(0.1),
            setPairEmission = cms.bool(False), # retain pair emission in MiNNLO x NLOEW / this
            setPhotonEmission = cms.bool(True),
            setStopAtCriticalError = cms.bool(False),
            # Use Photos only for W/Z decays
            suppressAll = cms.bool(True),
            forceBremForDecay = cms.PSet(
                parameterSets = cms.vstring("Z", "Wp", "Wm"),
                Z = cms.vint32(0, 23),
                Wp = cms.vint32(0, 24),
                Wm = cms.vint32(0, -24),
            ),
        ),
        parameterSets = cms.vstring("Photospp")
    )
)

ProductionFilterSequence = cms.Sequence(generator)
