# 管理应用账号

应用开发者可以使用[应用账号SDK](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md)管理本应用的账号数据。

能力限制：应用卸载场景下，被卸载应用的账号数据会被删除；本地账号删除场景下，被删除本地账号下的所有应用的账号数据会被删除。

## 开发准备

1. 导入应用账号模块。

   ```cangjie
   import kit.BasicServicesKit.*
   ```

2. 获取应用账号的实例对象。

   ```cangjie
   let appAccountManager = createAppAccountManager()
   ```

## 创建应用账号

用户在应用中登录后，开发者可以在系统中创建一个关联的应用账号，后续可以基于此账号进行数据管理。

具体开发实例如下：

1. 参数准备，指定账号名和可选配置。

   ```cangjie
   let data = HashMap<String, String>([("age", "12")])
   let options = CreateAccountOptions(customData: data)
   ```

2. 调用[createAccount](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#createaccountimplicitlyoptionsarraystring-string-hashmapstringappaccountvaluetype)接口，根据名称和选项创建应用账号。

   ```cangjie
   try {
      appAccountManager.createAccount("createAccount_name_second", options: options)
   } catch (e: BusinessException) {
      AppLog.error("${e.message.toString()}")
   }
   ```

## 查询应用账号列表

具体开发实例如下：
调用[getAllAccounts](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-getallaccounts)接口查询账号列表。

```cangjie
let data = appAccountManager.getAllAccounts()
```

## 存取账号的凭据

具体开发实例如下：

1. 准备参数，指定账号名、凭据类型和凭据。

   ```cangjie
   let name: String = 'ZhangSan'
   let credentialType: String = 'PIN_SIX'
   let credential: String = 'xxxxxx'
   ```

2. 调用[getCredential](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-getcredentialstring-string)接口，获取账号的凭据。

   ```cangjie
   appAccountManager.getCredential(name, credentialType)
   ```

3. 调用[setCredential](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-setcredentialstring-string-string)接口，设置账号的凭据。

   ```cangjie
   appAccountManager.setCredential(name, credentialType, credential)
   ```

## 存取账号的自定义数据

具体开发实例如下：

1. 准备参数，指定账号名和自定义键值。

   ```cangjie
   let name: String = 'ZhangSan'
   let key: String = 'age'
   let value: String = '12'
   ```

2. 调用[setCustomData](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-setcustomdatastring-string-string)接口，设置账号的自定义数据。

   ```cangjie
   appAccountManager.setCustomData(name, key, value)
   ```

3. 调用[getCustomData](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-account-appAccount.md#func-getcustomdatastring-string)接口，获取账号的自定义数据。

   ```cangjie
   appAccountManager.getCustomData(name, key)
   ```