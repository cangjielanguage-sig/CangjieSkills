# 管理麦克风

因为在录制过程中需要使用麦克风录制相关音频数据，所以建议开发者在调用录制接口前查询麦克风状态，并在录制过程中监听麦克风的状态变化，避免影响录制效果。

在音频录制过程中，当用户将麦克风静音，录音过程会正常进行，录制生成的数据文件的大小随录制时长递增，但写入文件的数据均为0，即无声数据（空白数据）。

## 开发示例

在AudioVolumeGroupManager中提供了管理麦克风状态的方法，接口的详细说明请参见[API文档](../../../API_Reference/source_zh_cn/apis/AudioKit/cj-apis-multimedia-audio.md#class-audiovolumegroupmanager)。

```cangjie
// index.cj
import ohos.component.*
import kit.AudioKit.*
import ohos.base.*

var audioVolumeGroupManager: Option<AudioVolumeGroupManager> = Option<AudioVolumeGroupManager>.None

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column {
                Button("createAudioVolumeGroupManager").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                    evt => createAudioVolumeGroupManager()
                }
                Button("isMicMute").fontSize(20).margin(10).fontWeight(FontWeight.Bold).onClick {
                    evt => isMicMute()
                }
            }.width(100.percent)
        }.height(100.percent)
    }

    // 创建audioVolumeGroupManager对象
    func createAudioVolumeGroupManager() {
        try {
            audioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(
                DEFAULT_VOLUME_GROUP_ID)
            AppLog.info("loadVolumeGroupManager success")
        } catch (e: BusinessException) {
            AppLog.error("loadVolumeGroupManager errCode: ${e.code}, errMessage: ${e.message}")
        }
    }

    // 查询麦克风是否静音，返回true为静音，false为非静音
    func isMicMute() {
        try {
            if (let Some(v) <- audioVolumeGroupManager) {
                let isMute = v.isMicrophoneMute()
                AppLog.info("isMicMute: ${isMute}")
            }
        } catch (e: BusinessException) {
            AppLog.error("loadVolumeGroupManager errCode: ${e.code}, errMessage: ${e.message}")
        }
    }
}
```
