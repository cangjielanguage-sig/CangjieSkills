# Refresh

可以进行页面下拉操作并显示刷新动效的容器组件。

## 子组件

支持单个子组件。

## 创建组件

### init(RefreshParams, () -> Unit)

```cangjie
public init(refreshparams: RefreshParams, content: () -> Unit)
```

**功能：** 创建refresh组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|refreshparams|[RefreshParams](#class-refreshparams)|是|-|设置组件刷新时的参数。|
|content|()->Unit|是|-|声明容器子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。