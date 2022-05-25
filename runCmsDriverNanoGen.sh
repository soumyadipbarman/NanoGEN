#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -ne 2 ]]; then
    echo "Must have two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile.root>"
    exit 1
fi

fragment=${1/python\//}

cmsDriver.py Configuration/GenProduction/python/fragment/$fragment \
    --fileout file:$2 --mc --eventcontent NANOAODSIM \
    --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN \
    --python_filename configs/${fragment/cff/cfg} \
    --customise_commands "process.source.firstRun=cms.untracked.uint32(1)" \
    -n 100 --no_exec
