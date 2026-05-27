func requestPermissons(): Unit {
                var resultCallback = {
                    errorCode: Option<AsyncError>, data: Option<AccessCtrlPermissionRequestResult> => match (errorCode) {
                        case Some(e) => AppLog.info("permissionResultCallBack request error: errcode: ${e.code}")
                        case _ => match (data) {
                            case Some(value) => for (i in (0..value.permissions.size)) {
                                if (value.authResults[i] == 0) {
                                    // 用户已授权
                                    AppLog.info("permission: ${value.permissions[i]} is granted.")
                                } else {
                                    // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
                                    AppLog.info("permission: ${value.permissions[i]} is denied by user.")
                                }
                            }
                            case _ => AppLog.info("permissionResultCallBack request error: data is null")
                        }
                    }
                }
                let stageContext = getStageContext(globalAbilityContext.getOrThrow())
                // 申请相机和麦克风权限
                let permissionList = ["ohos.permission.CAMERA", "ohos.permission.MICROPHONE"]
                let atManager = AbilityAccessCtrl.createAtManager()
                atManager.requestPermissionsFromUser(stageContext, permissionList, resultCallback)
            }

            func build() {
                Column {
                    Web(src: @rawfile("index.html"), controller: this.webController).onPermissionRequest {
                        event => AlertDialog.show(
                            AlertDialogParamWithButtons(
                                "text",
                                title: 'title',
                                primaryButton: AlertDialogButtonOptions(
                                    value: 'deny',
                                    action: {
                                        => event.request.deny();
                                    }
                                ),
                                secondaryButton: AlertDialogButtonOptions(
                                    value: 'onConfirm',
                                    action: {
                                        => event.request.grant(event.request.getAccessibleResource());
                                    }
                                ),
                                autoCancel: false,
                                cancel: {
                                    => event.request.deny();
                                }
                            )
                        )
                    }
                }
            }
        }
        ```

- 前端页面index.html代码：

    ```html
    <!-- resources/rawfile/index.html -->
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
    </head>
    <body>
    <video id="video" width="500px" height="500px" autoplay="autoplay"></video>
    <canvas id="canvas" width="500px" height="500px"></canvas>
    <br>
    <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()"/>
    <script>
      function getMedia()
      {
        let constraints = {
          video: {width: 500, height: 500},
          audio: true
        };
        // 获取video摄像头区域
        let video = document.getElementById("video");
        // 返回的Promise对象
        let promise = navigator.mediaDevices.getUserMedia(constraints);
        // then()异步，调用MediaStream对象作为参数
        promise.then(function (MediaStream) {
          video.srcObject = MediaStream;
          video.play();
        });
      }
    </script>
    </body>
    </html>
    ```