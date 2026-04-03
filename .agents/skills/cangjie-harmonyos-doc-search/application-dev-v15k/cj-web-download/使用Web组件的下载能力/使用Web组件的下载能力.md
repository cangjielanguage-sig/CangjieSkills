# 使用Web组件的下载能力

Web组件的下载功能要求应用通过调用[WebDownloadItem.start](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-startstring)来指定下载文件的保存路径。值得注意的是，WebDownloadItem.start并非启动下载，下载过程实际上在用户点击页面链接时即已开始。WebDownloadItem.start的作用是将已经下载到临时文件的部分移动到指定目标路径，后续未完成的下载的内容将直接保存到指定目标路径，临时目录位于`/data/storage/el2/base/cache/web/Temp/`。如果决定取消当前下载，应调用[WebDownloadItem.cancel](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-cancel)，此时临时文件将被删除。

如果不希望在WebDownloadItem.start之前将文件下载到临时目录，可以通过WebDownloadItem.cancel中断下载，后续可通过[WebDownloadManager.resumeDownload](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-resumedownloadwebdownloaditem)恢复中断的下载。