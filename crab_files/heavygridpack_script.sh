echo "================= CMSRUN starting ====================" 
# you have to change only this line. Just give the right path of the gridpack from T2 storage /eos path
xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/ttbar_QCD_NLO_5f_MCNLO-delta_441_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD 
cmsRun -j FrameworkJobReport.xml -p PSet.py
echo "================= CMSRUN finished ===================="
