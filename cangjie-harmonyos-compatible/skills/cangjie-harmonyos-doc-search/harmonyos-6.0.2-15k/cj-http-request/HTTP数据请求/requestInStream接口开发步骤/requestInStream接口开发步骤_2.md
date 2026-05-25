httpRequest.requestInStream("EXAMPLE_URL", {err, code =>
    if (let Some(e) <- err) {
        AppLog.error("exception: ${e.message}")
    }
    if (let Some(respCode) <- code) {
        AppLog.info("ResponseCode: ${respCode}")
    } else {
        AppLog.error("response is none")
    }
}, options: option)
```