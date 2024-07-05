<template>
    <div>
        <div class="c-bold" style="width: 100%; height: 50px; display: flex; align-items: center; position: fixed; background-color: white; margin: -8px;  z-index: 1"></div>
        <div class="c-bold" style="width: 100%; height: 50px; display: flex; align-items: center; position: fixed; background-color: white; margin: -8px; margin-top: 10px; z-index: 1">
            <img src="../components/icons/Roadlyft_LOGO.png" alt="" height="100%" width="auto" style="margin-left: 20px;">
            <p style="font-size: 30px; color: #10517d; margin-left: 10px; padding-top: 5px;">Roadlyft</p>

        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <div id="step_info">
            <div class="c-light" style="width: 100%; display: flex; justify-content: center; ">
                <div class="c-bold" style="width: 80%;">
                    <p style="font-size: 25px;">Driver Verificaiton</p>
                </div>
            </div>
            <br>
            <br>
            <br>
            <div class="c-semibold" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">Steps by step guide to complete your verificaiton:</p>
                </div>
            </div>
            <div class="c-light" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">1] Upload your photo.</p>
                    <p style="font-size: 20px;">2] Upload your government issued driving licence.</p>
                    <p style="font-size: 20px;">3] Upload your government issued commercial car certificate.</p>
                    <p style="font-size: 20px;">4] Make a payment.</p>
                </div>
            </div>
            <br>
            <br>
            <br>
            <div class="c-regular" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">You need to upload the documents on Roadlyft's Whatsapp. Our verified assistant will verify your documents.</p>
                </div>
            </div>
            <br>
            <br>
            <br>
            <div class="c-regular" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">After completing your verificaiton process, Roadlyft will verify your documents and enable you to publish your ride.</p>
                    <p class="c-light" style="font-size: 15px;">Note: The verificaiton process can take up to 24 hours.</p>
                </div>
            </div>
            <br>
            <br>
            <br>
            <div class="c-regular" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <!-- <p style="font-size: 20px;">After completing your verificaiton process, Roadlyft will verify your documents and enable you to publish your ride.</p> -->
                    <!-- <p class="c-light" style="font-size: 15px;">By continuing, you agree the Tearms and Conditions of Roadlyft</p> -->
                </div>
            </div>
            <div style="width: 100%; display: flex; justify-content: center;"> 
                  <div id="cont_1" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; cursor: pointer;"> 
                      <p class="c-bold" style=" font-size: 20px; margin-top: 15px;">Continue <span style="font-size: 15px;">↗</span></p>
                  </div>
            </div>
            <br>
            <br>
            <br>
        </div>
    </div>

</template>
<script>
const auth_toc_usr = getCookie('auth_toc_usr');
console.log("cookie: ", auth_toc_usr);
const loyalty = getCookie("lo_@_ty");
console.log("lo_@_ty:", loyalty);
const usr_verify = localStorage.getItem("dock-cid");
console.log("local_storage: ", usr_verify);
let booking_date_thresh = 0;

function getCookie(name) {
    const cookieString = document.cookie;
    const cookiesArray = cookieString.split('; ');
    for (let cookie of cookiesArray) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return cookieValue;
        }
    }
    return null; 
}

window.addEventListener('load', () => {
    if (usr_verify == null){
        window.location.replace("/login");
    }
    else if (auth_toc_usr == null){
        window.location.replace("/login");
    }
    else if (auth_toc_usr != usr_verify.slice(1, -1)){
        console.log("malacious activity detected");
        window.location.replace("/login");
    }

    document.getElementById("cont_1").addEventListener("click", function(){
        window.location.href = "https://wa.me/918830998140?text=I%20want%20to%20get%20verified%20as%20a%20a%20driver.";
        setTimeout(() => {
            window.location.replace = "/";
        }, 2000);
    });
});

</script>

