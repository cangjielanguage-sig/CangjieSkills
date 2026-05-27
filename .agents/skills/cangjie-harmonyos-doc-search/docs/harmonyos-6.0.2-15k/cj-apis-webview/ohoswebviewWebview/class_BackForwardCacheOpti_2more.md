## class BackForwardCacheOptions

```cangjie
public class BackForwardCacheOptions  {
    public BackForwardCacheOptions (
        public var size: Int32,
        public var timeToLive: Int32
    )
}
```

**功能：** 前进后退缓存相关设置对象，用来控制Web组件前进后退缓存相关选项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var size

```cangjie
public var size: Int32
```

**功能：** 设置每个Web组件允许缓存的最大页面个数。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var timeToLive

```cangjie
public var timeToLive: Int32
```

**功能：** 设置每个Web组件允许页面在前进后退缓存中停留的时间，默认为600秒。设置为0或负数时，前进后退缓存功能不生效。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### BackForwardCacheOptions(Int32, Int32)

```cangjie
public BackForwardCacheOptions (
    public var size: Int32,
    public var timeToLive: Int32
)
```

**功能：** 构造BackForwardCacheOptions对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|是|-|设置每个Web组件允许缓存的最大页面个数。|
|timeToLive|Int32|是|-|设置每个Web组件允许页面在前进后退缓存中停留的时间，默认为600秒。设置为0或负数时，前进后退缓存功能不生效。|

## class BackForwardCacheSupportedFeatures

```cangjie
public class BackForwardCacheSupportedFeatures  {
    public BackForwardCacheSupportedFeatures (
        public var nativeEmbed: Bool,
        public var mediaTakeOver: Bool
    )
}
```

**功能：** 选择性允许使用以下特性的页面进入前进后退缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var mediaTakeOver

```cangjie
public var mediaTakeOver: Bool
```

**功能：** 是否允许使用视频托管的页面进入前进后退缓存。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var nativeEmbed

```cangjie
public var nativeEmbed: Bool
```

**功能：** 是否允许使用同层渲染的页面进入前进后退缓存。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### BackForwardCacheSupportedFeatures(Bool, Bool)

```cangjie
public BackForwardCacheSupportedFeatures (
    public var nativeEmbed: Bool,
    public var mediaTakeOver: Bool
)
```

**功能：** 构造BackForwardCacheSupportedFeatures的对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|nativeEmbed|Bool|是|-|是否允许使用同层渲染的页面进入前进后退缓存。|
|mediaTakeOver|Bool|是|-|是否允许使用视频托管的页面进入前进后退缓存。|