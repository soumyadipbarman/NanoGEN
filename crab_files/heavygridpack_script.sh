echo "================= CMSRUN starting ====================" 
# you have to change only this line. Just give the right path of the gridpack from T2 storage /eos path
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt012j_5f_ckm_NLO_FXFX_mg265_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt012j_5f_ckm_NLO_FXFX_mg273_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt012j_5f_ckm_NLO_FXFX_MCNLO-delta_111_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt01j_5f_ckm_NLO_FXFX_MCNLO-delta_111_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD 
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt01j_5f_ckm_NLO_FXFX_MCNLO-delta_221_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt01j_5f_ckm_NLO_FXFX_MCNLO-delta_441_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/ttbar_QCD_NLO_5f_MCNLO-delta_111_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/ttbar_QCD_NLO_5f_MCNLO-delta_221_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/ttbar_QCD_NLO_5f_MCNLO-delta_441_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/date_17052021/tt012j_5f_ckm_NLO_FXFX_MCNLO-delta_221_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/UNLOPS/date_26102021/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/UNLOPS/date_26102021/dyee012j_5f_NLO_FXFX_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/UNLOPS/date_15012022/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/UNLOPS/2NLO3LO_icckw0/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/UNLOPS/date_30042022/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
#xrdcp root://cms-xrd-global.cern.ch//store/user/sobarman/Gridpack/UNLOPS/date_06062022/dyee012j_5f_NLO_UNLOPS_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $PWD
cmsRun -j FrameworkJobReport.xml -p PSet.py
echo "================= CMSRUN finished ===================="
