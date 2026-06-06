## 使用AudioCapturer录制本端的通话声音

该过程与[使用AudioCapturer开发音频录制功能](./cj-using-audiocapturer-for-recording.md)过程相似，关键区别在于audioCapturerInfo参数和音频数据流向。audioCapturerInfo参数中音源类型需设置为语音通话：SOURCE_TYPE_VOICE_COMMUNICATION。

所有录制均需要申请麦克风权限：`ohos.permission.MICROPHONE`，申请方式请参见[向用户申请授权](../../security/AccessToken/cj-request-user-authorization.md)。

1. 获取Context。

    ```cangjie
    // main_ability.cj
    import kit.AbilityKit.*
    import kit.UIKit.AppLog
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
        // ...
    }
    ```

2. 使用AudioCapturer录制本端的通话声音

    ```cangjie
    import kit.AudioKit.*
    import kit.CoreFileKit.*
    import ohos.base.*

    // 与使用AudioCapturer开发音频录制功能过程相似，关键区别在于audioCapturerInfo参数和音频数据流向
    var bufferSize: Int64 = 0
    var audioCapturer: Option<AudioCapturer> = Option<AudioCapturer>.None
    let audioStreamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_2, // 通道
        AudioEncodingType.ENCODING_TYPE_RAW, // 编码格式
        AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
        AudioSamplingRate.SAMPLE_RATE_48000 // 采样率
    )
    let audioCapturerInfo = AudioCapturerInfo(
        SourceType.SOURCE_TYPE_VOICE_COMMUNICATION, // 音源类型：语音通话
        0 // 音频采集器标志：默认为0即可
    )

    class MarkPeachCallback <: Callback1Argument<Int64> {
        public func invoke(arg: Int64) {
            AppLog.info("MarkPeachCallback callback: ${arg}")
        }
    }

    class PeriodPeachCallback <: Callback1Argument<Int64> {
        public func invoke(arg: Int64) {
            AppLog.info("PeriodPeachCallback callback: ${arg}")
        }
    }

    class ReadDataCallback <: Callback1Argument<Array<Byte>> {
        public func invoke(arg: Array<Byte>) {
            AppLog.info("AudioCapturer ReadDataCallback callback: ${arg.size}")
            // globalContext在Ability中获取
            let path = globalContext.getOrThrow().cacheDir
            let filePath = path + '/StarWars10s-2C-48000-4SW.wav'
            let file: File = FileFs.open(filePath, mode: READ_WRITE.mode | CREATE.mode)
            AppLog.info("AudioCapturer ReadDataCallback open success, path: ${filePath}")
            let len = FileFs.write(file.fd, arg, options: WriteOptions(length: UIntNative(arg.size), offset: bufferSize))
            AppLog.info("AudioCapturer ReadDataCallback write len: ${len}")
            bufferSize += len
        }
    }

    // 初始化，创建实例，设置监听事件
    func initAudioCapturer() {
        let audioCapturerOptions = AudioCapturerOptions(audioCapturerInfo, audioStreamInfo)
        try {
            // 创建AudioCapturer实例
            audioCapturer = createAudioCapturer(audioCapturerOptions)
            AppLog.info("createAudioCapturerr success.")
            if (let Some(capturer) <- audioCapturer) {
                // 订阅markReach事件，当采集的帧数达到1000帧时触发回调
                capturer.on(AudioCapturerCallbackType.MARK_REACH, 1000, MarkPeachCallback())
                AppLog.info("on MARK_REACH success.")

                // 订阅periodReach事件，当采集的帧数每达到2000时触发回调
                capturer.on(AudioCapturerCallbackType.PERIOD_REACH, 2000, PeriodPeachCallback())
                AppLog.info("on PERIOD_REACH success.")

                // 订阅READ_DATA事件，当需要读取音频流数据时触发回调
                capturer.on(AudioCapturerCallbackType.READ_DATA, ReadDataCallback())
                AppLog.info("on READ_DATA success.")
            }
        } catch (e: BusinessException) {
            AppLog.error("startRender failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }