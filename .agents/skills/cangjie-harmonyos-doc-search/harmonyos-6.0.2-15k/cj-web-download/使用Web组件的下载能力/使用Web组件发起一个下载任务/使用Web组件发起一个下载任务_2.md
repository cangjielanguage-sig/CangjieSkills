// 获取context
        func getContext(): UIAbilityContext {
            match (globalAbilityContext) {
                case Some(context) => context
                case _ => throw Exception("can not get globalcontext")
            }
        }

        func build() {
            Column {
                Button("Add options").onClick {
                    evt => try {
                        delegate.onBeforeDownload {
                            webDownloadItem: WebDownloadItem =>
                            // 使用DocumentViewPicker()获取当前示例的默认下载目录，将该目录设置为下载目录
                            let documentSaveOptions = DocumentSaveOptions()
                            let documentPicker = DocumentViewPicker(getContext())
                            let saveCallback = {
                                errorCode: Option<AsyncError>, data: Option<Array<String>> => match (errorCode) {
                                    case Some(e) => AppLog.info("document save error: errcode is ${e.code}")
                                    case _ => match (data) {
                                        case Some(value) =>
                                            AppLog.info("documentUris is ${value}")
                                            if (value.size <= 0) {
                                                AppLog.info("documentUris empty")
                                                return
                                            }
                                            let uriString = value[0]
                                            if (uriString.isEmpty()) {
                                                AppLog.info("documentUris empty")
                                                return
                                            }
                                            let uri = FileUri(uriString)
                                            webDownloadItem.start(uri.path + '/' + webDownloadItem.getSuggestedFileName())
                                        case _ => AppLog.error("document save error: data is null")
                                    }
                                }
                            }
                            documentPicker.save(saveCallback)
                        }
                        delegate.onDownloadUpdated {
                            webDownloadItem: WebDownloadItem =>
                            // 下载任务的唯一标识。
                            AppLog.info("download update guid: ${webDownloadItem.getGuid()}")
                            // 下载的进度。
                            AppLog.info("download update percent complete: ${webDownloadItem.getPercentComplete()}")
                            // 当前的下载速度。
                            AppLog.info("download update speed: ${webDownloadItem.getCurrentSpeed()}")
                        }
                        delegate.onDownloadFailed {
                            webDownloadItem: WebDownloadItem =>
                            AppLog.info("download failed guid: ${webDownloadItem.getGuid()}")
                            // 下载任务失败的错误码。
                            AppLog.info("download failed last error code: ${webDownloadItem.getLastErrorCode()}")
                        }
                        delegate.onDownloadFinish {
                            webDownloadItem: WebDownloadItem => AppLog.info(
                                "download finish guid: ${webDownloadItem.getGuid()}")
                        }
                        webController.setDownloadDelegate(this.delegate)
                    } catch (e: BusinessException) {
                        AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }
                Web(src: @rawfile("index_download.html"), controller: this.webController)
            }
        }
    }
    ```