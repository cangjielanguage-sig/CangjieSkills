## enum AVPlayerState

```cangjie
public enum AVPlayerState <: Equatable<AVPlayerState> & ToString {
    | Idle
    | Initialized
    | Prepared
    | Playing
    | Paused
    | Completed
    | Stopped
    | Released
    | AVError
    | ...
}
```

**功能：** [AVPlayer](#class-avplayer)的状态机，可通过[state](#prop-state)属性主动获取当前状态，也可通过监听[StateChange](#func-onavplayercallbacktype-onavplayerstatechangehandle)事件上报当前状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**父类型：**

- Equatable\<AVPlayerState>
- ToString

### AVError

```cangjie
AVError
```

**功能：** 错误状态，当播放引擎发生不可逆的错误（详见Media错误码），则会转换至当前状态，可以调用[reset()](#func-reset)重置，也可以调用[release()](#func-release)销毁重建。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Completed

```cangjie
Completed
```

**功能：** 播放至结尾状态，当媒体资源播放至结尾时，如果用户未设置循环播放（loop = true），AVPlayer会进入completed状态，此时调用[play()](#func-play)会进入playing状态和重播，调用[stop()](#func-stop)会进入stopped状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Idle

```cangjie
Idle
```

**功能：** 闲置状态，AVPlayer刚被创建[createAVPlayer()](#func-createavplayer)或者调用了[reset()](#func-reset)方法之后，进入Idle状态。

首次创建[createAVPlayer()](#func-createavplayer)，所有属性都为默认值。

调用[reset()](#func-reset)方法，url或fdSrc及loop属性会被重置，其他用户设置的属性将被保留。

**起始版本：** 19

### Initialized

```cangjie
Initialized
```

**功能：** 资源初始化，在Idle状态设置url或fdSrc属性，AVPlayer会进入initialized状态，此时可以配置窗口、音频等静态属性。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Paused

```cangjie
Paused
```

**功能：** 暂停状态，在playing状态调用pause方法，AVPlayer会进入paused状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Playing

```cangjie
Playing
```

**功能：** 正在播放状态，在prepared/paused/completed状态调用[play()](#func-play)方法，AVPlayer会进入playing状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Prepared

```cangjie
Prepared
```

**功能：** 已准备状态，在initialized状态调用[prepare()](#func-prepare)方法，AVPlayer会进入prepared状态，此时播放引擎的资源已准备就绪。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Released

```cangjie
Released
```

**功能：** 销毁状态，销毁与当前AVPlayer关联的播放引擎，无法再进行状态转换，调用[release()](#func-release)方法后，会进入released状态，结束流程。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### Stopped

```cangjie
Stopped
```

**功能：** 停止状态，在prepared/playing/paused/completed状态调用[stop()](#func-stop)方法，AVPlayer会进入stopped状态，此时播放引擎只会保留属性，但会释放内存资源，可以调用[prepare()](#func-prepare)重新准备，也可以调用[reset()](#func-reset)重置，或者调用[release()](#func-release)彻底销毁。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19