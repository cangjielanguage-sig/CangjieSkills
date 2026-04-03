```json
{
  "javascriptProxyPermission": {
    "urlPermissionList": [       // Object级权限，如果匹配，所有Method都授权
      {
        "scheme": "resource",    // 精确匹配，不能为空
        "host": "rawfile",       // 精确匹配，不能为空
        "port": "",              // 精确匹配，为空不检查
        "path": ""               // 前缀匹配，为空不检查
      },
      {
        "scheme": "https",       // 精确匹配，不能为空
        "host": "xxx.com",       // 精确匹配，不能为空
        "port": "8080",          // 精确匹配，为空不检查
        "path": "a/b/c"          // 前缀匹配，为空不检查
      }
    ],
    "methodList": [
      {
        "methodName": "test",
        "urlPermissionList": [   // Method级权限
          {
            "scheme": "https",   // 精确匹配，不能为空
            "host": "xxx.com",   // 精确匹配，不能为空
            "port": "",          // 精确匹配，为空不检查
            "path": ""           // 前缀匹配，为空不检查
          },
          {
            "scheme": "resource",// 精确匹配，不能为空
            "host": "rawfile",   // 精确匹配，不能为空
            "port": "",          // 精确匹配，为空不检查
            "path": ""           // 前缀匹配，为空不检查
          }
        ]
      },
      {
        "methodName": "test11",
        "urlPermissionList": [   // Method级权限
          {
            "scheme": "q",       // 精确匹配，不能为空
            "host": "r",         // 精确匹配，不能为空
            "port": "",          // 精确匹配，为空不检查
            "path": "t"          // 前缀匹配，为空不检查
          },
          {
            "scheme": "u",       // 精确匹配，不能为空
            "host": "v",         // 精确匹配，不能为空
            "port": "",          // 精确匹配，为空不检查
            "path": ""           // 前缀匹配，为空不检查
          }
        ]
      }
    ]
  }
}
```