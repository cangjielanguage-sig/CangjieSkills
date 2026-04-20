## class EdgeEffectOptions

```cangjie
public class EdgeEffectOptions {
    public EdgeEffectOptions (
        public let alwaysEnabled: Bool
    )
}
```

**功能：** 组件内容大小小于组件自身时，是否开启滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let alwaysEnabled

```cangjie
public let alwaysEnabled: Bool
```

**功能：** 组件内容大小小于组件自身时，设置是否开启滑动效果。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### EdgeEffectOptions(Bool)

```cangjie
public EdgeEffectOptions (
        public let alwaysEnabled: Bool
    )
```

**功能：** 构造一个EdgeEffectOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alwaysEnabled|Bool|是|-|组件内容大小小于组件自身时，设置是否开启滑动效果。设置为true开启滑动效果，设置为false关闭滑动效果。|

## enum ContentClipMode

```cangjie
public enum ContentClipMode {
    | CONTENT_ONLY
    | BOUNDARY
    | SAFE_AREA
}
```

**功能：** 表示滚动容器的内容裁剪模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

下图是组件配置了边距属性后的示意图，可理解每种枚举对应的裁剪区域。

![shape2](./figures/scroll-swipe-common.png)

### BOUNDARY

```cangjie
BOUNDARY
```

**功能：** 按组件区域裁剪，对应图中的整个蓝色区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### CONTENT_ONLY

```cangjie
CONTENT_ONLY
```

**功能：** 按内容区裁剪，对应图中的绿色区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SAFE_AREA

```cangjie
SAFE_AREA
```

**功能：** 按组件配置的SafeArea区域裁剪，对应图中的整个黄色区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ScrollSnapAlign

```cangjie
public enum ScrollSnapAlign {
    | NONE
    | START
    | CENTER
    | END
}
```

**功能：** 设置列表项滚动结束对齐效果。

只支持item等高场景限位，不等高场景可能存在不准确的情况。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### CENTER

```cangjie
CENTER
```

**功能：** 视图中的中间项将在列表中心对齐。

**起始版本：** 19

### END

```cangjie
END
```

**功能：** 视图中的最后一项将在列表末尾对齐。

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 默认无项目滚动对齐效果。

**起始版本：** 19

### START

```cangjie
START
```

**功能：** 视图中的第一项将在列表的开头对齐。