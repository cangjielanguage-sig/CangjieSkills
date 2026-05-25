### JSON配置文件示例

预置应用级证书的配置示例如下：

```json
{
  "network-security-config": {
    "base-config": {
      "trust-anchors": [
        {
          "certificates": "/etc/security/certificates"
        }
      ]
    },
    "domain-config": [
      {
        "domains": [
          {
            "include-subdomains": true,
            "name": "example.com"
          }
        ],
        "trust-anchors": [
          {
            "certificates": "/data/storage/el1/bundle/entry/resources/resfile"
          }
        ]
      }
    ]
  }
}
```

预置证书公钥哈希值的配置示例如下：

```json
{
  "network-security-config": {
    "domain-config": [
      {
        "domains": [
          {
            "include-subdomains": true,
            "name": "server.com"
          }
        ],
        "pin-set": {
          "expiration": "2024-11-08",
          "pin": [
            {
              "digest-algorithm": "sha256",
              "digest": "FEDCBA987654321"
            }
          ]
        }
      }
    ]
  }
}
```

**各个字段含义:**

| 字段                    | 类型    | 说明                                                                                                                         |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| network-security-config | object  | 网络安全配置。可包含0或者1个base-config，必须包含1个domain-config。                                                          |
| base-config             | object  | 指示应用程序范围的安全配置。必须包含1个trust-anchors。                                                                       |
| domain-config           | array   | 指示每个域的安全配置。可以包含任意个item。item必须包含1个domains，可以包含0或者1个trust-anchors，可以包含0个或者1个pin-set。 |
| trust-anchors           | array   | 受信任的CA。可以包含任意个item。item必须包含1个certificates。                                                                |
| certificates            | string  | CA证书路径。                                                                                                                 |
| domains                 | array   | 域。可以包含任意个item。item必须包含1个name(string:指示域名)，可以包含0或者1个include-subdomains。                           |
| include-subdomains      | boolean | 指示规则是否适用于子域。                                                                                                     |
| pin-set                 | object  | 证书公钥哈希设置。必须包含1个pin，可以包含0或者1个expiration。                                                               |
| expiration              | string  | 指示证书公钥哈希的过期时间。                                                                                                 |
| pin                     | array   | 证书公钥哈希。可以包含任意个item。item必须包含1个digest-algorithm，item必须包含1个digest。                                   |
| digest-algorithm        | string  | 指示用于生成哈希的摘要算法。目前只支持`sha256`。                                                                             |
| digest                  | string  | 指示公钥哈希。                                                                                                               |