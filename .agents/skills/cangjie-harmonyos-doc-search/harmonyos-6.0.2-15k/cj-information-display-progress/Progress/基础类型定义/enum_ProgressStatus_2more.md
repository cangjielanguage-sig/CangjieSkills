### enum ProgressStatus

```cangjie
public enum ProgressStatus {
    | LOADING
    | PROGRESSING
}
```

**功能：** Progress组件的进度条状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### LOADING

```cangjie
LOADING
```

**功能：** 加载中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PROGRESSING

```cangjie
PROGRESSING
```

**功能：** 进度更新中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum ProgressStyle

```cangjie
public enum ProgressStyle {
    | Linear
    | Ring
    | Eclipse
    | ScaleRing
    | Capsule
}
```

**功能：** Progress组件的样式类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Capsule

```cangjie
Capsule
```

**功能：** 胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同；中段处的进度展示效果与Linear相同。高度大于宽度的时候自适应垂直显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Eclipse

```cangjie
Eclipse
```

**功能：** 圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Linear

```cangjie
Linear
```

**功能：** 线性样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Ring

```cangjie
Ring
```

**功能：** 环形无刻度样式，环形圆环逐渐显示至完全填充效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ScaleRing

```cangjie
ScaleRing
```

**功能：** 环形有刻度样式，显示类似时钟刻度形式的进度展示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19