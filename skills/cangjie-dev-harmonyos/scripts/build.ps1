ohpm.bat install --all --registry https://ohpm.openharmony.cn/ohpm/ --strict_ssl true

node "C:\czc\DevStudio\DevEco Studio\tools\hvigor\bin\hvigorw.js" --mode module -p module=entry@default SyncCangjieResource --analyze=normal --parallel --incremental --daemon

node "C:\czc\DevStudio\DevEco Studio\tools\hvigor\bin\hvigorw.js" --mode module -p product=default assembleHap --analyze=normal --parallel --incremental --daemon

