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
                    <p style="font-size: 25px;">About</p>
                </div>
            </div>
            <br>
            <br>
            <br>
            
            <div class="c-regular" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">Roadlyft is a pioneering carpool service dedicated to delivering the most affordable, secure, fast, and reliable transportation solutions. Our platform stands out with minimal service fees and no hidden charges, ensuring transparent and fair pricing for all our users. Designed with the passenger's needs in mind, RoadLyft offers a seamless and convenient carpooling experience.</p>
                </div>
            </div>
            <br>
            <br>
            <br>
            <div class="c-regular" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">Our commitment to technological excellence drives our platform's superior performance. By integrating the latest advancements in frontend and backend development, security, and data processing, we ensure a smooth and responsive user experience. Our custom algorithms are tailored to minimize waiting times and optimize ride matching, providing users with prompt and efficient service.</p>
                    <!-- <p class="c-light" style="font-size: 15px;">Note: The verificaiton process can take up to 24 hours.</p> -->
                </div>
            </div>
            <br>
            <br>
            <br>
            <div class="c-regular" style="width: 100%; display: flex; justify-content: center; ">
                <div style="width: 80%;">
                    <p style="font-size: 20px;">Roadlyft operates on a robust and scalable infrastructure, leveraging powerful cloud hosting and advanced encryption techniques to protect user data. Our dedication to innovation and continuous improvement ensures that we stay ahead of the curve, delivering exceptional value and reliability to our users every day. Join us at Roadlyft and experience the future of carpooling.</p>
                    <!-- <p class="c-light" style="font-size: 15px;">Note: The verificaiton process can take up to 24 hours.</p> -->
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
                  <div id="cont_1" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; cursor: pointer;" onclick="window.location.href='/'"> 
                      <p class="c-bold" style=" font-size: 20px; margin-top: 15px;">Go <span style="font-size: 15px;">↗</span></p>
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
        window.location.href = "/";
        setTimeout(() => {
            window.location.replace = "/";
        }, 2000);
    });
});

</script>

