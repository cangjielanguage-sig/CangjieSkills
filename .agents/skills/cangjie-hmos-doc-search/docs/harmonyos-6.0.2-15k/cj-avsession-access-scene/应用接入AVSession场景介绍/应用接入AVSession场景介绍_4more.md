# 应用接入AVSession场景介绍

音视频应用在实现音视频功能的同时，需要接入媒体会话即AVSession Kit，下文将提供一些典型的接入AVSession的展示和控制场景，方便开发者根据场景进行适配。

对于不同的场景，将会在系统的播控中心看到不同的UI呈现。同时，在不同的场景下，应用的接入处理也需要遵循不同的规范约束。

## 哪些场景下需要接入AVSession

AVSession会对后台的音频播放、VOIP通话做约束，所以通常来说，长音频应用、听书类应用、长视频应用、VOIP类应用等都需要接入AVSession。当应用在没有创建接入AVSession的情况下进行了上述业务，那么系统会在检测到应用后台时，停止对应的音频播放，静音通话声音，以达到约束应用行为的目的。这种约束，应用上架前在本地就可以验证。

对于其他使用到音频播放的应用，比如游戏，直播等场景，接入AVSession不是必选项，只是可选，取决于应用是否有后台播放的使用诉求。若应用需要后台播放，那么接入AVSession仍然是必须的，否则业务的正常功能会受到限制。

当应用需要实现后台播放等功能时，需要使用[BackgroundTasks Kit](../../task-management/cj-background-task-overview.md)（后台任务管理）的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。

## 接入流程

应用接入AVSession流程分为如下几个步骤：

1. 确定应用需要创建的会话类型，[创建对应的会话](#创建不同类型的会话)，不同类型决定了播控中心展示的控制模板样式。
2. 按需[创建后台任务](#创建后台任务)。
3. [设置必要的元数据（Metadata）](#设置元数据)，以在播控中心展示响应的信息，包括不限于：当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。
4. [设置播放相关的状态](#设置播放状态)，包括不限于：当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。
5. 按需[注册不同的控制命令](#注册控制命令)，包括不限于：播放/暂停、上下一首、快进快退、收藏、循环模式、进度条。
6. 应用退出或者无对应业务时，注销会话。

## 创建不同类型的会话

AVSession在构造方法中支持不同的类型参数，由 [AVSessionType](../../../API_Reference/source_zh_cn/apis/AVSessionKit/cj-apis-multimedia_avsession.md#enum-avsessiontype) 定义，不同的类型代表了不同场景的控制能力，对于播控中心来说，会展示不同的控制模版。

- SESSION_TYPE_AUDIO类型，播控中心的控制样式为：收藏，上一首，播放/暂停，下一首，循环模式。

- SESSION_TYPE_VIDEO类型，播控中心的控制样式为：快退，上一首，播放/暂停，下一首，快进。

- SESSION_TYPE_VOICE_CALL类型，通话类型。

    使用代码示例：

    ```cangjie
    import kit.AVSessionKit.*
    import ohos.base.*

    // 开始创建并激活媒体会话。
    // 创建session。
    let context = Global.getStageContext() // 获取Context应用上下文请参见 [API 参考] -> [API参考概述] -> [开发说明] -> [仓颉示例代码说明]

    func createSession() {
        let `type`: AVSessionType = AVSessionType.SESSION_TYPE_AUDIO
        let session = createAVSession(context, 'SESSION_NAME', `type`)

        // 激活接口要在元数据、控制命令注册完成之后再执行。
        session.activate()
        AppLog.info("session create done : sessionId : ${session.sessionId}")
    }
    ```