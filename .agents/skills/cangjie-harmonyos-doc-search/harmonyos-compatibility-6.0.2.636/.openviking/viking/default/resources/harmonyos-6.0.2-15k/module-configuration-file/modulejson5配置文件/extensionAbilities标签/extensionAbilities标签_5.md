extensionAbilities示例：

```json
{
  "extensionAbilities": [
    {
      "name": "FormName",
      "srcEntry": "ohos_app_cangjie_entry.MainAbility",
      "icon": "$media:icon",
      "label" : "$string:extension_name",
      "description": "$string:form_description",
      "type": "form",
      "permissions": ["ohos.abilitydemo.permission.PROVIDER"],
      "readPermission": "",
      "writePermission": "",
      "exported": true,
      "uri":"scheme://authority/path/query",
      "skills": [{
        "actions": [],
        "entities": [],
        "uris": [],
        "permissions": []
      }],
      "metadata": [
        {
          "name": "ohos.extension.form",
          "resource": "$profile:form_config",
        }
      ],
      "extensionProcessMode": "instance",
      "dataGroupIds": [
        "testGroupId1"
      ]
    }
  ]
}
```