### func transformPoint(VArray\<Float64,$2>)

```cangjie
public func transformPoint(options: VArray<Float64, $2>): Array<Float64>
```

**功能：** Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|VArray\<Float64,$2>|是|-|需要转换的坐标点。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|返回矩阵变换后的Point对象。|

### func translate(TranslateOption)

```cangjie
public func translate(option: TranslateOption): This
```

**功能：** Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。会改变调用该函数的原始矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[TranslateOption](#class-translateoption)|是|-|设置平移参数。|