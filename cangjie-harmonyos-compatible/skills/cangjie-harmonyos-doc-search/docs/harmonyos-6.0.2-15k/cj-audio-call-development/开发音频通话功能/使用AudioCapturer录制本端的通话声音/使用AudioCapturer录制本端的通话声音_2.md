// 开始一次音频采集
    func start() {
        if (let Some(capturer) <- audioCapturer) {
            let stateGroup = [AudioState.STATE_PREPARED, AudioState.STATE_PAUSED, AudioState.STATE_STOPPED]
            if (stateGroup.indexOf(capturer.state) == -1) { // 当且仅当状态为STATE_PREPARED、STATE_PAUSED和STATE_STOPPED之一时才能启动采集
                AppLog.error("AudioCapturer start failed.")
                return
            }
            // 启动采集
            try {
                capturer.start()
                AppLog.info("AudioCapturer started.")
            } catch (e: BusinessException) {
                AppLog.error("AudioCapturer start errCode: ${e.code}, errMessage: ${e.message}")
            }
        }
    }

    // 停止采集
    func stop() {
        if (let Some(capturer) <- audioCapturer) {
            // 只有采集器状态为STATE_RUNNING或STATE_PAUSED的时候才可以停止
            if (capturer.state != AudioState.STATE_RUNNING && capturer.state != AudioState.STATE_PAUSED) {
                AppLog.error("AudioCapturer stop failed, capturer is not running or paused.")
                return
            }
            // 停止采集
            try {
                capturer.stop()
                if (capturer.state == AudioState.STATE_STOPPED) {
                    AppLog.info("AudioCapturer stopped successfully.")
                    return
                }
                AppLog.error("AudioCapturer stopped failed.")
            } catch (e: BusinessException) {
                AppLog.error("AudioCapturer stop errCode: ${e.code}, errMessage: ${e.message}")
            }
        }
    }

    // 销毁实例，释放资源
    func release() {
        if (let Some(capturer) <- audioCapturer) {
            // 采集器状态不是STATE_RELEASED或STATE_NEW状态，才能release
            if (capturer.state == AudioState.STATE_RELEASED || capturer.state == AudioState.STATE_NEW) {
                AppLog.error("Capturer already released")
                return
            }
            // 释放资源
            try {
                capturer.release()
                audioCapturer = Option<AudioCapturer>.None
                if (capturer.state == AudioState.STATE_RELEASED) {
                    AppLog.info("AudioCapturer release successfully.")
                    return
                }
                AppLog.error("AudioCapturer release failed")
            } catch (e: BusinessException) {
                AppLog.error("AudioCapturer release errCode: ${e.code}, errMessage: ${e.message}")
            }
        }
    }
    ```