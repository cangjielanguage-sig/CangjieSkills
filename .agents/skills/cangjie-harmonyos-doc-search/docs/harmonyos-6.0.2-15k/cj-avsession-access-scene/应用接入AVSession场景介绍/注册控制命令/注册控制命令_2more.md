## 注册控制命令

应用接入AVSession，可以通过注册不同的控制命令来实现播控中心界面上的控制操作，即通过on接口注册不同的控制命令参数，即可实现对应的功能。
具体的接口参考[接口注册](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#func-onavsessioneventtype-callback0argument)。

> **说明：**
>
> 创建AVSession后，请先注册应用支持的控制命令，再激活Session

媒体资源支持的控制命令列表：

| 控制命令 | 功能说明   |
| ------  | -------------------------|
| play    | 播放命令。 |
| pause    | 暂停命令。 |
| stop    | 停止命令。 |
| playNext    | 播放下一首命令。 |
| playPrevious    | 播放上一首命令。 |
| fastForward    | 快进命令。 |
| rewind    | 快退命令。 |
| playFromAssetId    | 根据某个资源id进行播放命令。 |
| seek    | 跳转命令。 |
| setSpeed    | 设置播放速率命令。 |
| setLoopMode    | 设置循环模式命令。 |
| toggleFavorite    | 设置是否收藏命令。 |
| skipToQueueItem    | 设置播放列表其中某项被选中播放的命令。 |
| handleKeyEvent    | 设置按键事件的命令。 |
| commonCommand    | 设置自定义控制命令。 |

通话类应用支持的控制：

| 控制命令 | 功能说明   |
| ------  | -------------------------|
| answer    | 接听电话的命令。 |
| hangUp    | 通话挂断的命令。 |
| toggleCallMute    | 通话静音或解除静音的命令。 |

### 不支持命令的处理

系统支持的控制命令对于不支持的控制，比如应用不支持“上一首”的命令处理，只需要使用off 接口注销对应的控制命令，系统的播控中心会相应的对该控制界面进行置灰处理，以明确告知用户此控制命令不支持。

```cangjie
import kit.AVSessionKit.*

let context = Global.getStageContext() // 获取Context应用上下文请参见 [API 参考] -> [API参考概述] -> [开发说明] -> [仓颉示例代码说明]

func unregisterSessionListener() {
    let `type`: AVSessionType = AVSessionType.SESSION_TYPE_AUDIO
    // 假设已经创建了一个session，如何创建session可以参考之前的案例。
    let session = createAVSession(context, 'SESSION_NAME', `type`)

    // 取消指定session下的相关监听。
    session.off(AVSessionEventType.Play)
    session.off(AVSessionEventType.Pause)
    session.off(AVSessionEventType.Stop)
    session.off(AVSessionEventType.PlayNext)
    session.off(AVSessionEventType.PlayPrevious)
}
```