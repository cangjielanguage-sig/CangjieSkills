### HdrStaticMetadata(Array\<Float32>, Array\<Float32>, Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public HdrStaticMetadata(
    public var displayPrimariesX: Array<Float32>,
    public var displayPrimariesY: Array<Float32>,
    public var whitePointX: Float32,
    public var whitePointY: Float32,
    public var maxLuminance: Float32,
    public var minLuminance: Float32,
    public var maxContentLightLevel: Float32,
    public var maxFrameAverageLightLevel: Float32
)
```

**功能：** 创建HdrStaticMetadata对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|displayPrimariesX|Array\<Float32>|是|-|归一化后显示设备三基色的X坐标，数组的长度为3，以0.00002为单位，范围[0.0, 1.0]。|
|displayPrimariesY|Array\<Float32>|是|-|归一化后显示设备三基色的Y坐标，数组的长度为3，以0.00002为单位，范围[0.0, 1.0]。|
|whitePointX|Float32|是|-|归一化后白点值的X坐标，以0.00002为单位，范围[0.0, 1.0]。|
|whitePointY|Float32|是|-|归一化后白点值的Y坐标，以0.00002为单位，范围[0.0, 1.0]。|
|maxLuminance|Float32|是|-|图像主监视器最大亮度。以1为单位，最大值为65535。|
|minLuminance|Float32|是|-|图像主监视器最小亮度。以0.0001为单位，最大值6.55535。|
|maxContentLightLevel|Float32|是|-|显示内容的最大亮度。以1为单位，最大值为65535。|
|maxFrameAverageLightLevel|Float32|是|-|显示内容的最大平均亮度，以1为单位，最大值为65535。|