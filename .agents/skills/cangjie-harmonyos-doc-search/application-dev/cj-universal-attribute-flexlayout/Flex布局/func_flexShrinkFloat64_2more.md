## func flexShrink(?Float64)

```cangjie
func flexShrink(value: ?Float64): T
```

**功能：** 设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|父容器压缩尺寸分配给此属性所在组件的比例。<br> 父容器为[Column](./cj-row-column-stack-column.md)、[Row](./cj-row-column-stack-row.md)时，取值范围(0,+∞)，初始值为0.0。 <br>父容器为[Flex](./cj-row-column-stack-flex.md)时，初始值：1.0。<br>[constraintSize](./cj-universal-attribute-layoutconstraints.md#func-constraintsizelength-length-length-length)限制组件的尺寸范围，[Column](./cj-row-column-stack-column.md)和[Row](./cj-row-column-stack-row.md)即使设置了[constraintSize](./cj-universal-attribute-layoutconstraints.md#func-constraintsizelength-length-length-length)，在未设置主轴尺寸（[width](./cj-universal-attribute-size.md#func-widthoptionlength)/[height](./cj-universal-attribute-size.md#func-heightoptionlength)/[size](./cj-universal-attribute-size.md#func-sizelength-length)时仍遵守默认布局行为，在主轴上自适应子组件尺寸，此时flexShrink不生效。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func flexShrink(?Int64)

```cangjie
func flexShrink(value: ?Int64): T
```

**功能：** 设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int64|是|-|父容器压缩尺寸分配给此属性所在组件的比例。<br> 父容器为Column、Row时，初始值为0。 <br>父容器为Flex时，初始值为1。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|