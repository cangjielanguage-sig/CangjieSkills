/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// The Cangjie API is in Beta. For details on its capabilities and limitations, please refer to the README file.

package ohos.application.error_observer

import ohos.ffi.Callback1Param

@C
protected struct CErrorObject {
    protected CErrorObject(
        let name: CString,
        let message: CString,
        let stack: CString
    ) {}

    protected func free() {
        unsafe {
            LibC.free(this.name)
            LibC.free(this.message)
            LibC.free(this.stack)
        }
    }
}

@C
protected struct CErrorObserver {
    var onUnhandledException: Int64
    var onException: Int64

    protected init(obsever: ErrorObserver) {
        let wrapper1 = {
            errMsg: CString =>
                let cjErrMsg = errMsg.toString()
                unsafe { LibC.free(errMsg) }
                obsever.onUnhandledException(cjErrMsg)
        }
        let lambdaData1 = Callback1Param<CString, Unit>(wrapper1)
        this.onUnhandledException = lambdaData1.getID()

        if (let Some(v) <- obsever.onException) {
            let wrapper2 = {
                errObject: CErrorObject =>
                    let cjErrObject = ErrorObject(errObject)
                    unsafe { errObject.free() }
                    v(cjErrObject)
            }
            let lambdaData2 = Callback1Param<CErrorObject, Unit>(wrapper2)
            this.onException = lambdaData2.getID()
        } else {
            this.onException = 0
        }
    }
}

@C
protected struct RetDataI32 {
    private RetDataI32(
        protected let code: Int32,
        protected let data: Int32
    ) {}
}
