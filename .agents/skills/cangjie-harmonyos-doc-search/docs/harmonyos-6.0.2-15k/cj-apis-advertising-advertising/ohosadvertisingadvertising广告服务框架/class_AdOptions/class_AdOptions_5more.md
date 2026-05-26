## class AdOptions

```cangjie
public class AdOptions {
    public AdOptions(
        public let tagForChildProtection!: ?Int32 = -1,
        public let adContentClassification!: ?String = None,
        public let nonPersonalizedAd!: ?UInt32 = None,
        public let extraAttrs!: ?Array<Parameter> = None
    )
}
```

**功能：** 广告配置参数。

**系统能力：** SystemCapability.Advertising.Ads

**起始版本：** 19

### let adContentClassification

```cangjie
public let adContentClassification: ?String = None
```

**功能：** 设置广告内容分级上限。<br>- W：适合幼儿及以上年龄段观众的内容。<br>- PI：适合少儿及以上年龄段观众的内容。<br>- J：适合青少年及以上年龄段观众的内容。<br>- A：仅适合成人观众的内容。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let extraAttrs

```cangjie
public let extraAttrs: ?Array<Parameter> = None
```

**功能：** 自定义参数<br>- totalDuration：类型Int32，单位：s。贴片广告必填自定义参数，用于设置贴片广告展示时长。<br>- placementAdCountDownDesc：类型string。贴片广告可选自定义参数，用于设置贴片广告倒计时文案，该参数需要使用encodeURI()方法编码。填写了该参数，则展示倒计时文案，否则只展示倒计时。<br>- allowMobileTraffic：类型Int32。可选自定义参数，设置是否允许使用流量下载广告素材。0：不允许，1：允许，不设置以广告主设置为准。

**类型：** ?Array\<[Parameter](#class-parameter)>

**读写能力：** 只读

**起始版本：** 19

### let nonPersonalizedAd

```cangjie
public let nonPersonalizedAd: ?UInt32 = None
```

**功能：** 设置是否只请求非个性化广告。<br>- 0：请求个性化广告与非个性化广告。<br>- 1：只请求非个性化广告。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let tagForChildProtection

```cangjie
public let tagForChildProtection: ?Int32 = -1
```

**功能：** 设置儿童保护标签。<br>- -1：您不希望表明您的广告内容是否需要符合COPPA的规定。<br>- 0：表明您的广告内容不需要符合COPPA的规定。<br>- 1：表明您的广告内容需要符合COPPA的规定（该广告请求无法获取到任何广告）。

**类型：** ?Int32

**读写能力：** 只读

**起始版本：** 19