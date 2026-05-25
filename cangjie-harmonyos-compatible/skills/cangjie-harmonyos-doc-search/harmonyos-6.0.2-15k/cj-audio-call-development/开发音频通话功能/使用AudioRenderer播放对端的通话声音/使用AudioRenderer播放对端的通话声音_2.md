if (let Some(render) <- renderModel) {
                // 监听状态变化事件，当转换到指定的状态时触发回调
                render.on(AudioRendererCallbackType.AR_STATE_CHANGE, AudioRenderStateChangeCallback())
                // 订阅markReach事件，当渲染的帧数达到1000帧时触发回调
                render.on(AudioRendererCallbackType.AR_MARK_PEACH, 1000, MarkPeachCallback())
                // 监听音频数据写入回调事件（当需要写入音频数据时触发）
                render.on(AudioRendererCallbackType.AR_WRITE_DATA, WriteDataCallback())
            }
        } catch (e: BusinessException) {
            AppLog.error("initAudioRender failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }

    // 开始一次音频渲染
    func startRender() {
        try {
            if (let Some(render) <- renderModel) {
                let stateGroup = [AudioState.STATE_PREPARED, AudioState.STATE_PAUSED, AudioState.STATE_STOPPED]
                if (stateGroup.indexOf(render.state) == -1) { // 当且仅当状态为STATE_PREPARED、STATE_PAUSED和STATE_STOPPED之一时才能启动渲染
                    AppLog.warn("start render failed")
                    return
                }
                render.start()
                AppLog.info("start render success")
            }
        } catch (e: BusinessException) {
            AppLog.error("startRender failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }

    // 暂停渲染
    func pauseRender() {
        try {
            if (let Some(render) <- renderModel) {
                // 只有渲染器状态为STATE_RUNNING的时候才能暂停
                if (render.state != AudioState.STATE_RUNNING) {
                    AppLog.warn("Renderer is not running")
                    return
                }
                // 暂停渲染
                render.pause()
                if (render.state == AudioState.STATE_PAUSED) {
                    AppLog.info("Renderer is paused")
                } else {
                    AppLog.error("Pausing renderer failed.")
                }
            }
        } catch (e: BusinessException) {
            AppLog.error("pauseRender failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }

    // 停止渲染
    func stopRender() {
        try {
            if (let Some(render) <- renderModel) {
                // 只有渲染器状态为STATE_RUNNING或STATE_PAUSED的时候才可以停止
                if (render.state != AudioState.STATE_RUNNING && render.state != AudioState.STATE_PAUSED) {
                    AppLog.warn("Renderer is not running or paused.")
                    return
                }
                // 停止渲染
                render.stop()
                if (render.state == AudioState.STATE_STOPPED) {
                    AppLog.info("Renderer is stopped")
                } else {
                    AppLog.error("Stopping renderer failed.")
                }
            }
        } catch (e: BusinessException) {
            AppLog.error("stopRender failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }

    // 销毁实例，释放资源
    func releaseRender() {
        try {
            if (let Some(render) <- renderModel) {
                // 渲染器状态不是STATE_RELEASED状态，才能release
                if (render.state == AudioState.STATE_RELEASED) {
                    AppLog.info("Renderer already released")
                    return
                }
                // 释放资源
                render.release()
                if (render.state == AudioState.STATE_RELEASED) {
                    AppLog.info("Renderer is released")
                } else {
                    AppLog.error("Renderer release failed.")
                }
            }
        } catch (e: BusinessException) {
            AppLog.error("stopRender failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }

    @Entry
    @Component
    class EntryView {
        func build() {
            Row {
                Column {
                    Button("init").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                        evt => initAudioRender()
                    }
                    Button("start").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                        evt => startRender()
                    }
                    Button("pause").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                        evt => pauseRender()
                    }
                    Button("stop").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                        evt => stopRender()
                    }
                    Button("release").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                        evt => releaseRender()
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```