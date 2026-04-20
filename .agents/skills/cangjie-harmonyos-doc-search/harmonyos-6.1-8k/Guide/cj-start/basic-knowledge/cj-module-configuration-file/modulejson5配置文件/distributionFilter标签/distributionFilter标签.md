## distributionFilter标签

该标签用于定义HAP对应的细分设备规格的分发策略，以便在应用市场进行云端分发应用包时做精准匹配。

- **适用场景：** 当一个工程中存在多个Entry，且多个Entry配置的deviceTypes存在交集时，则需要通过该标签进行区分。比如下面的两个Entry都支持tablet类型，就需要通过该标签进行区分。

   ```json
   // entry1支持的设备类型
   {
     "module": {
       "name": "entry1",
       "type": "entry",
       "deviceTypes" : [
         "2in1",
         "tablet"
       ]
     }
   }
   ```

   ```json
   // entry2支持的设备类型
   {
     "module": {
       "name": "entry2",
       "type": "entry",
       "deviceTypes" : [
         "tablet"
       ]
     }
   }
   ```

- **配置规则：** 该标签支持配置四个属性，包括屏幕形状([screenShape](#screenshape标签))、窗口分辨率([screenWindow](#screenwindow标签))、屏幕像素密度([screenDensity](#screendensity标签) )、设备所在国家与地区([countryCode](#countrycode标签))。详见下表。

    在分发应用包时，通过deviceTypes与这四个属性的匹配关系，唯一确定一个用于分发到设备的HAP。

    - 如果需要配置该标签，则至少包含一个属性。
    - 如果一个Entry中配置了任意一个或多个属性，则其他Entry也必须包含相同的属性。
    - `screenShape`和`screenWindow`属性仅适用于轻量级智能穿戴设备。

- **配置方式：** 该标签需要配置在/resources/base/profile资源目录下，并在metadata的resource字段中引用。

**表12** distributionFilter标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| [screenShape](#screenshape标签) | 标识屏幕形状的支持策略。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [screenWindow](#screenwindow标签) | 标识应用运行时的窗口分辨率的支持策略。| 对象数组 | 该标签可缺省，缺省值为空。 |
| [screenDensity](#screendensity标签) | 标识屏幕的像素密度（dpi：Dot&nbsp;Per&nbsp;Inch）的支持策略。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [countryCode](#countrycode标签) | 标识国家与地区的支持策略，取值参考ISO-3166-1标准。支持多个国家和地区枚举定义。 | 对象数组 | 该标签可缺省，缺省值为空。 |