## enum ColoringStrategy

```cangjie
public enum ColoringStrategy <: Equatable<ColoringStrategy> {
    | Invert
    | ...
}
```

**功能：** 智能取色枚举类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ColoringStrategy](#enum-coloringstrategy)>

### Invert

```cangjie
Invert
```

**功能：** 设置前景色为控件背景色的反色。仅支持在foregroundColor中设置该枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ColoringStrategy)

```cangjie
public operator func ==(other: ColoringStrategy): Bool
```

**功能：** 判断两个ColoringStrategy枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColoringStrategy](#enum-coloringstrategy)|是|-|要比较的另一个ColoringStrategy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ColoringStrategy)

```cangjie
public operator func !=(other: ColoringStrategy): Bool
```

**功能：** 判断两个ColoringStrategy枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColoringStrategy](#enum-coloringstrategy)|是|-|要比较的另一个ColoringStrategy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|