## class AdDisplayOptions

```cangjie
public class AdDisplayOptions {
    public AdDisplayOptions(
        public let customData!: ?String = None,
        public let userId!: ?String = None,
        public let useMobileDataReminder!: ?Bool = None,
        public let mute!: ?Bool = None,
        public let audioFocusType!: ?UInt32 = None,
        public let extraAttrs!: ?Array<Parameter> = None
    )
}
```

**功能：** 广告展示参数。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let audioFocusType

```cangjie
public let audioFocusType: ?UInt32 = None
```

**功能：** 视频播放过程中获得音频焦点的场景类型。<br>- 0：视频播放静音、非静音时都获取焦点。<br>- 1：视频静音播放时不获取焦点。<br>- 2：视频播放静音、非静音时都不获取焦点。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let customData

```cangjie
public let customData: ?String = None
```

**功能：** 媒体自定义数据。用于服务端通知媒体服务器某位用户因为与激励视频广告互动而应予以奖励，从而规避欺骗的行为。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let extraAttrs

```cangjie
public let extraAttrs: ?Array<Parameter> = None
```

**功能：** 自定义参数。<br>refreshTime：类型Int32，单位：ms，取值范围[30000, 120000]。AutoAdComponent组件可选自定义参数，用于控制广告的轮播时间间隔。填写了该参数，则广告按照参数配置的时间间隔轮播，否则广告不会轮播，只会展示广告响应中的第一个广告内容。

**类型：** ?Array\<[Parameter](#class-parameter)>

**读写能力：** 只读

**起始版本：** 19

### let mute

```cangjie
public let mute: ?Bool = None
```

**功能：** 广告视频播放是否静音。<br>- true：静音播放。<br>- false：非静音播放。

**类型：** ?Bool

**读写能力：** 只读

**起始版本：** 19

### let useMobileDataReminder

```cangjie
public let useMobileDataReminder: ?Bool = None
```

**功能：** 使用移动数据播放视频或下载应用时是否弹框通知用户。<br>- true：弹框通知。<br>- false：不弹框通知。

**类型：** ?Bool

**读写能力：** 只读

**起始版本：** 19

### let userId

```cangjie
public let userId: ?String = None
```

**功能：** 媒体自定义用户id。用于服务端通知媒体服务器某位用户因为与激励视频广告互动而应予以奖励，从而规避欺骗的行为。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19