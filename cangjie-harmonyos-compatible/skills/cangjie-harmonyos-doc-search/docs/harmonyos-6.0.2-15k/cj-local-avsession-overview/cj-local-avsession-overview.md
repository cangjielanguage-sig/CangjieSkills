# 本地媒体会话概述

## 交互过程

本地媒体会话的数据源均在设备本地，交互过程如图所示。

![Local AVSession Interaction Process](figures/local-avsession-interaction-process.jpg)

此过程中涉及两大角色，媒体会话提供方和媒体会话控制方。

> **说明：**
>
> 媒体会话控制方为系统应用，三方应用可以成为媒体会话提供方。

本地媒体会话中，媒体会话提供方通过媒体会话管理器和媒体会话控制方进行信息交互：

1. 媒体会话提供方通过createAVSession创建AVSession对象。

2. 媒体会话提供方通过AVSession对象，设置会话元数据（媒体ID、标题、媒体时长等）、会话播放属性（播放状态、播放倍速、播放位置等）等。

3. 媒媒体会话控制方通过getController获取AVSessionController对象。

4. 媒体会话控制方通过AVSessionController对象可以监听对应会话元数据变化、播放属性变化等。

5. 媒体会话控制方通过AVSessionController对象还可以向媒体会话发送控制命令。

6. 媒体会话提供方通过AVSession对象可以监听来自媒体会话控制方的控制命令，例如：“play”播放、“playNext”播放下一首、“fastForward”快进、 “setSpeed”设置播放倍数等。

## 创建媒体会话

```cangjie
import ohos.base.*
import kit.AVSessionKit.*

// 创建session。
let ctx = Global.getStageContext() // 获取Context应用上下文请参见 [API 参考] -> [API参考概述] -> [开发说明] -> [仓颉示例代码说明]
let session: AVSession = createAVSession(ctx, 'SESSION_NAME', AVSessionType.SESSION_TYPE_AUDIO)
AppLog.info('session create done : sessionId : ${session.sessionId}')
```
