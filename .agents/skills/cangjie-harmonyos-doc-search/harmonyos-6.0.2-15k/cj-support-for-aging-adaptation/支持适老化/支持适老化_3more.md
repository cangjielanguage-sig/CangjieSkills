# 支持适老化

系统字体被放大后，应用应确保整体布局不出现错乱，组件不出现重叠。可以根据业务需要限制跟随的字体最大档位、改变布局来更好的适配更大字体等。本文旨在指导应用如何跟随系统字体大小和跟随到的最大倍数。

## 应用适配规则

- 在系统使用1.75倍及以上的大字体时，页面布局不得错乱，组件不得叠加，文字不得截断。
- 图标及图片不会随着字体的变大而变化。
- 页面中不重要的内容字体，可采用不跟随系统字体变化或限制字体最大尺寸的方法进行布局。
- 若应用跟随系统字体增大后导致页面内容位置挤压或截断等问题，可采取将X轴扩展至Y轴的措施，例如将左右布局调整为上下布局。
- [系统组件](#适配适老化的系统组件及触发方式)已针对适老化大字体进行了单独适配，尽可能在开发过程中使用系统组件。

## 应用适配适老化大字体

- 开启路径

  在“设置-辅助功能-关怀模式-放大显示”中开启。

  各档位对应参数：

  |档位|字体大小|字体粗细|
  |:---|:---|:---|
  | 标准 | 1倍 | 1倍 |
  | 大1档 | 1.15倍 | 1倍 |
  | 大2档 | 1.3倍 | 1.1倍 |
  | 大3档 | 1.45倍 | 1.1倍 |
  | 大4档 | 1.75倍 | 1.25倍 |
  | 大5档 | 2.0倍 | 1.25倍 |
  | 大6档 | 3.2倍 | 1.25倍 |

- 适配方法

  当前默认应用不跟随系统字体的变化。如需跟随系统字体变化，并设置最大跟随变化的倍数，请按以下步骤操作：

    - app.json5配置文件适配。

        通过配置"configuration": "$profile:configuration"，指向base/profile/configuration.json文件；

        ```cangjie
        {
            "app": {
                "bundleName": "com.example.myapplication",
                "vendor": "example",
                "versionCode": 1000000,
                "versionName": "1.0.0",
                "icon": "$media:app_icon",
                "label": "$string:app_name",
                "configuration": "$profile:configuration"
            }
        }
        ```

    - 在AppScope/resources/base文件目录下新增profile文件夹，并在此目录下新增 configuration.json 文件。

        配置"fontSizeScale": "followSystem"表示该应用的字体大小将根据系统设置进行缩放，"fontSizeMaxScale": "1.3"表示应用字体大小随系统变化的最大缩放比例为1.3倍。

        ```cangjie
        {
            "configuration": {
                "fontSizeScale": "followSystem",
                "fontSizeMaxScale": "1.3"
            }
        }
        ```

    - 若应用需适应系统字体大小的变化，最大应调整至1.75倍，但部分组件可调整至2倍。

        首先需要按照上述步骤配置"fontSizeMaxScale"为1.75。

        ```cangjie
        {
            "configuration": {
            "fontSizeScale": "followSystem",
            "fontSizeMaxScale": "1.75"
            }
        }
        ```

        然后，为Text添加maxFontScale属性，传递参数为2，表示该Text组件跟随系统字体大小变化的最大倍数为2倍。

        ```cangjie
        Text("hello world!")
            .fontSize(@r(sys.float.Body_M))
            .maxFontScale(2.0)
            .fontColor(@r(sys.color.font_secondary))
        ```

- 获取字体大小和粗细

    - 生命周期回调方法[onConfigurationUpdate](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#let-onconfigurationupdated)的config参数可接收字体大小（[fontSizeScale](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#var-fontsizescale)）字体粗（[fontWeightScale](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#var-fontweightscale)）。

        注册系统环境变化的监听后，在系统环境变化时可触发回调。

    - 应用冷启动查询系统字体大小档位。context获取方法详见[仓颉示例代码说明](../../API_Reference/source_zh_cn/cj-development-intro.md#仓颉示例代码说明)。

        ```cangjie
        let context = Global.getAbilityContext();
        let fontSizeScale: Float64 = context.config.fontSizeScale;
        ```