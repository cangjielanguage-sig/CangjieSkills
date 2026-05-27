## 使用AudioRenderer播放对端的通话声音

该过程与[使用AudioRenderer开发音频播放功能](./cj-using-audiorenderer-for-playback.md)过程相似，关键区别在于audioRendererInfo参数和音频数据来源。audioRendererInfo参数中，音频内容类型需设置为语音：CONTENT_TYPE_SPEECH，音频流使用类型需设置为VOIP通话：STREAM_USAGE_VOICE_COMMUNICATION。

1. 获取Context。

    ```cangjie
    // main_ability.cj
    import kit.UIKit.AppLog
    import kit.ArkUI.WindowStage
    import kit.AbilityKit.*
    var globalContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

    class MainAbility <: UIAbility {
        public init() {
            super()
            registerSelf()
        }

        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            AppLog.info("MainAbility OnCreated.${want.abilityName}")
            // 获取context
            globalContext = this.context
            match (launchParam.launchReason) {
                case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
                case _ => ()
            }
        }

        public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            AppLog.info("MainAbility onWindowStageCreate.")
            windowStage.loadContent("EntryView")
        }
        // ...
    }
    ```

2. 使用AudioRenderer实现音频输出。

    ```cangjie
    import ohos.component.Button
    import ohos.state_macro_manage.*
    import kit.AudioKit.*
    import kit.CoreFileKit.*
    import ohos.base.*

    var bufferSize: Int64 = 0
    var renderModel: Option<AudioRenderer> = Option<AudioRenderer>.None
    let audioStreamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_2, // 通道
        AudioEncodingType.ENCODING_TYPE_RAW, // 编码格式
        AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
        AudioSamplingRate.SAMPLE_RATE_48000 // 采样率
    )
    let audioRendererInfo = AudioRendererInfo(
        StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型：VOIP通话
        0 // 音频渲染器标志：默认为0即可
    )
    let audioCapturerOptions = AudioRendererOptions(audioRendererInfo, audioStreamInfo)

    // 自定义AudioRender AR_STATE_CHANGE事件的回调
    class AudioRenderStateChangeCallback <: Callback1Argument<AudioState> {
        public func invoke(arg: AudioState) {
            AppLog.info("AudioRenderStateChangeCallback audio renderer state is: ${arg}")
        }
    }

    // 自定义AudioRender AR_MARK_PEACH事件的回调
    class MarkPeachCallback <: Callback1Argument<Int64> {
        public func invoke(arg: Int64) {
            AppLog.info("MarkPeachCallback: ${arg}")
        }
    }
    // 自定义AudioRender AR_WRITE_DATA事件的回调
    class WriteDataCallback <: Callback1ArgumentWithReturn<Array<Byte>, AudioDataCallbackResult> {
        public func invoke(arg: Array<Byte>): AudioDataCallbackResult {
            AppLog.info("AudioRender WriteDataCallback: ${arg.size}")
            let path = globalContext.getOrThrow().cacheDir
            // 确保该沙箱路径下存在该资源
            let filePath = path + '/StarWars10s-2C-48000-4SW.wav'
            let file: File = FileFs.open(filePath, mode: READ_ONLY.mode)
            AppLog.info("AudioRender WriteDataCallback open success, path: ${filePath}")

            let len = FileFs.read(file.fd, arg, options: ReadOptions(length: UIntNative(arg.size), offset: bufferSize))
            AppLog.info("AudioRender WriteDataCallback read len: ${len}")
            bufferSize += len
            return AudioDataCallbackResult.VALID
        }
    }

    // 初始化，创建实例，设置监听事件
    func initAudioRender() {
        try {
            // 创建AudioRenderer实例
            renderModel = createAudioRenderer(audioCapturerOptions)
            AppLog.info("createAudioRenderer success")