### init(String, UInt8, UInt64, PackingDynamicRange, Bool)

```cangjie
public init(format: String, quality: UInt8, bufferSize!: UInt64 = 0,
    desiredDynamicRange!: PackingDynamicRange = Sdr, needsPackProperties!: Bool = false)
```

**功能：** 创建PackingOption对象。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|format|String|是|-|目标格式。|
|quality|UInt8|是|-|1. 编码中设定输出图片质量的参数，该参数仅对JPEG图片和HEIF图片生效。取值范围：[0, 100]。0质量最低，100质量最高，质量越高生成图片所占空间越大。WebP、PNG等图片均为无损编码。<br> 2.sdr_astc_4x4编码中，可以设定输出图片质量的参数，可选参数：92、85。<br>3. sut编码中，设定输出图片质量可选参数：92。<br>4. hdr_astc_4x4编码中，可以设定输出图片质量的参数，可选参数：85。|
|bufferSize|UInt64|否|0|**命名参数。** 接收编码数据的缓冲区大小，单位为Byte。如果不设置大小，默认为25M。如果编码图片超过25M，需要指定大小。bufferSize需大于编码后图片大小。使用[packToFile](#func-packtofileimagesource-int32-packingoption)不受此参数限制。|
|desiredDynamicRange|[PackingDynamicRange](#enum-packingdynamicrange)|否|Sdr|**命名参数。** 目标动态范围。默认值为Sdr。|
|needsPackProperties|Bool|否|false|**命名参数。** 是否需要编码图片属性信息，例如EXIF。true表示需要，false表示不需要。默认值为false。|