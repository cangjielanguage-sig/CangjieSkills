### 在DevEco Studio中配置关联的网址域名

在应用的[module.json5文件](../cj-start/basic-knowledge/module-configuration-file.md)中进行如下配置，以声明应用关联的域名地址，并开启域名校验开关。

* "entities"列表中必须包含"entity.system.browsable"。
* "actions"列表中必须包含"ohos.want.action.viewData"。
* "uris"列表中必须包含"scheme"为"https"且"host"为域名地址的元素，可选属性包含"path"、"pathStartWith"和"pathRegex"，详情请参见“[uris标签说明](./cj-app-uri-config.md#uris标签说明)”。
* "domainVerify"设置为true，表示开启域名校验开关。

> **说明：**
>
> skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。
>
> 如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。

例如，声明应用关联的域名是www.example.com，则需进行如下配置。

```json
{
  "module": {
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "ohos_app_cangjie_entry.MainAbility",
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        // 请将exported配置为true；如果exported为false，仅具有权限的系统应用能够拉起该应用，否则无法拉起应用
        "exported": true,
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background",
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "action.system.home"
            ]
          },
          {
            "entities": [
              // entities必须包含"entity.system.browsable"
              "entity.system.browsable"
            ],
            "actions": [
              // actions必须包含"ohos.want.action.viewData"
              "ohos.want.action.viewData"
            ],
            "uris": [
              {
                // scheme须配置为https
                "scheme": "https",
                // host须配置为关联的域名
                "host": "www.example.com",
                // path可选，表示域名服务器上的目录或文件路径，例如www.example.com/path1/中的path1
                // 如果应用只能处理部分特定的path，则此处应该配置应用所支持的path，避免出现应用不能处理的path链接也被引流到应用中的问题
                "path": "path1"
              }
            ],
            // domainVerify须设置为true
           "domainVerify": true
          }
          // 若有其他跳转能力，如推送消息跳转、NFC跳转，可新增一个skill对象，防止与App Linking业务冲突
        ]
      }
    ]
  }
}
```