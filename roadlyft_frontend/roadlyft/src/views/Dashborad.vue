<template>
    <div>
        <div id="home-content" style="display: none;">
            <div id="dashb-content" style="display: block;">
                <div style="position: fixed; right: 0; z-index: -2;">
                    <button id="prev-route-btn" style="background-color: transparent; border: 1px solid rgba(0, 0, 0, 0.1); width: 50px; height: 50px; border-radius: 10px; margin-right: 10px;">
                    <img src="../components/icons/more.png" width="30" height="30">
                    </button>
                </div>
                <div id="prev-route" class="c-light" style="display: none; width: 300px; height: 70vh; position:fixed; z-index:-1; background-color: white; top: 0; right: 0px; border-radius: 0px 0px 0px 20px; border: 0px solid rgba(0, 0, 0, 0.4); box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22); text-align: center; overflow: scroll; ">
                    <br>
                    <p>Your previous routes</p>
                    <br>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                    <div class="round-edge" style="width: 90%; margin-left: 5%; margin-bottom: 20px;"></div>
                </div>
                <div style="width: 100%; z-index: -3;  margin: -8px; margin-top: -10px;  height: 400px; position: fixed; background-image: linear-gradient(225deg, #00c6fb 0%, #005bea 100%);">
                    <br>
                    <p class="c-semibold" style=" font-size: 30px; margin-left: 30px;  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color: white;">Hey,</p>
                    <p id="usr-name" class="c-bold" style=" font-size: 50px; margin-left: 30px; margin-top: -10px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color: white;">User</p>
                    <br>
                    <br>
                    <div class="outer-container" style="width: 100%; height: 100px; background-color: rgba(0, 0, 0, 0.0); margin-top: -20px;  align-items: center; padding-left: 20px; overflow-x: auto; white-space: nowrap; -ms-overflow-style: none;">
                    <div id="date_highlt_0" style="width: 80px; height: 80px; background-color: rgba(255, 255, 255, 0.01); border: 1px solid rgba(225, 225, 225, 0.6); border-radius: 20px; display: inline-block; margin-right: 10px; box-shadow: 0 3px 7px 0 rgba(0, 0, 0, .13), 0 1px 2px 0 rgba(0, 0, 0, .11); justify-content: center; overflow: hidden; text-align: center;" >
                        <p class="c-bold" id="today_date" style="position: relative; color: white; font-size: 20px; ">-</p>
                        <p class="c-light" style="position: relative; color: white; margin-top: -10px;">Today</p>
                    </div>
                    <div id="date_highlt_1" style="width: 80px; height: 80px; background-color: rgba(255, 255, 255, 0.01); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: 20px; display: inline-block; margin-right: 10px; box-shadow: 0 3px 7px 0 rgba(0, 0, 0, .13), 0 1px 2px 0 rgba(0, 0, 0, .11); justify-content: center; overflow: hidden; text-align: center;" >
                        <p class="c-bold" id="tomorrow_date" style="position: relative; color: white; font-size: 20px; ">-</p>
                        <p class="c-light" style="position: relative; color: white; margin-top: -10px;">Tommo</p>
                    </div>
                    
                    <div id="date_highlt_2" style="width: 80px; height: 80px; background-color: rgba(0, 0, 0, 0.1); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: 20px; display: inline-block; margin-right: 10px; overflow: hidden; text-align: center;">
                        <p class="c-bold" id="day_after_tomorrow_date" style="position: relative; color: white; font-size: 20px; ">-</p>
                        <p class="c-light" id="day_after_tomorrow_day" style="position: relative; color: white; margin-top: -10px;">day</p>
                    </div>
                    <div id="date_highlt_3" style="width: 80px; height: 80px; background-color: rgba(0, 0, 0, 0.1); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: 20px; display: inline-block; margin-right: 10px; overflow: hidden; text-align: center;">
                        <p class="c-bold" id="thrid_date" style="position: relative; color: white; font-size: 20px; ">-</p>
                        <p class="c-light" id="thrid_day" style="position: relative; color: white; margin-top: -10px;">day</p>
                    </div>
                    <div id="date_highlt_4" style="width: 80px; height: 80px; background-color: rgba(0, 0, 0, 0.1); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: 20px; display: inline-block; margin-right: 30px; overflow: hidden; text-align: center;">
                        <p class="c-bold" id="forth_date" style="position: relative; color: white; font-size: 20px; ">-</p>
                        <p class="c-light" id="forth_day" style="position: relative; color: white; margin-top: -10px;">day</p>
                    </div>
                    <!-- <div style="width: 80px; height: 80px; background-color: rgba(0, 0, 0, 0.1); border-radius: 20px; display: inline-block; margin-right: 30px; overflow: hidden; text-align: center;">
                        <input type="date" class="c-bold" style="position: relative; color: white; font-size: 20px; ">
                        <p class="c-bold" style="position: relative; color: white; font-size: 20px; ">_</p>
                        <p class="c-light" style="position: relative; color: white; margin-top: -10px;">___</p>
                    </div> -->
                    <!-- <div style="width: 10px; height: 80px; background-color: transparent; border-radius: 20px; display: inline-block; margin-right: 20px;"></div> -->
                    
                    </div>
                </div>
                
                <div id="div2" class="titlebar" style=" overflow: scroll; ">
                    <br>
                    <div style="width: 100%; display: flex; justify-content: center;">
                        <div style="width: 15px; height: 15px; border-right: 2px solid rgba(0, 0, 0, 0.2); border-top: 2px solid rgba(0, 0, 0, 0.2); rotate: -45deg;"></div>
                    </div>
                    <div style="overflow-x: scroll; position: relative;">
                
                        <br>
                        <div style="display: flex; justify-content: center; width: 100%;">
                        <div class="round-edge">
                            <p class="c-light" style=" font-size: 15px; margin-left: 20px; ">where would you like to go...</p>
                        </div>
                        </div>
                
                        <br>
                        <br>
                        <div style="width: 100%; display: flex; justify-content: center;">
                
                        <div class="round-edge" style="background-color: transparent; height: 300px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);">
                            <br>
                            <div style="position: absolute; z-index:  -1; margin-left: 50px;">
                            <div style="height: 10px; width: 10px; border: 2px solid black; border-radius: 50px 50px 50px 50px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 7px; width: 7px; border: 2px solid black; margin-left: 2px;"></div>
                            </div>
                            <br>
                            <p class="c-regular" style="position: absolute; margin-left: 80px; margin-top: 8px;">From</p>
                            <br>
                            <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                            <div class="search pickup_dropdown_p" >
                                <svg width="25" height="25" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg" style=" margin-top: 14px; margin-left: 11px; margin-right: 8px;">
                                <circle cx="200" cy="200" r="140" stroke="rgba(19, 19, 19, 0.423)" stroke-width="40"/>
                                <rect x="383.057" y="397.199" width="117.085" height="20" transform="rotate(-135 383.057 397.199)" fill="rgba(19, 19, 19, 0.423)" stroke="rgba(19, 19, 19, 0.423)" stroke-width="20" stroke-linejoin="round"/>
                                </svg>
                                <input id="pickup_locationInput_p" class="search-inp c-regular" type="text" placeholder="Pickup point">
                                <div id="pickup_dropdownContent_p" class="pickup_dropdown-content_p c-light">
                                    <!-- <div>hello</div> -->
                                </div>
                            </div>
                            </div>
                            <br>
                            <br>
                            <p class="c-regular" style="position: absolute; margin-left: 80px; margin-top: 8px;">To</p>
                            <br>
                            <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                            <div class="search dropoff_dropdown_p">
                                <svg width="25" height="25" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg" style=" margin-top: 14px; margin-left: 11px; margin-right: 8px;">
                                <circle cx="200" cy="200" r="140" stroke="rgba(19, 19, 19, 0.423)" stroke-width="40"/>
                                <rect x="383.057" y="397.199" width="117.085" height="20" transform="rotate(-135 383.057 397.199)" fill="rgba(19, 19, 19, 0.423)" stroke="rgba(19, 19, 19, 0.423)" stroke-width="20" stroke-linejoin="round"/>
                                </svg>
                                <input id="dropoff_locationInput_p" class="search-inp c-regular" type="text" placeholder="Dropoff point">
                                <div id="dropoff_dropdownContent_p" class="dropoff_dropdown-content_p c-light">
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                        <br>
                        <br>
                        <div style="width: 100%; display: flex; justify-content: center;"> 
                        <div class="round-edge" style="background-color: transparent; height: 130px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);">
                            <br>
                            <p class="c-regular" style="position: absolute; margin-left: 20px; margin-top: 8px;">Seats</p>
                            <br>
                            <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                            <div class="search">
                                
                                <input id="n_seats" class="search-inp c-regular" type="number" value="1" min="1" max="4" style="text-align: center; width: 100%;">
                            </div>
                            </div>
                        </div>
                        </div>
                        <br>
                        <br>
                        <div style="width: 100%; display: flex; justify-content: center;"> 
                            <div id="p_go" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb;"> 
                                <p id="para_go_p" class="c-bold" style=" font-size: 20px; margin-top: 15px;">Go..!</p>
                            </div>
                        </div>
                        
                    </div>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                </div>
            </div>
            <div id="map-content" style="display: none;">
                <div style="position: fixed; top: 0; left: 0; margin-top: 10px; margin-left: 10px; width: 50px; height: 50px; background-color: white; border-radius: 10px; display: flex; justify-content: center; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); z-index: 5;"
                onclick="document.getElementById('map-content').style.display = 'none'; document.getElementById('dashb-content').style.display = 'block';">
                    <div class="c-bold" style="width: 20px; height: 20px; margin-left: -8px; margin-top: -22px; font-size: 40px; opacity: 0.5 ;" ><</div>
                </div>
                <div id="map_p"></div>
                <div style="width: 100%; display: flex; justify-content: center; bottom: 0; z-index: 10; position: fixed; margin-bottom: 100px;"> 
                    <div style="width: 100%; margin-left: -15px">
                        <div id="p_search_cabs" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; margin-left: 10%;"> 
                            <p id="p_search_cabs_p" class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Confirm</p>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
            <div id="cablist-content" style="display: none;">
                <div style="position: fixed; top: 0; left: 0; margin-top: 10px; margin-left: 10px; width: 50px; height: 50px; background-color: white; border-radius: 10px; display: flex; justify-content: center; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); z-index: 5;"
                onclick="document.getElementById('cablist-content').style.display = 'none'; document.getElementById('dashb-content').style.display = 'block';">
                    <div class="c-bold" style="width: 20px; height: 20px; margin-left: -8px; margin-top: -22px; font-size: 40px; opacity: 0.5 ;" ><</div>
                </div>
            
                <div style="display: flex; justify-content: center; width: 100%; margin-top: 10px;">
                    <div class="round-edge" style=" border-top-left-radius: 0px; border-bottom-left-radius: 0px;">
                        <p id="cab_search_status" class="c-light" style=" font-size: 15px; margin-left: 30px;"></p>
                    </div>
                </div>
                <div id="cab-search-result">

                </div>
                <!-- <div class="round-edge" style="margin-left: 10%; background-color: transparent; height: 250px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);">
                    <p class="c-bold" style=" margin-right: 20px; padding-top: 10px; text-align: right;">₹500/-</p>

                    <p class="c-regular" style="position: absolute; margin-left: 20px; margin-top: -25px;">Time</p>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -25px; ">
                        <div class="search c-medium" >
                            <p style="height: 30px; margin-left: 20px; margin-right: 20px; overflow: scroll;">alkdf lakdflk asd alke adfjla aldjflas alkedejl a skla alk d</p>
                        </div>
                    </div>
                    <p class="c-light" style="margin-left: 20px; margin-right: 20px; text-align: right; margin-top: 5px;">20m</p>
                    <br>
                    <br>

                    <p class="c-regular" style="position: absolute; margin-left: 20px; margin-top: -25px;">Time</p>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -25px; ">
                        <div class="search c-medium" >
                            <p style="height: 30px; margin-left: 20px; margin-right: 20px; overflow: scroll;">alkdf lakdflk asd alke adfjla aldjflas alkedejl a skla alk d</p>
                        </div>
                    </div>
                    <p class="c-light" style="margin-left: 20px; margin-right: 20px; text-align: right; margin-top: 5px;">20m</p>
                    
                </div> -->
            </div>
            <div id="cab_info" style="display: none;">
                <div style="position: fixed; top: 0; left: 0; margin-top: 10px; margin-left: 10px; width: 50px; height: 50px; background-color: white; border-radius: 10px; display: flex; justify-content: center; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); z-index: 5;"
                onclick="document.getElementById('cablist-content').style.display = 'block'; document.getElementById('cab_info').style.display = 'none';">
                    <div class="c-bold" style="width: 20px; height: 20px; margin-left: -8px; margin-top: -22px; font-size: 40px; opacity: 0.5 ;" ><</div>
                </div>
                <br>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 90px; padding-top: 10px; overflow: scroll;">
                        <!-- <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Ride details: </p> -->
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Driver: <span id="driver_name"></span></p>
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Mobile number: <span id="driver_mobile"></span></p>
                        <!-- <p class="c-bold" style=" font-size: 15px; margin-left: 40px;"><span id="r_toll"></span></p> -->
                    </div>
                </div>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 50px; padding-top: 10px; overflow: scroll;">
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Seats available: <span id="seats_in_cab"></span></p>
                    </div>
                </div>
                <br>
                <br>
                <!-- <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 200px; padding-top: 10px; overflow: scroll;">
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Ride details: </p>
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Origin: <span id="seats_in_cab"></span></p>
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Destination: <span id="seats_in_cab"></span></p>
                    </div>
                </div> -->
                <div style="width: 100%; display: flex; justify-content: center; bottom: 0; z-index: 10; position: fixed; margin-bottom: 100px;"> 
                    <div style="width: 100%; margin-left: -15px">
                        <div id="p_cab_request" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; margin-left: 10%;"> 
                            <p id="p_cab_request_p" class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Request</p>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
            <div id="in_booking" style="display: none; color: #10517d">
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 180px; padding-top: 10px; overflow: scroll;">
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Route details: </p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">From: <span id="p_from_inbooking"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">To: <span id="p_to_inbooking"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">Seats: <span id="p_seats_inbooking"></span></p>
                    </div>
                </div>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 180px; padding-top: 10px; overflow: scroll;">
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Driver details: </p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">Name: <span id="p_D_Name"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">Mobile: <span id="p_D_Mbl"></span></p>
                    </div>
                </div>
                <br>
                <div id="approved_ride" style="width: 100%; display: none; justify-content: center; bottom: 0; z-index: 10; position: fixed; margin-bottom: 100px;"> 
                    <div style="width: 100%; margin-left: -15px">
                        <div  class="round-edge" style="display: flex; justify-content: center; background-color: #FFFFFF; border: 1px solid #10517d; margin-left: 10%;"> 
                            <p  class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Ride Approved</p>
                        </div>
                        
                    </div>
                    
                </div>
                <div style="width: 100%; display: flex; justify-content: center; bottom: 0; z-index: 10; position: fixed; margin-bottom: 100px;"> 
                    <div style="width: 100%; margin-left: -15px">
                        <div id="p_cancel_booking" class="round-edge" style="display: none; justify-content: center; background-color: #00c6fb; margin-left: 10%;"> 
                            <p id="p_cancel_booking_p" class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Cancel booking</p>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>
        <div id="publish-content" style="display: none; color: #10517d">
            <div id="publish-dash" style="display: block;">
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" >
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Publish your ride...</p>
                    </div>
                </div>
                <br>
                <br>
                <div style="width: 100%; display: flex; justify-content: center;">
                    <div class="round-edge" style="background-color: transparent; height: 300px; ">
                        <br>
                        <div style="position: absolute; z-index:  -1; margin-left: 50px;">
                            <div style="height: 10px; width: 10px; border: 2px solid black; border-radius: 50px 50px 50px 50px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid transparent; margin-left: 6px;"></div>
                            <div style="height: 5px; width: 0px; border-left: 2px solid black; margin-left: 6px;"></div>
                            <div style="height: 7px; width: 7px; border: 2px solid black; margin-left: 2px;"></div>
                        </div>
                        <br>
                        <p class="c-regular" style="position: absolute; margin-left: 80px; margin-top: 8px;">From</p>
                        <br>
                        <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                            <div class="search pickup_dropdown_d" >
                                <svg width="25" height="25" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg" style=" margin-top: 14px; margin-left: 11px; margin-right: 8px;">
                                <circle cx="200" cy="200" r="140" stroke="rgba(19, 19, 19, 0.423)" stroke-width="40"/>
                                <rect x="383.057" y="397.199" width="117.085" height="20" transform="rotate(-135 383.057 397.199)" fill="rgba(19, 19, 19, 0.423)" stroke="rgba(19, 19, 19, 0.423)" stroke-width="20" stroke-linejoin="round"/>
                                </svg>
                                <input id="pickup_locationInput_d" class="search-inp c-regular" type="text" placeholder="Pickup point">
                                <div id="pickup_dropdownContent_d" class="pickup_dropdown-content_d c-light"></div>
                            </div>
                        </div>
                        <br>
                        <br>
                        <p class="c-regular" style="position: absolute; margin-left: 80px; margin-top: 8px;">To</p>
                        <br>
                        <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                            <div class="search dropoff_dropdown_d">
                                <svg width="25" height="25" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg" style=" margin-top: 14px; margin-left: 11px; margin-right: 8px;">
                                <circle cx="200" cy="200" r="140" stroke="rgba(19, 19, 19, 0.423)" stroke-width="40"/>
                                <rect x="383.057" y="397.199" width="117.085" height="20" transform="rotate(-135 383.057 397.199)" fill="rgba(19, 19, 19, 0.423)" stroke="rgba(19, 19, 19, 0.423)" stroke-width="20" stroke-linejoin="round"/>
                                </svg>
                                <input id="dropoff_locationInput_d" class="search-inp c-regular" type="text" placeholder="Pickup point">
                                <div id="dropoff_dropdownContent_d" class="dropoff_dropdown-content_d c-light"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="background-color: transparent; height: 130px; justify-content: center; align-items: center;">
                    <br>
                    <p class="c-regular" style="position: absolute; margin-left: 10%; margin-top: 8px;">Seats</p>
                    <br>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                    <div class="search" style="width: 80%;">
                        <input id="d_seats" class="search-inp c-regular" type="number" value="1" min="1" max="30" style="text-align: center; width: 100%;">
                    </div>
                    </div>
                </div>
                <div style="background-color: transparent; height: 130px; justify-content: center; align-items: center;">
                    <br>
                    <p class="c-regular" style="position: absolute; margin-left: 10%; margin-top: 8px;">Date</p>
                    <br>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                    <div class="search" style="width: 80%; ">
                        <input id="d_date" class="search-inp c-regular" type="date" style="text-align: center; width: 85%; margin-left: 10%;">
                    </div>
                    </div>
                </div>
                <div style="background-color: transparent; height: 130px; justify-content: center; align-items: center;">
                    <br>
                    <p class="c-regular" style="position: absolute; margin-left: 10%; margin-top: 8px;">Time</p>
                    <br>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                    <div class="search" style="width: 80%; ">
                        <input id="d_time" class="search-inp c-regular" type="time" style="text-align: center; width: 85%; margin-left: 10%;">
                    </div>
                    </div>
                </div>
                <br>
                <div id="DRIVER_F_0" style="display: none; justify-content: center; width: 100%;">
                    <div class="round-edge" style="width: 80%; height: 150px; display: flex; justify-content: center; align-items: center; background-color: rgb(255, 232, 232);" >
                        <div style="width: 100%;">
                            <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Please complete verification before you can publish your rides.</p>
                            <p class="c-light" style=" font-size: 15px; margin-left: 20px; color: #00c6fb;" onclick="window.location.href = '/driver-verification'">Verify ↗︎</p>
                        </div>
                    </div>
                </div>
                <div id="DRIVER_F_1" style="display: none; justify-content: center; width: 100%;">
                    <div class="round-edge" style="width: 80%; height: 120px; display: flex; justify-content: center; align-items: center; background-color: rgb(255, 232, 232);" >
                        <div style="width: 100%;">
                            <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Your subscription is expired. Please renew it.</p>
                            <p class="c-light" style=" font-size: 15px; margin-left: 20px; color: #00c6fb;" onclick="window.location.href = '/driver-renew'">Renew ↗︎</p>
                        </div>
                    </div>
                </div>
                <div id="DRIVER_F_2" style="width: 100%; display: none; justify-content: center; color: #10517d;"> 
                    <div id="d_publish" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb;"> 
                        <p id="para_proceed_d" class="c-bold" style=" font-size: 20px; margin-top: 15px;">Proceed</p>
                    </div>
                    <br>
                    <br>
                    <br>
                    <br>
                </div>
                <br>
                <br>
                <br>
                <br>
                <br>
            </div>

            <div id="map-content-publish" style="display: none;">
                <div style="position: fixed; top: 0; left: 0; margin-top: 10px; margin-left: 10px; width: 50px; height: 50px; background-color: white; border-radius: 10px; display: flex; justify-content: center; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); z-index: 5;"
                onclick="document.getElementById('map-content-publish').style.display = 'none'; document.getElementById('publish-dash').style.display = 'block';">
                    <div class="c-bold" style="width: 20px; height: 20px; margin-left: -8px; margin-top: -22px; font-size: 40px; opacity: 0.5 ;" ><</div>
                </div>
                <div id="map_d"></div>
                <div style="width: 100%; display: flex; justify-content: center; bottom: 0; z-index: 10; position: fixed; margin-bottom: 100px;"> 
                    <div style="width: 100%; margin-left: -15px">
                        
                        <div class="round-edge" style="background-color: rgba(255, 255, 255, .9); height: 160px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); border-bottom-left-radius: 0; border-bottom-right-radius: 0; margin-left: 10%; margin-bottom: -25px;">
                            <div style="position:absolute; width: 70%; height: 30px; margin-top: 15px; margin-left: 20px; overflow: scroll; align-items: center;">
                                <p id="route_summary" class="c-regular" style="margin: 0px; padding-top: 1px;">Route</p>
                            </div>
                            <br>
                            <div id="route_info" style="width: 100%; display: flex; margin-top: 20px; ">
                                <div style="width: 50%; align-items: center; text-align: center; justify-content: center;">
                                    <p id="route_len" class="c-bold" style="margin-top: 15px;">Select route:</p>
                                </div>
                                <div style="width: 50%; align-items: center; text-align: center;">
                                    <p id="route_toll" class="c-bold" style="margin-top: 15px;"></p>

                                </div>
                            </div>

                            <div style="width: 100%; display: flex; justify-content: center; margin-top: -28px; ">
                                <div class="search" style="display: flex; justify-content: center; align-items: center;">  
                                    <form class="c-light" style="display: flex;">
                                        <label id="lbl_1" style="display: none;">
                                            <input type="radio" name="color" value="Blue">
                                            Blue
                                        </label>
                                        <label id="lbl_2" style="display: none;">
                                            <input type="radio" name="color" value="Green" style="margin-left: 20px;">
                                            Green
                                        </label>
                                        <label id="lbl_3" style="display: none;">
                                            <input type="radio" name="color" value="Red" style="margin-left: 20px;">
                                            Red
                                        </label>
                                    </form>
                                </div>
                            </div>
                        </div>
                        <div id="d_route_confirm" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; margin-left: 10%;"> 
                            <p class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Confirm</p>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
            <div id="cost-confirm-publish" style="display: none;">
                <div style="position: fixed; top: 0; left: 0; margin-top: 10px; margin-left: 10px; width: 50px; height: 50px; background-color: white; border-radius: 10px; display: flex; justify-content: center; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); z-index: 5;"
                onclick="document.getElementById('cost-confirm-publish').style.display = 'none'; document.getElementById('map-content-publish').style.display = 'block';">
                    <div class="c-bold" style="width: 20px; height: 20px; margin-left: -8px; margin-top: -22px; font-size: 40px; opacity: 0.5 ;" ><</div>
                </div>
                <br>
                <br>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 180px; padding-top: 10px; overflow: scroll;">
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Route details: </p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px;">Summary: <span id="r_summary"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px;">Distance: <span id="r_distance"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px;">Time: <span id="r_time"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px;">Toll: <span id="r_toll"></span></p>
                    </div>
                </div>
                <br>
                <br>
                <div class="round-edge" style="margin-left: 10%; background-color: transparent; height: 150px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);">
                    <br>
                    <p class="c-regular" style="position: absolute; margin-left: 20px; margin-top: 8px;">Fare (<span class="c-bold"> &#8377 </span>)</p>
                    <br>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                        <div class="search">
                            <input id="d_cost" class="search-inp c-regular" type="number" style="text-align: center; width: 100%;" value="0">
                        </div>
                    </div>
                    <div style="width: 100%; display: flex; justify-content: center; margin-top: -5px; ">
                        <p id="recommended_fare" class="c-light" style="position: absolute; color: black; font-size: 15px;"></p>
                    </div>

                </div>
                <br>
                <br>
                <br>
                <div id="d_price_confirm" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; margin-left: 10%;"> 
                    <p id="d_price_confirm_p" class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Publish</p>
                </div>

            </div>
            <div id="in_ride" style="display: none;">
                
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 180px; padding-top: 10px; overflow: scroll;">
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Route details: </p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">From: <span id="i_from"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">To: <span id="i_to"></span></p>
                        <p class="c-bold" style=" font-size: 15px; margin-left: 40px; margin-right: 20px">Scheduled on: <span id="i_scheduled"></span></p>
                        <!-- <p class="c-bold" style=" font-size: 15px; margin-left: 40px;"><span id="r_toll"></span></p> -->
                    </div>
                </div>
                <br>
                <br>
                <p class="c-regular" style=" margin-left: 20px; margin-top: 8px;">Requests</p>
                <div id="cab_request_toapp" class="round-edge" style="margin-left: 10%; background-color: transparent; height: 350px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); overflow: scroll;">
                    <!-- <br>
                    <div style="display: flex; justify-content: center; width: 100%;">
                        <div class="round-edge" style="height: 130px; padding-top: 10px; overflow: scroll;">
                            <p class="c-bold" style=" font-size: 15px; margin-left: 20px; margin-right: 20px">From: <span class="c-light">a</span></p>
                            <p class="c-bold" style=" font-size: 15px; margin-left: 20px; margin-right: 20px">To: <span class="c-light">b</span></p>
                            <p class="c-bold" style=" font-size: 15px; margin-left: 20px; margin-right: 20px">Seats: <span class="c-light">c</span></p>
                        </div>
                    </div> -->
                </div>
                <br>
                <br>
                <p class="c-regular" style=" margin-left: 20px; margin-top: 8px;">Approved</p>
                <div id="cab_accept_toapp" class="round-edge" style="margin-left: 10%; background-color: transparent; height: 350px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); overflow: scroll;">
                    
                </div>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
            </div>
            <div id="request_info" style="display: none;">
                <div style="position: fixed; top: 0; left: 0; margin-top: 10px; margin-left: 10px; width: 50px; height: 50px; background-color: white; border-radius: 10px; display: flex; justify-content: center; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); z-index: 5;"
                    onclick="document.getElementById('in_ride').style.display = 'block'; document.getElementById('request_info').style.display = 'none';">
                    <div class="c-bold" style="width: 20px; height: 20px; margin-left: -8px; margin-top: -22px; font-size: 40px; opacity: 0.5 ;" ><</div>
                </div>
                <br>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 90px; padding-top: 10px; overflow: scroll;">
                        <!-- <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Ride details: </p> -->
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Passanger: <span id="passanger_name"></span></p>
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Mobile number: <span id="passanger_mobile"></span></p>
                        <!-- <p class="c-bold" style=" font-size: 15px; margin-left: 40px;"><span id="r_toll"></span></p> -->
                    </div>
                </div>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 50px; padding-top: 10px; overflow: scroll;">
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Seats booking: <span id="seat_request"></span></p>
                    </div>
                </div>
                <br>
                <br>
                <div style="display: flex; justify-content: center; width: 100%;">
                    <div class="round-edge" style="height: 200px; padding-top: 10px; overflow: scroll;">
                        <p class="c-light" style=" font-size: 15px; margin-left: 20px;">Request details: </p>
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Pickup: <span id="pick_p_d"></span></p>
                        <p class="c-regular" style=" font-size: 15px; margin-left: 20px;">Dropoff: <span id="drop_p_d"></span></p>
                    </div>
                </div>
                <div style="width: 100%; display: flex; justify-content: center; bottom: 0; z-index: 10; position: fixed; margin-bottom: 100px;"> 
                    <div style="width: 100%; margin-left: -15px">
                        <div id="d_confirm_passanger" class="round-edge" style="display: flex; justify-content: center; background-color: #00c6fb; margin-left: 10%;"> 
                            <p id="d_confirm_passanger_p" class="c-bold" style=" font-size: 20px; margin-top: 15px; color: #10517d;">Accept</p>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>
        <div id="profile-content" style="display: none;">
            <div>
                <div style="width: 100%; height: 150px; display: flex;">
                    <!-- <div class="round-edge" style="width: 100px; height:100px; margin: 30px; display: flex; justify-content: center; border: 1px solid rgba(0, 0, 0, 0.05);">
                        <div class="round-edge" style="width: 50px; height: 50px; background-color: white; margin-top: 10px;"></div>
                        <div class="round-edge" style="width: 80px; height: 30px; position:absolute; background-color: white;  margin-top: 70px;"></div>
                    </div> -->
                    <div style="margin-top: 20px; margin-left: -20px; font-size: 50px; align-content: center;">
                        <p id="cust_name" class="c-bold" style="margin-left: 40px;"></p>
                    </div>
                </div>
                <br>
                <br>
                <div style="width: 100%; height: 30px; display: flex; border-bottom: 1px solid rgba(0, 0, 0, 0.1); font-size: 20px;">
                <div class="c-bold" id="prof" style="width: 50%; text-align: center; border-bottom: 1px solid black;">Profile</div>
                <div class="c-bold" id="acc" style="width: 50%; text-align: center;">Account</div>
                </div>
                <br>
                <br>
                <br>
                <div id="prof-cont" style="text-align: center;  ">
                    <div class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                        <p>Personal Information</p>
                    </div>
                    <div class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                        <p>Setting</p> 
                    </div>
                    <div class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                        <p>About</p> 
                    </div>
                    <div id="d_renew" class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                        <p>Subscription</p> 
                    </div>
                    <div id="d_verification" class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                        <p>Verification</p> 
                    </div>
                </div>
                <div id="acc-cont" style="display: none; text-align: center;">
                    <div class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                    <p>Account Information</p>
                    </div>
                    <div class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                    <p>Account Setting</p> 
                    </div>
                    <div id="logout_btn" class="round-edge c-regular" style="width: 90%; margin-left: 5%; margin-bottom: 20px; border: 1px solid rgba(0, 0, 0, 0.05);">
                    <p>Logout</p> 
                    </div>

                </div>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
            </div>
        </div>
        
        
        
        <div style="width: 100%; display: flex; justify-content: center; ">
        
            <div class="navbar c-light" style="display: flex; justify-content: center;">
    
                <div class="navbar" style="width: 85%; border: none; box-shadow: none; left: auto; background-color: transparent;">
                    <div style="width: 100%; height: 60px; display: flex; margin-top: 15px;">
                        <div style="width: 33%; height: 30px; display: flex; justify-content: center; ">
                            <div id="home-div" style="text-decoration: none; width: 50px; height: 50px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.1); display: flex; justify-content: center; margin-top: -10px; align-items: center;">
                                <img id="home-ico" src="../components/icons/home_w.png" width="30" height="30" >
                            </div>
                        </div>
                        <div style="width: 33%; height: 30px; display: flex; justify-content: center;">
                            <div id="publish-div" style="text-decoration: none; width: 50px; height: 50px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.1); display: flex; justify-content: center; margin-top: -10px; align-items: center;">
                                <img id="publish-ico" src="../components/icons/progress_w.png" width="30" height="30">
                            </div>
                        </div>
                        <div style="width: 33%; height: 30px; display: flex; justify-content: center;">
                            <div id="profile-div" style="text-decoration: none; width: 50px; height: 50px; border-radius: 50%; background-color: rgba(255, 255, 255, 0.1); display: flex; justify-content: center; margin-top: -10px; align-items: center;">
                                <img id="profile-ico" src="../components/icons/profile_w.png" width="30" height="30">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>








<script>

const auth_toc_usr = getCookie('auth_toc_usr');
const loyalty = getCookie("lo_@_ty");
const usr_verify = localStorage.getItem("dock-cid");
let booking_date_thresh = 0;
const customMapStyles = [
    {
        "featureType": "all",
        "elementType": "labels.text.fill",
        "stylers": [
            { "color": "#000000" }, { "lightness": 40}
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.fill",
        "stylers": [
            { "color": "#000000" }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [
            { "color": "#d0d0d0" },
            { "lightness": 14 },
            { "weight": 1.4 }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "all",
        "stylers": [
            { "color": "#eff3f7" }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
            { "color": "#d9e1ea" },
            { "lightness": 5 }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [
            { "color": "#abbfd3" }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
            { "color": "#abbfd3" },
            { "lightness": 1 }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [
            { "color": "#d9e1ea" }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry.stroke",
        "stylers": [
            { "color": "#e1e8ef" },
            { "lightness": 1 }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry",
        "stylers": [
            { "color": "#FFFFFF" }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "all",
        "stylers": [
            { "color": "#d9e1ea" }
        ]
    },
    {
        "featureType": "water",
        "elementType": "all",
        "stylers": [
            { "color": "#5d6e74" }
        ]
    }
];
let map, geocoder, directionsService, directionsRenderer;
let pickup_latlng_dg, dropoff_latlng_dg, route_indx_dg
let pickup_latlng_pg, dropoff_latlng_pg

function home_btn_disp (){
    document.getElementById("home-content").style.display = "block";
    document.getElementById("publish-content").style.display = "none";
    document.getElementById("profile-content").style.display = "none";
    document.getElementById("home-ico").style.opacity = 1;
    document.getElementById("publish-ico").style.opacity = 0.5;
    document.getElementById("profile-ico").style.opacity = 0.5;
    document.getElementById("home-div").style.backgroundColor = "rgba(255, 255, 255, 0.1)";
    document.getElementById("publish-div").style.backgroundColor = "transparent";
    document.getElementById("profile-div").style.backgroundColor = "transparent";
}
function publish_btn_disp(){
    document.getElementById("home-content").style.display = "none";
    document.getElementById("publish-content").style.display = "block";
    document.getElementById("profile-content").style.display = "none";
    document.getElementById("home-ico").style.opacity = 0.5;
    document.getElementById("publish-ico").style.opacity = 1;
    document.getElementById("profile-ico").style.opacity = 0.5;
    document.getElementById("publish-div").style.backgroundColor = "rgba(255, 255, 255, 0.1)";
    document.getElementById("home-div").style.backgroundColor = "transparent";
    document.getElementById("profile-div").style.backgroundColor = "transparent";
}
function profile_btn_disp(){
    document.getElementById("home-content").style.display = "none";
    document.getElementById("publish-content").style.display = "none";
    document.getElementById("profile-content").style.display = "block";
    document.getElementById("home-ico").style.opacity = 0.5;
    document.getElementById("publish-ico").style.opacity = 0.5;
    document.getElementById("profile-ico").style.opacity = 1;
    document.getElementById("profile-div").style.backgroundColor = "rgba(255, 255, 255, 0.1)";
    document.getElementById("publish-div").style.backgroundColor = "transparent";
    document.getElementById("home-div").style.backgroundColor = "transparent";
}
function day_select_highlt(thresh_day){
    if (thresh_day == 0){
        booking_date_thresh = thresh_day;
        document.getElementById('date_highlt_0').style.border = "1px solid rgba(225, 225, 225, 0.6)";
        document.getElementById('date_highlt_1').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_2').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_3').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_4').style.border = "1px solid rgba(0, 0, 0, 0.05)";
    }
    else if (thresh_day == 1){
        booking_date_thresh = thresh_day;
        document.getElementById('date_highlt_1').style.border = "1px solid rgba(225, 225, 225, 0.6)";
        document.getElementById('date_highlt_0').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_2').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_3').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_4').style.border = "1px solid rgba(0, 0, 0, 0.05)";
    }
    else if (thresh_day == 2){
        booking_date_thresh = thresh_day;
        document.getElementById('date_highlt_2').style.border = "1px solid rgba(225, 225, 225, 0.6)";
        document.getElementById('date_highlt_0').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_1').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_3').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_4').style.border = "1px solid rgba(0, 0, 0, 0.05)";
    }
    else if (thresh_day == 3){
        booking_date_thresh = thresh_day;
        document.getElementById('date_highlt_3').style.border = "1px solid rgba(225, 225, 225, 0.6)";
        document.getElementById('date_highlt_0').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_2').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_1').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_4').style.border = "1px solid rgba(0, 0, 0, 0.05)";
    }
    else if (thresh_day == 4){
        booking_date_thresh = thresh_day;
        document.getElementById('date_highlt_4').style.border = "1px solid rgba(225, 225, 225, 0.6)";
        document.getElementById('date_highlt_0').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_2').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_3').style.border = "1px solid rgba(0, 0, 0, 0.05)";
        document.getElementById('date_highlt_1').style.border = "1px solid rgba(0, 0, 0, 0.05)";
    }
}
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
function logout(){
    console.log("Preparing to logout.");
    localStorage.removeItem("dock-cid");
    document.cookie = 'auth_toc_usr=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
    window.location.reload();
}
function profile_section(){
    document.getElementById("prof").style.borderBottom = "1px solid black";
    document.getElementById("acc").style.borderBottom = "0px solid black";
    document.getElementById("acc-cont").style.display = "none";
    document.getElementById("prof-cont").style.display = "block";
}
function account_section(){
    document.getElementById("acc").style.borderBottom = "1px solid black";
    document.getElementById("prof").style.borderBottom = "0px solid black";
    document.getElementById("prof-cont").style.display = "none";
    document.getElementById("acc-cont").style.display = "block";
}
function clck (event) {
    var myDiv = document.getElementById("prev-route");
    var myDiv_2 = document.getElementById("prev-route-btn");
    var isClickInside = myDiv.contains(event.target);
    var isClickInside_2 = myDiv_2.contains(event.target);

    if (!isClickInside) {
        if (myDiv.style.display == "block"){
        myDiv.style.display = "none";
        }
        // Your code to handle click outside of the div goes here
    }
    if (isClickInside_2){
    document.getElementById("prev-route").style.display = "block";
    }
}
function fetchLocations_1() {
    var input = document.getElementById('pickup_locationInput_p').value;
    const dropdown = document.getElementById('pickup_dropdownContent_p');
    dropdown.style.display = "block";

    const service = new google.maps.places.AutocompleteService();
    // service.getPlacePredictions({ input: input }, function (predictions, status) {
    service.getPlacePredictions({ input: input, componentRestrictions: { country: 'in' } }, function (predictions, status) {

        if (status != google.maps.places.PlacesServiceStatus.OK) {
            console.log(status);
            return;
        }
        dropdown.innerHTML = '';
        predictions.forEach(function (prediction) {
            const option = document.createElement('div');
            option.addEventListener("click", function (){document.getElementById('pickup_locationInput_p').value = prediction.description;document.getElementById("pickup_dropdownContent_p").style.display = "none";document.getElementById('dropoff_locationInput_p').focus();});
            option.innerText = prediction.description;
            dropdown.appendChild(option);
        });
    });
}
function fetchLocations_2() {
    const input = document.getElementById('dropoff_locationInput_p').value;
    const dropdown = document.getElementById('dropoff_dropdownContent_p');
    dropdown.style.display = "block";

    const service = new google.maps.places.AutocompleteService();
    // service.getPlacePredictions({ input: input }, function (predictions, status) {
    service.getPlacePredictions({ input: input, componentRestrictions: { country: 'in' } }, function (predictions, status) {

        if (status != google.maps.places.PlacesServiceStatus.OK) {
            console.log(status);
            return;
        }

        dropdown.innerHTML = '';

        predictions.forEach(function (prediction) {
            const option = document.createElement('div');
            option.addEventListener("click", function (){document.getElementById('dropoff_locationInput_p').value = prediction.description;document.getElementById("dropoff_dropdownContent_p").style.display = "none";});
            option.innerText = prediction.description;
            dropdown.appendChild(option);
        });
    });
}
function fetchLocations_3() {
    var input = document.getElementById('pickup_locationInput_d').value;
    const dropdown = document.getElementById('pickup_dropdownContent_d');
    dropdown.style.display = "block";

    const service = new google.maps.places.AutocompleteService();
    // service.getPlacePredictions({ input: input }, function (predictions, status) {
    service.getPlacePredictions({ input: input, componentRestrictions: { country: 'in' } }, function (predictions, status) {

        if (status != google.maps.places.PlacesServiceStatus.OK) {
            console.log(status);
            return;
        }
        dropdown.innerHTML = '';
        predictions.forEach(function (prediction) {
            const option = document.createElement('div');
            option.addEventListener("click", function (){document.getElementById('pickup_locationInput_d').value = prediction.description;document.getElementById("pickup_dropdownContent_d").style.display = "none";document.getElementById('dropoff_locationInput_p').focus();});
            option.innerText = prediction.description;
            dropdown.appendChild(option);
        });
    });
}
function fetchLocations_4() {
    const input = document.getElementById('dropoff_locationInput_d').value;
    const dropdown = document.getElementById('dropoff_dropdownContent_d');
    dropdown.style.display = "block";

    const service = new google.maps.places.AutocompleteService();
    // service.getPlacePredictions({ input: input }, function (predictions, status) {
    service.getPlacePredictions({ input: input, componentRestrictions: { country: 'in' } }, function (predictions, status) {

        if (status != google.maps.places.PlacesServiceStatus.OK) {
            console.log(status);
            return;
        }

        dropdown.innerHTML = '';

        predictions.forEach(function (prediction) {
            const option = document.createElement('div');
            option.addEventListener("click", function (){document.getElementById('dropoff_locationInput_d').value = prediction.description;document.getElementById("dropoff_dropdownContent_d").style.display = "none";});
            option.innerText = prediction.description;
            dropdown.appendChild(option);
        });
    });
}
function fetch_loc(){
    fetch('https://b48a-103-234-240-164.ngrok-free.app/get_loc_da', {
        method: 'POST',
        credentials: 'include',
        
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials': 'true',
        },
        body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1)})
        
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Response from server:', data);
        if (data['RESP_STAT'] == "SUCCESS") {
            for(var i = 0; i < data["LOC"].length; i++){
                var pickup_div_p = document.createElement("div");
                var dropoff_div_p = document.createElement("div");
                pickup_div_p.innerText = data["LOC"][i];
                dropoff_div_p.innerText = data["LOC"][i];
                document.getElementById("pickup_dropdownContent_p").appendChild(pickup_div_p);
                document.getElementById("dropoff_dropdownContent_p").appendChild(dropoff_div_p);
            }
        }
        else {
            alert("Error with your profile. Please login again.");
            logout();
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert("Something went wrong. Please try again after some time.")
    });
}
function p_go(){
    var pickup_point = document.getElementById("pickup_locationInput_p").value;
    var dropoff_point = document.getElementById("dropoff_locationInput_p").value;
    var number_seats = document.getElementById("n_seats").value;
    if (number_seats < 5 && number_seats > 0){
        
    }
    else{
        alert("We allow maximum 4 seat booking.")
        return;}
    if (pickup_point.length > 2 && dropoff_point.length > 2){
        if (pickup_point != dropoff_point){
            document.getElementById("para_go_p").innerText = "...";
            document.getElementById("p_go").removeEventListener("click", p_go);
            document.getElementById("dashb-content").style.display = "none";
            document.getElementById("map-content").style.display = "block";
            showLocations_p();
            document.getElementById("para_go_p").innerText = "Go..!";
            document.getElementById("p_go").addEventListener("click", p_go);
        }
        else{
            alert("Pickup and Dropoff points cannot be same.");
        }
    }
}
function p_search_cabs(){
    document.getElementById('cablist-content').style.display = 'block';
    document.getElementById('map-content').style.display = 'none';
    document.getElementById('p_search_cabs_p').innerText = "...";
    document.getElementById('p_search_cabs').removeEventListener("click", p_search_cabs);
    document.getElementById('cab_search_status').innerText = "Searching for cabs...";
    var number_seats = document.getElementById("n_seats").value;

    let parentElement = document.getElementById("cab-search-result");
    while (parentElement.firstChild) {
        console.log(parentElement.firstChild);
        parentElement.removeChild(parentElement.firstChild);
    }

    fetch('https://b48a-103-234-240-164.ngrok-free.app/p_search_cabs', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty, "pickup_latlng": pickup_latlng_pg, "dropoff_latlng": dropoff_latlng_pg, "seats":number_seats, "booking_date_thresh": booking_date_thresh})
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                // alert("Success.");
                console.log(data["CAB_LST"]);
                document.getElementById('cab_search_status').innerText = `${data["CAB_LST"].length} cabs found.`;
                
                

                for (var i = 0; i < data["CAB_LST"].length; i ++){
                    console.log(data["CAB_LST"][i][0]);
                    cabs_append(i, data["CAB_LST"][i]);
                }


                
            }

            else if (data['RESP_STAT'] == "NONE") {
                // alert("No cabs found.")
                document.getElementById('cab_search_status').innerText = "No cabs found.";
            }
            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
            document.getElementById('p_search_cabs_p').innerText = "Confirm";
            document.getElementById('p_search_cabs').addEventListener("click", p_search_cabs);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Something went wrong. Please try again after some time.")
            document.getElementById('p_search_cabs_p').innerText = "Confirm";
            document.getElementById('p_search_cabs').addEventListener("click", p_search_cabs);
        }); 

}
function showLocations_p() {
    map = new google.maps.Map(document.getElementById('map_p'), {
        center: { lat: 17.27889429107477, lng: 74.1848932778437 },
        zoom: 15, 
        styles: customMapStyles, 
        disableDefaultUI: true,
        zoomControl: false,
    });
    geocoder = new google.maps.Geocoder();
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({
        suppressMarkers: true 
    });
    directionsRenderer.setMap(map);
    const location1 = document.getElementById('pickup_locationInput_p').value;
    const location2 = document.getElementById('dropoff_locationInput_p').value;

    if (!location1 || !location2) {
        alert("Please enter both locations");
        document.getElementById('map-content').style.display = 'none'; 
        document.getElementById('dashb-content').style.display = 'block';
        return;
    }

    geocodeLocation(location1, (latLng1) => {
        if (!latLng1) {
            alert(`Pickup not found: ${location1}`);
            document.getElementById('map-content').style.display = 'none'; 
            document.getElementById('dashb-content').style.display = 'block';
            return;
        }

        geocodeLocation(location2, (latLng2) => {
            if (!latLng2) {
                alert(`Dropoff not found: ${location2}`);
                document.getElementById('map-content').style.display = 'none'; 
                document.getElementById('dashb-content').style.display = 'block';
                return;
            }

            directionsRenderer.set('directions', null);
            pickup_latlng_pg = latLng1;
            dropoff_latlng_pg = latLng2;
            only_markers(latLng1, latLng2);
        });
    });
}
function showLocations_d() {
    map = new google.maps.Map(document.getElementById('map_d'), {
        center: { lat: 17.27889429107477, lng: 74.1848932778437 },
        zoom: 15, 
        styles: customMapStyles, 
        disableDefaultUI: true,
        zoomControl: false,
    });
    geocoder = new google.maps.Geocoder();
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({
        suppressMarkers: true 
    });
    directionsRenderer.setMap(map);
    const location1 = document.getElementById('pickup_locationInput_d').value;
    const location2 = document.getElementById('dropoff_locationInput_d').value;

    if (!location1 || !location2) {
        alert("Please enter both locations");
        document.getElementById("map-content-publish").style.display = "none";
        document.getElementById("publish-dash").style.display = "block";
        return;
    }

    geocodeLocation(location1, (latLng1) => {
        if (!latLng1) {
            alert(`Pickup not found: ${location1}`);
            document.getElementById("map-content-publish").style.display = "none";
            document.getElementById("publish-dash").style.display = "block";
            return;
        }

        geocodeLocation(location2, (latLng2) => {
            if (!latLng2) {
                alert(`Dropoff not found: ${location2}`);
                document.getElementById("map-content-publish").style.display = "none";
                document.getElementById("publish-dash").style.display = "block";
                return;
            }

            // Clear previous directions
            directionsRenderer.set('directions', null);

            // Place markers and show route
            placeMarkersAndShowRoute(latLng1, latLng2);
            // only_markers(latLng1, latLng2);
        });
    });
}
function geocodeLocation(location, callback) {
    geocoder.geocode({ 'address': location }, function(results, status) {
        if (status === 'OK') {
            // console.log(location, " : ", results[0].geometry.location.lat(), results[0].geometry.location.lng());
            callback(results[0].geometry.location);
        } else {
            callback(null);
        }
    });
}
function get_latlong(location) {
    geocoder.geocode({ 'address': location }, function(results, status) {
        if (status === 'OK') {
            return (results[0].geometry.location.lat(), results[0].geometry.location.lng());
        } else {
            return null;
        }
    });
}
function only_markers(latLng1, latLng2) {
    // Create a custom marker using SVG icon
    const icon1 = {
        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent('<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M249.5 428.996C232 428.996 145 251 145 251L354 251C354 251 267 428.996 249.5 428.996Z" fill="#10517D"/><ellipse cx="249.5" cy="192" rx="119.5" ry="121" fill="#10517D"/><circle cx="250" cy="192" r="50" fill="white"/></svg>'),
        scaledSize: new google.maps.Size(80, 80), // Adjust size if needed
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(40, 68)
    };

    const icon2 = {
        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent('<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M261.925 389.462C259.009 397.051 248.323 397.189 245.21 389.679L130.858 113.765C127.856 106.521 134.907 99.1702 142.269 101.869L246.444 140.052C248.552 140.825 250.872 140.781 252.95 139.931L358.125 96.8919C365.426 93.9042 372.764 101.087 369.934 108.45L261.925 389.462Z" fill="#7ED956"/></svg>'),
        scaledSize: new google.maps.Size(80, 80), // Adjust size if needed
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(41, 63)
    };

    // Place markers
    new google.maps.Marker({
        position: latLng1,
        map: map,
        icon: icon1,
        title: 'Location 1',
    });

    new google.maps.Marker({
        position: latLng2,
        map: map,
        icon: icon2,
        title: 'Location 2',
    });

    // // Show route
    // const request = {
    //     origin: latLng1,
    //     destination: latLng2,
    //     travelMode: 'DRIVING'
    // };

    // directionsService.route(request, function(result, status) {
    //     if (status === 'OK') {
    //         directionsRenderer.setDirections(result);
    //     } else {
    //         alert('Directions request failed due to ' + status);
    //     }
    // });

    // Fit the map to the bounds of the markers
    const bounds = new google.maps.LatLngBounds();
    bounds.extend(latLng1);
    bounds.extend(latLng2);
    map.fitBounds(bounds);
}
function show_route_select_opt(len){
    var lbl_1 = document.getElementById("lbl_1")
    var lbl_2 = document.getElementById("lbl_2")
    var lbl_3 = document.getElementById("lbl_3")
    if (len == 1){
        lbl_1.style.display = "block";
        lbl_2.style.display = "none";
        lbl_3.style.display = "none";
    }
    else if (len == 2){
        lbl_1.style.display = "block";
        lbl_2.style.display = "block";
        lbl_3.style.display = "none";
    }
    else if (len == 3){
        lbl_1.style.display = "block";
        lbl_2.style.display = "block";
        lbl_3.style.display = "block";
    }
    document.querySelector('#lbl_1 input').checked = false;
    document.querySelector('#lbl_2 input').checked = false;
    document.querySelector('#lbl_3 input').checked = false;
    document.getElementById("route_toll").innerText = " "
    document.getElementById("route_toll").style.color = "#10517d"
    document.getElementById("route_len").innerText = `Select route:`
    document.getElementById("route_summary").innerText = "Route";

}
function placeMarkersAndShowRoute(latLng1, latLng2){
    // Define icons
    const icon1 = {
        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent('<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M249.5 428.996C232 428.996 145 251 145 251L354 251C354 251 267 428.996 249.5 428.996Z" fill="#10517D"/><ellipse cx="249.5" cy="192" rx="119.5" ry="121" fill="#10517D"/><circle cx="250" cy="192" r="50" fill="white"/></svg>'),
        scaledSize: new google.maps.Size(80, 80), // Adjust size if needed
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(40, 68)
    };

    const icon2 = {
        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent('<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M261.925 389.462C259.009 397.051 248.323 397.189 245.21 389.679L130.858 113.765C127.856 106.521 134.907 99.1702 142.269 101.869L246.444 140.052C248.552 140.825 250.872 140.781 252.95 139.931L358.125 96.8919C365.426 93.9042 372.764 101.087 369.934 108.45L261.925 389.462Z" fill="#7ED956"/></svg>'),
        scaledSize: new google.maps.Size(80, 80), // Adjust size if needed
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(41, 63)
    };

    // Place markers
    new google.maps.Marker({
        position: latLng1,
        map: map,
        icon: icon1,
        title: 'Location 1',
    });

    new google.maps.Marker({
        position: latLng2,
        map: map,
        icon: icon2,
        title: 'Location 2',
    });

    // Show routes
    const request = {
        origin: latLng1,
        destination: latLng2,
        travelMode: 'DRIVING',
        provideRouteAlternatives: true // Request alternative routes
    };

    directionsService.route(request, function(result, status) {
        if (status === 'OK') {
            const routes = result.routes.slice(0, 3); // Take up to 3 routes
            show_route_select_opt(routes.length);
            routes.forEach((route, index) => {
                new google.maps.DirectionsRenderer({
                    map: map,
                    directions: result,
                    routeIndex: index, // Specify which route to display
                    polylineOptions: {
                        strokeColor: index === 0 ? 'blue' : index === 1 ? 'green' : 'red', // Different colors for each route
                        strokeOpacity: 0.6,
                        strokeWeight: 3
                    },
                    suppressMarkers: true // Suppress default markers
                });
            });
        } else {
            alert('Directions request failed due to ' + status);
        }
    });

    // Fit the map to the bounds of the markers
    const bounds = new google.maps.LatLngBounds();
    bounds.extend(latLng1);
    bounds.extend(latLng2);
    map.fitBounds(bounds);

}
function placeMarkersAndShowRoute_with_index(latLng1, latLng2, route_indx){
    // Define icons
    const icon1 = {
        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent('<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M249.5 428.996C232 428.996 145 251 145 251L354 251C354 251 267 428.996 249.5 428.996Z" fill="#10517D"/><ellipse cx="249.5" cy="192" rx="119.5" ry="121" fill="#10517D"/><circle cx="250" cy="192" r="50" fill="white"/></svg>'),
        scaledSize: new google.maps.Size(80, 80), // Adjust size if needed
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(40, 68)
    };

    const icon2 = {
        url: 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent('<svg width="500" height="500" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M261.925 389.462C259.009 397.051 248.323 397.189 245.21 389.679L130.858 113.765C127.856 106.521 134.907 99.1702 142.269 101.869L246.444 140.052C248.552 140.825 250.872 140.781 252.95 139.931L358.125 96.8919C365.426 93.9042 372.764 101.087 369.934 108.45L261.925 389.462Z" fill="#7ED956"/></svg>'),
        scaledSize: new google.maps.Size(80, 80), // Adjust size if needed
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(41, 63)
    };

    // Place markers
    new google.maps.Marker({
        position: latLng1,
        map: map,
        icon: icon1,
        title: 'Location 1',
    });

    new google.maps.Marker({
        position: latLng2,
        map: map,
        icon: icon2,
        title: 'Location 2',
    });

    // Show routes
    const request = {
        origin: latLng1,
        destination: latLng2,
        travelMode: 'DRIVING',
        provideRouteAlternatives: true // Request alternative routes
    };
    directionsService.route(request, function(result, status) {
        if (status === 'OK') {
            const routes = result.routes.slice(0, 3); // Take up to 3 routes
            routes.forEach((route, index) => {
                if (index === route_indx) {

                    new google.maps.DirectionsRenderer({
                        map: map,
                        directions: result,
                        routeIndex: index, 
                        polylineOptions: {
                            strokeColor: "#4f97c7", 
                            strokeWeight: 3
                        },
                        suppressMarkers: true 
                    });

                    let totalDistance = 0;
                    route.legs.forEach(leg => {
                        totalDistance += leg.distance.value;
                    });
                    document.getElementById("route_len").innerText = `${(totalDistance / 1000).toFixed(2)} km`;                    
                    document.getElementById("r_distance").innerText = `${(totalDistance / 1000).toFixed(2)} km`;                    
                    document.getElementById("recommended_fare").innerText = `₹${(((totalDistance / 1000).toFixed(2)*5)-((totalDistance / 1000).toFixed(2)*5*0.1)).toFixed(2)} to ₹${(((totalDistance / 1000).toFixed(2)*5)+((totalDistance / 1000).toFixed(2)*5*0.1)).toFixed(2)}`;
                    document.getElementById("d_cost").value = ((totalDistance / 1000)*5).toFixed(2);
                    document.getElementById("route_summary").innerText = route.summary;
                    const duration = route.legs[0].duration.text;
                    document.getElementById("r_time").innerText = duration;
                    document.getElementById("r_summary").innerText = route.summary;
                }
            });
            var hasTolls = false;
            var route = result.routes[route_indx];
            const tollElement = document.getElementById("route_toll");
            const tollElement_2 = document.getElementById("r_toll");
            route.legs.forEach(function(leg) {
                leg.steps.forEach(function(step) {
                    if (step.instructions.toLowerCase().includes('toll')) {
                        hasTolls = true;
                    }
                });
            });
            if (hasTolls) {
                    tollElement.innerText = "Tolls applicable";
                    tollElement.style.color = "red";
                    tollElement_2.innerText = "Tolls applicable";
                    tollElement_2.style.color = "red";
                } else {
                    tollElement.innerText = "No tolls";
                    tollElement.style.color = "green";
                    tollElement_2.innerText = "No tolls";
                    tollElement_2.style.color = "green";
                }
            route_indx_dg = route_indx;
        } else {
            alert('Directions request failed due to ' + status);
        }
    });



    // Fit the map to the bounds of the markers
    const bounds = new google.maps.LatLngBounds();
    bounds.extend(latLng1);
    bounds.extend(latLng2);
    map.fitBounds(bounds);
}
function selected_route_highlight(route_indx){
    map = new google.maps.Map(document.getElementById('map_d'), {
        center: { lat: 17.27889429107477, lng: 74.1848932778437 },
        zoom: 15, 
        styles: customMapStyles, 
        disableDefaultUI: true,
        zoomControl: false,
    });
    geocoder = new google.maps.Geocoder();
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({
        suppressMarkers: true 
    });
    directionsRenderer.setMap(map);
    const location1 = document.getElementById('pickup_locationInput_d').value;
    const location2 = document.getElementById('dropoff_locationInput_d').value;

    if (!location1 || !location2) {
        alert("Please enter both locations");
        return;
    }

    geocodeLocation(location1, (latLng1) => {
        if (!latLng1) {
            alert(`Pickup not found: ${location1}`);
            return;
        }
        
        geocodeLocation(location2, (latLng2) => {
            if (!latLng2) {
                alert(`Dropoff not found: ${location2}`);
                return;
            }
            
            // Clear previous directions
            directionsRenderer.set('directions', null);
            
            // Place markers and show route
            pickup_latlng_dg = latLng1;
            dropoff_latlng_dg = latLng2;
            placeMarkersAndShowRoute_with_index(latLng1, latLng2, route_indx);
        });
    });
}
function d_proceed(){
    var pickup_point_d = document.getElementById("dropoff_locationInput_d").value;
    var dropoff_point_d = document.getElementById("pickup_locationInput_d").value;
    var d_seats = document.getElementById("d_seats").value;
    var d_date = document.getElementById("d_date").value;
    var d_time = document.getElementById("d_time").value;
    
    if (pickup_point_d == dropoff_point_d){
        alert("Pickup and dropoff point are same.");
        return;
    }
    if (d_seats < 1){
        alert("Number of seats should be 1 or more than 1.");
        return;
    }
    if (d_seats > 30){
        alert("Maximum seats allowed is 30.");
        return;
    }
    if (d_date.length < 2){
        alert("Please select date.");
        return;
    }
    if (d_time.length < 2){
        alert("Please select time.");
        return;
    }
    document.getElementById("publish-dash").style.display = "none";
    document.getElementById("map-content-publish").style.display = "block";
    showLocations_d();
}
function d_route_confirm(){
    var lbl_1 = document.querySelector('#lbl_1 input');
    var lbl_2 = document.querySelector('#lbl_2 input');
    var lbl_3 = document.querySelector('#lbl_3 input');
    
    if (lbl_1.checked){
        document.getElementById("map-content-publish").style.display = "none";
        document.getElementById("cost-confirm-publish").style.display = "block";
        
    }
    else if (lbl_2.checked){
        document.getElementById("map-content-publish").style.display = "none";
        document.getElementById("cost-confirm-publish").style.display = "block";
        
    }
    else if (lbl_3.checked){
        document.getElementById("map-content-publish").style.display = "none";
        document.getElementById("cost-confirm-publish").style.display = "block";

    }
    else{
        alert("Select one route.");
        return;
    }
}
function d_price_confirm(){
    const distance = parseFloat(document.getElementById("r_distance").innerText);
    console.log("distance", distance);
    const usr_price = document.getElementById("d_cost").value;
    if (usr_price <= ((distance*5)+(distance*5*0.1)) && usr_price >= ((distance*5)-(distance*5*0.1))){
        document.getElementById("d_price_confirm_p").innerText = "..."
        document.getElementById("d_price_confirm").removeEventListener("click", d_price_confirm);
        console.log("requesting server");
        var pickup_name_d = document.getElementById("pickup_locationInput_d").value;
        var dropoff_name_d = document.getElementById("dropoff_locationInput_d").value;
        var d_seats = document.getElementById("d_seats").value;
        var d_date = document.getElementById("d_date").value;
        var d_time = document.getElementById("d_time").value;
        

        fetch('https://b48a-103-234-240-164.ngrok-free.app/d_post', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty,
                "pickup_name_d": pickup_name_d,
                "dropoff_name_d": dropoff_name_d,
                "pickup_latlng_d": pickup_latlng_dg,
                "dropoff_latlng_d": dropoff_latlng_dg,
                "route_indx": route_indx_dg,
                "d_seats": d_seats,
                "d_date": d_date,
                "d_time": d_time,
                "d_cost": usr_price
            })
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                alert("Your ride published successfully.")
                document.getElementById("in_ride").style.display = "block";
                document.getElementById("cost-confirm-publish").style.display = "none";
                document.getElementById("d_price_confirm_p").innerText = "Publish"
                document.getElementById("d_price_confirm").addEventListener("click", d_price_confirm); 
                d_in_ride_content(); 
            }
            else if (data['RESP_STAT'] == "ABORTED"){
                alert(data["MSG"]);
                document.getElementById("d_price_confirm_p").innerText = "Publish"
                document.getElementById("d_price_confirm").addEventListener("click", d_price_confirm);
            }

            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Something went wrong. Please try again after some time.")
        });           


    }
    else{
        alert(`Fare price should be in range ${((distance*5)-(distance*5*0.1))} to ${((distance*5)+(distance*5*0.1))}`);
        return;
    }

}
function d_in_ride_content(){
    fetch('https://b48a-103-234-240-164.ngrok-free.app/d_inride_content/0', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty,})
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                console.log(data['ROUTE_INFO']);
                document.getElementById("i_from").innerText = data["ROUTE_INFO"][0];
                document.getElementById("i_to").innerText = data["ROUTE_INFO"][1];
                document.getElementById("i_scheduled").innerText = `${data["ROUTE_INFO"][2]} to ${data["ROUTE_INFO"][3]}`;
                let parentElement = document.getElementById("cab_request_toapp");
                while (parentElement.firstChild) {
                    parentElement.removeChild(parentElement.firstChild);
                }

                for (var i = 0; i < data["ROUTE_INFO"][6].length; i++){
                    requests_append(i, data["ROUTE_INFO"][6][i])
                }

                for (var i = 0; i < data["ROUTE_INFO"][5].length; i++){
                    requests_accepted_append(i, data["ROUTE_INFO"][5][i])
                }
                

            }

            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Something went wrong. Please try again after some time.")
        }); 
}
function show_cab_info(indx, data){
    document.getElementById("driver_name").innerText = data[0];
    document.getElementById("driver_mobile").innerText = data[1];
    document.getElementById("seats_in_cab").innerText = data[7];
    document.getElementById("cab_info").style.display = "block";
    document.getElementById("cablist-content").style.display = "none";
    let element = document.getElementById("p_cab_request");
    let newElement = element.cloneNode(true);
    element.parentNode.replaceChild(newElement, element);
    
    document.getElementById("p_cab_request").addEventListener("click", function(){ 
        let element = document.getElementById("p_cab_request");
        let newElement = element.cloneNode(true);
        element.parentNode.replaceChild(newElement, element);
        document.getElementById("p_cab_request_p").innerText = "...";
        fetch('https://b48a-103-234-240-164.ngrok-free.app/p_book_cab', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty,
                "driver_mbl": data[1],
                "origin": data[8],
                "destination": data[9],
                "pickup_name": document.getElementById("pickup_locationInput_p").value,
                "dropoff_name": document.getElementById("dropoff_locationInput_p").value,
                "pickup_latlng": pickup_latlng_pg,
                "dropoff_latlng": dropoff_latlng_pg,
                "seats": document.getElementById('n_seats').value
            })
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                alert("Your request was sent to driver.")
                document.getElementById("cab_info").style.display = "none";
                document.getElementById("in_booking").style.display = "block";
                in_booking();
            }

            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Something went wrong. Please try again after some time.")
        });           

     });
    

}
function cabs_append(indx, data){   
//     0
// : 
// "Pratik Suhas Pawar"
// 1
// : 
// "8830998140"
// 2
// : 
// 0.664971132655344
// 3
// : 
// 21.86208356867975
// 4
// : 
// "Sat, 13 Jul 2024 14:04:16 GMT"
// 5
// : 
// "Sat, 13 Jul 2024 15:18:00 GMT"
// 6
// : 
// 74.335
// 7
// : 
// 1
// 8
// : 
// "Kolhapur, Maharashtra, India"
// 9
// : 
// "Pune, Maharashtra, India"
// 10
// : 
// {lat: 16.7049873, lng: 74.24325270000001}
// 11
// : 
// {lat: 18.5204303, lng: 73.8567437}
// 12
// : 
// 0
// 13
// : 
// "1"
// 14
// : 
// "2024-07-13"
// 15
// : 
// "12:24"
// 16
// : 
// "2024-07-13 17:03"
// 17
// : 
// []
// 18
// : 
// []
// 19
// : 
// "1151.33"
    let mainDiv = document.createElement("div");
    mainDiv.className = "round-edge";
    mainDiv.style.cssText = "margin-left: 10%; background-color: transparent; height: 250px; box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);";
    mainDiv.addEventListener("click", function(){
        show_cab_info(indx, data);
    })
    // Create the price paragraph
    let priceParagraph = document.createElement("p");
    priceParagraph.className = "c-bold";
    priceParagraph.style.cssText = "margin-right: 20px; padding-top: 10px; text-align: right; font-size: 18px";
    priceParagraph.textContent = `₹${(parseInt(data[6])*5).toFixed(2)}/-`;
    mainDiv.appendChild(priceParagraph);

    // Create the first time label
    let timeLabel1 = document.createElement("p");
    timeLabel1.className = "c-regular";
    timeLabel1.style.cssText = "position: absolute; margin-left: 20px; margin-top: -25px;";
    timeLabel1.textContent = data[4];
    mainDiv.appendChild(timeLabel1);

    // Create the first search div
    let searchDiv1 = document.createElement("div");
    searchDiv1.style.cssText = "width: 100%; display: flex; justify-content: center; margin-top: -25px;";

    // Create the first inner search div
    let innerSearchDiv1 = document.createElement("div");
    innerSearchDiv1.className = "search c-medium";

    // Create the first inner search paragraph
    let innerSearchParagraph1 = document.createElement("p");
    innerSearchParagraph1.style.cssText = "height: 30px; margin-left: 20px; margin-right: 20px; overflow: scroll;";
    innerSearchParagraph1.textContent = document.getElementById("pickup_locationInput_p").value;

    // Append the inner search paragraph to the inner search div
    innerSearchDiv1.appendChild(innerSearchParagraph1);

    // Append the inner search div to the search div
    searchDiv1.appendChild(innerSearchDiv1);

    // Append the search div to the main div
    mainDiv.appendChild(searchDiv1);

    // Create the first duration paragraph
    let durationParagraph1 = document.createElement("p");
    durationParagraph1.className = "c-light";
    durationParagraph1.style.cssText = "margin-left: 20px; margin-right: 20px; text-align: right; margin-top: 5px;";
    durationParagraph1.textContent = `${data[2]}m`;
    mainDiv.appendChild(durationParagraph1);

    let br1 = document.createElement("br");
    mainDiv.appendChild(br1);

    let br2 = document.createElement("br");
    mainDiv.appendChild(br2);

    // Create the second time label
    let timeLabel2 = document.createElement("p");
    timeLabel2.className = "c-regular";
    timeLabel2.style.cssText = "position: absolute; margin-left: 20px; margin-top: -25px;";
    timeLabel2.textContent = data[5];
    mainDiv.appendChild(timeLabel2);

    // Create the second search div
    let searchDiv2 = document.createElement("div");
    searchDiv2.style.cssText = "width: 100%; display: flex; justify-content: center; margin-top: -25px;";

    // Create the second inner search div
    let innerSearchDiv2 = document.createElement("div");
    innerSearchDiv2.className = "search c-medium";

    // Create the second inner search paragraph
    let innerSearchParagraph2 = document.createElement("p");
    innerSearchParagraph2.style.cssText = "height: 30px; margin-left: 20px; margin-right: 20px; overflow: scroll;";
    innerSearchParagraph2.textContent = document.getElementById("dropoff_locationInput_p").value;

    // Append the inner search paragraph to the inner search div
    innerSearchDiv2.appendChild(innerSearchParagraph2);

    // Append the inner search div to the search div
    searchDiv2.appendChild(innerSearchDiv2);

    // Append the search div to the main div
    mainDiv.appendChild(searchDiv2);

    // Create the second duration paragraph
    let durationParagraph2 = document.createElement("p");
    durationParagraph2.className = "c-light";
    durationParagraph2.style.cssText = "margin-left: 20px; margin-right: 20px; text-align: right; margin-top: 5px;";
    durationParagraph2.textContent = `${data[3]}m`;
    mainDiv.appendChild(durationParagraph2);

    // Append the main div to the body or any other container
    document.getElementById("cab-search-result").appendChild(mainDiv);

}
function show_request_info(indx, data){
    document.getElementById("passanger_name").innerText = data[0];
    document.getElementById("passanger_mobile").innerText = data[1];
    document.getElementById("seat_request").innerText = data[6];
    document.getElementById("pick_p_d").innerText = data[2];
    document.getElementById("drop_p_d").innerText = data[3];
    document.getElementById("request_info").style.display = "block";
    document.getElementById("in_ride").style.display = "none";
    let element = document.getElementById("d_confirm_passanger");
    let newElement = element.cloneNode(true);
    element.parentNode.replaceChild(newElement, element);
    document.getElementById("d_confirm_passanger").addEventListener("click", function(){
        document.getElementById("d_confirm_passanger_p").innerText = "...";

        fetch('https://b48a-103-234-240-164.ngrok-free.app/d_request_accept', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty,
                "passanger_request": data
            })
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                // alert("success");
                document.getElementById('in_ride').style.display = 'block'; 
                document.getElementById('request_info').style.display = 'none';
                d_in_ride_content();
                document.getElementById("d_confirm_passanger_p").innerText = "Request";
        
            }
            else if (data['RESP_STAT'] == "ABORTED") {
                alert("This ride was canceled by the passenger.");
                document.getElementById('in_ride').style.display = 'block'; 
                document.getElementById('request_info').style.display = 'none';
                d_in_ride_content();
                document.getElementById("d_confirm_passanger_p").innerText = "Request";
            }
            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Something went wrong. Please try again after some time.")
        });           

    })
}

function show_accepted_info(indx, data){
    document.getElementById("passanger_name").innerText = data[0];
    document.getElementById("passanger_mobile").innerText = data[1];
    document.getElementById("seat_request").innerText = data[6];
    document.getElementById("pick_p_d").innerText = data[2];
    document.getElementById("drop_p_d").innerText = data[3];
    document.getElementById("request_info").style.display = "block";
    document.getElementById("in_ride").style.display = "none";
    document.getElementById("d_confirm_passanger").style.display = "none";
    
    
}

function requests_append(indx, data){
    console.log("data: ", data);
    // Create the main div with flex display
    let mainDiv = document.createElement("div");
    mainDiv.style.cssText = "display: flex; justify-content: center; width: 100%;";

    // Create the inner round-edge div
    let roundEdgeDiv = document.createElement("div");
    roundEdgeDiv.className = "round-edge";
    roundEdgeDiv.style.cssText = "height: 130px; padding-top: 10px; overflow: scroll;";

    // Create the "From" paragraph
    let fromParagraph = document.createElement("p");
    fromParagraph.className = "c-bold";
    fromParagraph.style.cssText = "font-size: 15px; margin-left: 20px; margin-right: 20px;";
    fromParagraph.innerHTML = `From: <span class="c-light">${data[2]}</span>`;

    // Create the "To" paragraph
    let toParagraph = document.createElement("p");
    toParagraph.className = "c-bold";
    toParagraph.style.cssText = "font-size: 15px; margin-left: 20px; margin-right: 20px;";
    toParagraph.innerHTML = `To: <span class="c-light">${data[3]}</span>`;

    // Create the "Seats" paragraph
    let seatsParagraph = document.createElement("p");
    seatsParagraph.className = "c-bold";
    seatsParagraph.style.cssText = "font-size: 15px; margin-left: 20px; margin-right: 20px;";
    seatsParagraph.innerHTML = `Seats: <span class="c-light">${data[6]}</span>`;

    // Append the paragraphs to the round-edge div
    roundEdgeDiv.appendChild(fromParagraph);
    roundEdgeDiv.appendChild(toParagraph);
    roundEdgeDiv.appendChild(seatsParagraph);

    // Append the round-edge div to the main div
    mainDiv.appendChild(roundEdgeDiv);

    let br = document.createElement("br");

    mainDiv.addEventListener("click", function(){show_request_info(indx, data);})
    document.getElementById("cab_request_toapp").appendChild(br);
    document.getElementById("cab_request_toapp").appendChild(mainDiv);


}

function requests_accepted_append(indx, data){
    console.log("data: ", data);
    // Create the main div with flex display
    let mainDiv = document.createElement("div");
    mainDiv.style.cssText = "display: flex; justify-content: center; width: 100%;";

    // Create the inner round-edge div
    let roundEdgeDiv = document.createElement("div");
    roundEdgeDiv.className = "round-edge";
    roundEdgeDiv.style.cssText = "height: 130px; padding-top: 10px; overflow: scroll;";

    // Create the "From" paragraph
    let fromParagraph = document.createElement("p");
    fromParagraph.className = "c-bold";
    fromParagraph.style.cssText = "font-size: 15px; margin-left: 20px; margin-right: 20px;";
    fromParagraph.innerHTML = `From: <span class="c-light">${data[2]}</span>`;

    // Create the "To" paragraph
    let toParagraph = document.createElement("p");
    toParagraph.className = "c-bold";
    toParagraph.style.cssText = "font-size: 15px; margin-left: 20px; margin-right: 20px;";
    toParagraph.innerHTML = `To: <span class="c-light">${data[3]}</span>`;

    // Create the "Seats" paragraph
    let seatsParagraph = document.createElement("p");
    seatsParagraph.className = "c-bold";
    seatsParagraph.style.cssText = "font-size: 15px; margin-left: 20px; margin-right: 20px;";
    seatsParagraph.innerHTML = `Seats: <span class="c-light">${data[6]}</span>`;

    // Append the paragraphs to the round-edge div
    roundEdgeDiv.appendChild(fromParagraph);
    roundEdgeDiv.appendChild(toParagraph);
    roundEdgeDiv.appendChild(seatsParagraph);

    // Append the round-edge div to the main div
    mainDiv.appendChild(roundEdgeDiv);

    let br = document.createElement("br");

    mainDiv.addEventListener("click", function(){show_accepted_info(indx, data);})
    document.getElementById("cab_accept_toapp").appendChild(br);
    document.getElementById("cab_accept_toapp").appendChild(mainDiv);
}
function in_booking(){
    fetch('https://b48a-103-234-240-164.ngrok-free.app/in_booking', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty,
               
            })
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                console.log("in_booking data: ", data)
                if (data['STAT'] == "PENDING"){
                    console.log("pending")
                    document.getElementById("in_booking").style.display = "block";
                    document.getElementById("dashb-content").style.display = "none";
                    document.getElementById("p_cancel_booking").style.display = "flex";
                    document.getElementById("p_from_inbooking").innerText = data['ORG'];
                    document.getElementById("p_to_inbooking").innerText = data["DEST"];
                    document.getElementById("p_seats_inbooking").innerText = data["SEATS"];
                    document.getElementById("p_D_Name").innerText = data["D_NAME"];
                    document.getElementById("p_D_Mbl").innerText = data["D_MOB"];
                    document.getElementById("p_cancel_booking").addEventListener("click", function(){
                        fetch('https://b48a-103-234-240-164.ngrok-free.app/cancel_booking', {
                            method: 'POST',
                            credentials: 'include',
                            
                            headers: {
                                'Content-Type': 'application/json',
                                'Access-Control-Allow-Credentials': 'true',
                            },
                            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty})
                            
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            return response.json();
                        })
                        .then(data => {
                            console.log('Response from server:', data);
                            if (data['RESP_STAT'] == "SUCCESS") {
                                alert("Your ride canceled successfully");
                                document.getElementById("in_booking").style.display = "none";
                                document.getElementById("dashb-content").style.display = "block";
                                window.location.reload();
                            }
                            else {
                                alert("Error with your profile. Please login again.");
                                logout();
                            }
                        })
                        .catch(error => {
                            console.error('There was a problem with the fetch operation:', error);
                            alert("Cannot connet to server. Please check your internet connection and try after sometime.")
                        });
                    })
                    


                }
                else if (data['STAT'] == "APPROVED"){
                    document.getElementById("in_booking").style.display = "block";
                    document.getElementById("dashb-content").style.display = "none";
                    document.getElementById("p_cancel_booking").style.display = "none";
                    document.getElementById("approved_ride").style.display = "flex";
                    document.getElementById("p_from_inbooking").innerText = data['ORG'];
                    document.getElementById("p_to_inbooking").innerText = data["DEST"];
                    document.getElementById("p_seats_inbooking").innerText = data["SEATS"];
                    document.getElementById("p_D_Name").innerText = data["D_NAME"];
                    document.getElementById("p_D_Mbl").innerText = data["D_MOB"];
                    
                }
                else if (data['STAT'] == "COMPLETED"){
                    document.getElementById("in_booking").style.display = "none";
                    document.getElementById("dashb-content").style.display = "block";
                }
                
            }

            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Something went wrong. Please try again after some time.")
        });           

     
}

function on_load() {
    document.getElementById("progress-bar").style.display = "flex";
    document.getElementById("home-div").addEventListener("click", home_btn_disp);
    document.getElementById("publish-div").addEventListener("click", publish_btn_disp);
    document.getElementById("profile-div").addEventListener("click", profile_btn_disp);
    document.getElementById("prof").addEventListener("click", profile_section);
    document.getElementById("acc").addEventListener("click", account_section);
    document.getElementById("logout_btn").addEventListener("click", logout);
    document.getElementById("p_go").addEventListener("click", p_go);
    // document.getElementById("p_go").addEventListener("click", showLocations_p);
    document.addEventListener('click', clck);
    document.getElementById("date_highlt_0").addEventListener("click", function(){day_select_highlt(0);});
    document.getElementById("date_highlt_1").addEventListener("click", function(){day_select_highlt(1);});
    document.getElementById("date_highlt_2").addEventListener("click", function(){day_select_highlt(2);});
    document.getElementById("date_highlt_3").addEventListener("click", function(){day_select_highlt(3);});
    document.getElementById("date_highlt_4").addEventListener("click", function(){day_select_highlt(4);});
    document.getElementById("lbl_1").addEventListener("click", function(){selected_route_highlight(0);});
    document.getElementById("lbl_2").addEventListener("click", function(){selected_route_highlight(1);});
    document.getElementById("lbl_3").addEventListener("click", function(){selected_route_highlight(2);});
    document.getElementById("d_route_confirm").addEventListener("click", d_route_confirm);
    document.getElementById("d_price_confirm").addEventListener("click", d_price_confirm);
    document.getElementById('p_search_cabs').addEventListener("click", p_search_cabs);
    document.getElementById("d_verification").addEventListener("click", function(){window.location.href = "/driver-verification";});
    document.getElementById("d_renew").addEventListener("click", function(){window.location.href = "/driver-renew";});
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
    else{
        
        home_btn_disp();
        // publish_btn_disp();
        // profile_btn_disp();

        fetch('https://b48a-103-234-240-164.ngrok-free.app/get_homepage_da', {
            method: 'POST',
            credentials: 'include',
            
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Credentials': 'true',
            },
            body: JSON.stringify({"auth_toc_usr": auth_toc_usr, 'local_str': usr_verify.slice(1, -1), "loyalty": loyalty})
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data['RESP_STAT'] == "SUCCESS") {
                document.getElementById("today_date").innerText = data["TODAY"];
                document.getElementById("tomorrow_date").innerText = data["TOMORROW"];
                document.getElementById("day_after_tomorrow_date").innerText = data["DATE_AFTER_TOMORROW"];
                document.getElementById("thrid_date").innerText = data["THIRD_DATE"];
                document.getElementById("forth_date").innerText = data["FORTH_DATE"];
                document.getElementById("day_after_tomorrow_day").innerText = data["DAY_AFTER_TOMORROW"];
                document.getElementById("thrid_day").innerText = data["THIRD_DAY"];
                document.getElementById("forth_day").innerText = data['FORTH_DAY'];
                document.getElementById("usr-name").innerText = data['USR_NAME'].split(" ")[0];
                document.getElementById("cust_name").innerText = data['USR_NAME'].split(" ")[0];

                if (data["RIDE_STAT"] == 1){
                    document.getElementById("publish-dash").style.display = "none";
                    document.getElementById("in_ride").style.display = "block";
                    d_in_ride_content();
                }
                if (data["BOOK_STAT"] == 1){
                    document.getElementById("dashb-content").style.display = "none";
                    document.getElementById("in_booking").style.display = "block";
                    in_booking();
                }
                else if (data["BOOK_STAT"] == 2){
                    document.getElementById("dashb-content").style.display = "none";
                    document.getElementById("in_booking").style.display = "block";
                    in_booking();
                }
                if (data["DRIVING_FLAG"] == 0){
                    document.getElementById("DRIVER_F_0").style.display = "flex";
                }
                else if (data["DRIVING_FLAG"] == 1){
                    document.getElementById("DRIVER_F_1").style.display = "flex";

                }
                else if (data["DRIVING_FLAG"] == 2){
                    document.getElementById("DRIVER_F_2").style.display = "flex";
                    document.getElementById("d_publish").addEventListener("click", d_proceed);
                }
                // fetch_loc();
                document.getElementById("progress-bar").style.display = "none";
            }
            else {
                alert("Error with your profile. Please login again.");
                logout();
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert("Cannot connet to server. Please check your internet connection and try after sometime.")
        });           
    }

    const pickup_inp_p = document.getElementById('pickup_locationInput_p');
    const dropoff_inp_p = document.getElementById('dropoff_locationInput_p');

    pickup_inp_p.addEventListener("keyup", fetchLocations_1);
    pickup_inp_p.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === 'Tab') {
            e.preventDefault();
            if (pickup_inp_p.value.length >= 1){
                document.getElementById("pickup_dropdownContent_p").style.display = "none";
                pickup_inp_p.value = document.getElementById("pickup_dropdownContent_p").firstChild.innerText;
                dropoff_inp_p.focus();
            }
            else{
                document.getElementById("pickup_dropdownContent_p").style.display = "none";
            }
        }
    });
    // pickup_inp_p.addEventListener("blur", function(){
    //     if (pickup_inp_p.value.length >= 1){
    //         document.getElementById("pickup_dropdownContent_p").style.display = "none";
    //         pickup_inp_p.value = document.getElementById("pickup_dropdownContent_p").firstChild.innerText;
    //     }
    //     else{
    //         document.getElementById("pickup_dropdownContent_p").style.display = "none";
    //     }
    // });
    dropoff_inp_p.addEventListener("keyup", fetchLocations_2);
    dropoff_inp_p.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === 'Tab') {

            if (dropoff_inp_p.value.length >= 1){
                document.getElementById("dropoff_dropdownContent_p").style.display = "none";
                dropoff_inp_p.value = document.getElementById("dropoff_dropdownContent_p").firstChild.innerText;
                dropoff_inp_p.blur();
            }
            else{
                document.getElementById("dropoff_dropdownContent_p").style.display = "none";
            }
        }
    });
    // dropoff_inp_p.addEventListener("blur", function(){
    //     if (dropoff_inp_p.value.length >= 1){
    //         document.getElementById("dropoff_dropdownContent_p").style.display = "none";
    //         dropoff_inp_p.value = document.getElementById("dropoff_dropdownContent_p").firstChild.innerText;
    //     }
    //     else{
    //         document.getElementById("dropoff_dropdownContent_p").style.display = "none";
    //     }
    // });


    const pickup_inp_d = document.getElementById('pickup_locationInput_d');
    const dropoff_inp_d = document.getElementById('dropoff_locationInput_d');

    pickup_inp_d.addEventListener("keyup", fetchLocations_3);
    pickup_inp_d.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === 'Tab') {
            e.preventDefault();
            if (pickup_inp_d.value.length >= 1){
                document.getElementById("pickup_dropdownContent_d").style.display = "none";
                pickup_inp_d.value = document.getElementById("pickup_dropdownContent_d").firstChild.innerText;
                dropoff_inp_d.focus();
            }
            else{
                document.getElementById("pickup_dropdownContent_d").style.display = "none";
            }
        }
    });
    dropoff_inp_d.addEventListener("keyup", fetchLocations_4);
    dropoff_inp_d.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === 'Tab') {

            if (dropoff_inp_d.value.length >= 1){
                document.getElementById("dropoff_dropdownContent_d").style.display = "none";
                dropoff_inp_d.value = document.getElementById("dropoff_dropdownContent_d").firstChild.innerText;
                dropoff_inp_d.blur();
            }
            else{
                document.getElementById("dropoff_dropdownContent_d").style.display = "none";
            }
        }
    });
    
}

export default {
  mounted() {
    on_load();
  }
};

</script>
