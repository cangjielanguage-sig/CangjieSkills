# ohos.multimedia-avcast_picker_param（投播组件）

avcast_picker_param提供了ohos.multimedia.avcast_picker窗口状态枚举值。

## 导入模块

```cangjie
import kit.AVSessionKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## enum AVCastPickerState

```cangjie
public enum AVCastPickerState <: ToString & Equatable<AVCastPickerState> {
    | StateAppearing
    | StateDisappearing
    | ...
}
```

**功能：** 投播状态参数选项。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 20

**父类型：**

- ToString
- Equatable\<[AVCastPickerState](#enum-avcastpickerstate)>

### StateAppearing

```cangjie
StateAppearing
```

**功能：** 组件显示。

**起始版本：** 20

### StateDisappearing

```cangjie
StateDisappearing
```

**功能：** 组件消失。

**起始版本：** 20

### func !=(AVCastPickerState)

```cangjie
public operator func !=(other: AVCastPickerState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVCastPickerState](#enum-avcastpickerstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVCastPickerState)

```cangjie
public operator func ==(other: AVCastPickerState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVCastPickerState](#enum-avcastpickerstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|
