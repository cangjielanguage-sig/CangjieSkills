# Checkbox

多选框组件，通常用于某选项的打开或关闭。

## 子组件

无

## 创建组件

### init(String, String, ?() -> Unit)

```cangjie
public init(name!: String = "", group!: String = "", indicatorBuilder!: ?()->Unit = None)
```

**功能：** 创建多选框组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|否|""| **命名参数。** 多选框名称。|
|group|String|否|""| **命名参数。** 用于指定多选框所属群组的名称（即所属[CheckboxGroup](./cj-button-picker-checkboxgroup.md#checkboxgroup)的名称）。<br/>**说明**：<br/>未配合使用[CheckboxGroup](./cj-button-picker-checkboxgroup.md#checkboxgroup)组件时，此值无用。|
|indicatorBuilder|?()->Unit|否|None| **命名参数。** 配置多选框的选中样式为自定义UI描述。自定义UI描述与Checkbox组件为中心点对齐显示。indicatorBuilder设置为None时，默认为indicatorBuilder未设置状态。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。