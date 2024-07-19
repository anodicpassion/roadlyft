<template>
    <div>
        <div class="c-bold" style="width: 100%; height: 50px; display: flex; align-items: center; position: fixed; background-color: white; margin: -8px;  z-index: 1"></div>
        <div class="c-bold" style="width: 100%; height: 50px; display: flex; align-items: center; position: fixed; background-color: white; margin: -8px; margin-top: 10px; z-index: 1">
            <img src="../components/icons/Roadlyft_LOGO.png" alt="" height="100%" width="auto" style="margin-left: 20px;">
            <p style="font-size: 30px; color: #10517d; margin-left: 10px; padding-top: 5px;">Roadlyft</p>

        </div>
        <div style="width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; ">
            <div style="width: 100%;">
                <div style="width: 100%; display: flex; justify-content: center;">
                    <img src="../components/icons/Roadlyft_LOGO.png" alt="" height=200px width=200px >

                </div>
                <br>
                <br>
                <br>
                <div style="width: 100%; display: flex; justify-content: center;"> 
                    <div id="cont_1" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; cursor: pointer;"> 
                        <p class="c-bold" style=" font-size: 20px; margin-top: 15px;">Go <span style="font-size: 15px;">↗</span></p>
                    </div>
                </div>
            </div>
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

